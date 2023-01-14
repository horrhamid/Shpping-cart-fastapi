from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base  = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String)
    password = Column(String)


class Cart(Base):
    __tablename__= 'cart'
    id = Column(Integer, primary_key=True, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())

    desc = Column(String)
    user_id = Column(Integer, ForeignKey(
        'user.id'), nullable=False)
    user = relationship('User')

class Products(Base):
    __tablename__= 'product'
    id = Column(Integer, primary_key=True, nullable=False)
    product_code = Column(Integer)
    title = Column(String)
    price = Column(Numeric)
    description = Column(String)
    category = Column(String)

    cart_id = Column(Integer, ForeignKey(
        'cart.id', ondelete='CASCADE'), nullable=False)
    cart = relationship('Cart')
    


