from fastapi import APIRouter, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import razorpay 
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from database import get_db
from models.pay import Payment  # Import the Payment model

# Load environment variables
load_dotenv()

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Create a router without a prefix - the prefix will be added in the main app
router = APIRouter()

# Debug: Print environment variables (mask the secret for security)
key_id = os.getenv("RAZORPAY_KEY_ID")
key_secret = os.getenv("RAZORPAY_KEY_SECRET")
print(f"RAZORPAY_KEY_ID: {'Found' if key_id else 'Not found'}")
if key_id:
    print(f"Key ID: {key_id[:4]}{'*' * (len(key_id) - 8)}{key_id[-4:] if len(key_id) > 8 else ''}")
print(f"RAZORPAY_KEY_SECRET: {'Found' if key_secret else 'Not found'}")
if key_secret:
    print(f"Key Secret: {key_secret[:4]}{'*' * (len(key_secret) - 8)}{key_secret[-4:] if len(key_secret) > 8 else ''}")

# Configure Razorpay client
razorpay_client = razorpay.Client(
    auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))
)

# Models
class OrderRequest(BaseModel):
    amount: float
    currency: str = "INR"
    receipt: str = None
    notes: dict = None

class RefundRequest(BaseModel):
    amount: float = None  # Optional for partial refunds
    notes: dict = None

# Serve the HTML file at the root of this router
@router.get("/", response_class=HTMLResponse)
async def get_payment_page():
    """Serve the payment page HTML"""
    return FileResponse("templates/pay.html")

# Payment Endpoints
@router.post("/create-order")
async def create_order(order_request: OrderRequest):
    """Create a Razorpay order"""
    
    # Validate if amount is correctly passed
    if not order_request.amount or order_request.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    # Convert amount to paise (Razorpay uses the smallest currency unit)
    amount_in_paise = int(order_request.amount * 100)
    print(f"Amount in paise: {amount_in_paise}")  # Log for debugging
    
    # Create order data
    order_data = {
        'amount': amount_in_paise,
        'currency': order_request.currency,
        'receipt': order_request.receipt,
        'notes': order_request.notes
    }

    try:
        # Create order using Razorpay client
        order = razorpay_client.order.create(data=order_data)
        print(f"Order created: {order}")  # Log the order details
        
        # Send the order details and Razorpay key ID to frontend
        return {
            "order_id": order['id'],
            "amount": order['amount'],  # Don't convert back to rupees - keep in paise
            "currency": order['currency'],
            "key_id": os.getenv("RAZORPAY_KEY_ID")  # Your Razorpay key from environment variable
        }
    except Exception as e:
        print("ORDER CREATION ERROR:", str(e))  # Log the exact error
        raise HTTPException(status_code=400, detail=f"Failed to create order: {str(e)}")

@router.post("/verify-payment")
async def verify_payment(
    request: Request,
    razorpay_payment_id: str = Form(...),
    razorpay_order_id: str = Form(...),
    razorpay_signature: str = Form(...),
    customer_name: str = Form(...),
    customer_email: str = Form(...),
    customer_mobile: str = Form(...),
    customer_address: str = Form(...),
    db: Session = Depends(get_db)
):
    """Verify payment signature and save payment details to database"""
    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        'razorpay_signature': razorpay_signature
    }

    try:
        razorpay_client.utility.verify_payment_signature(params_dict)

        # Save payment to DB
        new_payment = Payment(
            razorpay_order_id=razorpay_order_id,
            razorpay_payment_id=razorpay_payment_id,
            razorpay_signature=razorpay_signature,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_mobile=customer_mobile,
            customer_address=customer_address,
            amount=None,  # We'll fill it below
            currency="INR"
        )

        # Optionally fetch order details to get the amount
        order = razorpay_client.order.fetch(razorpay_order_id)
        if order:
            new_payment.amount = order.get("amount", 0) / 100  # Convert from paise

        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

        return {"status": "success", "message": "Payment verified and saved"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Payment verification failed: {str(e)}")
    
@router.get("/{submission_id}", response_class=HTMLResponse)
async def pay_for_submission(submission_id: int):
    return FileResponse("templates/pay.html")


# Export the router for inclusion in the main app
# This line is crucial - it allows your main app to import this router
# The main app will do: app.include_router(pay.router, prefix="/pay", tags=["pay"])