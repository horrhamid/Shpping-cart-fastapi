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



@router.post('/products')
def create_posts(product: schema.CreateProductSchema, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {'status': 'success', 'Product': new_product}


@router.get('/carts')
def get_carts(db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    products = db.query(models.Cart).filter(models.Cart.user_id==user_id).all()
    return {'status': 'success', 'results': len(products), 'Carts': products}


@router.post('/carts')
def create_cart(cart: schema.CreateCartSchema, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    temp = cart.dict()
    temp["user_id"] = user_id
    new_cart = models.Cart(**temp)

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)

    return {'status': 'success', 'Cart': new_cart}


@router.get('/carts/{cart_id}')
def get_cart(cart_id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    carts = db.query(models.Cart).filter(models.Cart.user_id==user_id, 
                        models.Cart.id==int(cart_id)).first()

    product_in_cart = db.query(models.Products).filter(models.Products.cart_id == int(cart_id)).all()    
    return {'status': 'success', 'results': 1, 'Cart': carts, "products in cart": product_in_cart}


@router.post('/carts/{cart_id}')
def create_cart(cart_id: str, prdc: schema.AddProductToCartSchema, db: Session = Depends(get_db), 
                user_id: str = Depends(require_user)):
    
    cart = db.query(models.Cart).filter(models.Cart.user_id==user_id, 
                        models.Cart.id==int(cart_id)).first()

    if cart != [] :
        try:
            t_id = prdc.dict()["product_id"]
            print(t_id)
            product = db.query(models.Product).filter(models.Product.id == int(t_id)).first()
            print(product)
        except Exception as e:
            return {'status': 'Failed1', 'Error': e}

        try:
            id = len(db.query(models.Products).all()) + 1
            new_products = models.Products(id = id, product_code = prdc.dict()["product_id"],
                                            description = product.description, cart_id = int(cart_id))
            db.add(new_products)
            db.commit()
            db.refresh(new_products)
            return {'status': 'success', 'Cart': new_products}
        except Exception as e:
            return {'status': 'Failed2', 'Error': e}
        
    return {'status': 'Failed', 'Error': "Cart not Founded!"}

        

    