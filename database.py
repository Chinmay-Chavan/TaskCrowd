# db.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = "mysql+pymysql://remote_user:root@192.168.1.8/mydb"



DATABASE_URL = "mysql+pymysql://remote_user:root@192.168.1.2/mydb"




engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    password = Column(String(100))
    lusername = Column(String(100))
    email = Column(String(100))
    role = Column(String(100))

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()