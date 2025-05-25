from database import engine
from database import Base  
from models import pay

Base.metadata.create_all(bind=engine)

print("Missing tables created (if any).")
