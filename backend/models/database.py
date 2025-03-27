from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection
DATABASE_URL = "sqlite:///./tax_data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model
Base = declarative_base()

# Define TaxReceipt model
class TaxReceipt(Base):
    __tablename__ = "tax_receipts"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    total_amount = Column(Float)
    tax_amount = Column(Float)
    tax_percentage = Column(Float)
    date = Column(String)

# Create database tables
Base.metadata.create_all(bind=engine)
