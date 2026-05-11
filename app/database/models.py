from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    category = Column(String)
    response = Column(String)
    status = Column(String)