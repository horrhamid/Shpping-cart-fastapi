from datetime import datetime
import uuid
from db import schema, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.database import get_db
from app.oauth2 import require_user


router = APIRouter()


@router.get('/products')
def get_posts(db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    products = db.query(models.Product).all()
    return {'status': 'success', 'results': len(products), 'Products': products}


@router.get('/carts')
def get_posts(db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    products = db.query(models.Cart).filter(models.Cart.user_id==user_id).all()
    return {'status': 'success', 'results': len(products), 'Carts': products}

@router.get('/carts/{cart_id}')
def get_posts(cart_id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    carts = db.query(models.Cart).filter(models.Cart.user_id==user_id, 
                        models.Cart.id==int(cart_id)).first()

    product_in_cart = db.query(models.Products).filter(cart_id == int(cart_id)).all()    
    return {'status': 'success', 'results': 1, 'Cart': carts, "products in cart": product_in_cart}