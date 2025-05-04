from database import engine
from database import Base  

Base.metadata.create_all(bind=engine)

print("Missing tables created (if any).")
