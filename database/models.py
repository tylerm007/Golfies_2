# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 31, 2024 13:47:49
# Database: sqlite:////tmp/tmp.wYCAw7lpYs/Golfies_2/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductCategoryLinkList : Mapped[List["ProductCategoryLink"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    CartList : Mapped[List["Cart"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")



class Discount(SAFRSBaseX, Base):
    __tablename__ = 'discount'
    _s_collection_name = 'Discount'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    description = Column(String)
    percentage = Column(Float)
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderDiscountLinkList : Mapped[List["OrderDiscountLink"]] = relationship(back_populates="discount")



class Product(SAFRSBaseX, Base):
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductCategoryLinkList : Mapped[List["ProductCategoryLink"]] = relationship(back_populates="product")
    ProductSupplierLinkList : Mapped[List["ProductSupplierLink"]] = relationship(back_populates="product")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="product")
    CartItemList : Mapped[List["CartItem"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")



class Supplier(SAFRSBaseX, Base):
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductSupplierLinkList : Mapped[List["ProductSupplierLink"]] = relationship(back_populates="supplier")



class Cart(SAFRSBaseX, Base):
    __tablename__ = 'cart'
    _s_collection_name = 'Cart'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CartList"))

    # child relationships (access children)
    CartItemList : Mapped[List["CartItem"]] = relationship(back_populates="cart")



class Order(SAFRSBaseX, Base):
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_number = Column(String)
    customer_id = Column(ForeignKey('customer.id'))
    order_date = Column(DateTime)
    status = Column(String)
    total_amount = Column(Float)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDiscountLinkList : Mapped[List["OrderDiscountLink"]] = relationship(back_populates="order")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class ProductCategoryLink(SAFRSBaseX, Base):
    __tablename__ = 'product_category_link'
    _s_collection_name = 'ProductCategoryLink'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    category_id = Column(ForeignKey('category.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductCategoryLinkList"))
    product : Mapped["Product"] = relationship(back_populates=("ProductCategoryLinkList"))

    # child relationships (access children)



class ProductSupplierLink(SAFRSBaseX, Base):
    __tablename__ = 'product_supplier_link'
    _s_collection_name = 'ProductSupplierLink'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    supplier_id = Column(ForeignKey('supplier.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductSupplierLinkList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductSupplierLinkList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    customer_id = Column(ForeignKey('customer.id'))
    rating = Column(Integer)
    review_text = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    product : Mapped["Product"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class CartItem(SAFRSBaseX, Base):
    __tablename__ = 'cart_item'
    _s_collection_name = 'CartItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    cart_id = Column(ForeignKey('cart.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    cart : Mapped["Cart"] = relationship(back_populates=("CartItemList"))
    product : Mapped["Product"] = relationship(back_populates=("CartItemList"))

    # child relationships (access children)



class OrderDiscountLink(SAFRSBaseX, Base):
    __tablename__ = 'order_discount_link'
    _s_collection_name = 'OrderDiscountLink'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    discount_id = Column(ForeignKey('discount.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    discount : Mapped["Discount"] = relationship(back_populates=("OrderDiscountLinkList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderDiscountLinkList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer)
    item_price = Column(Float)
    total_price = Column(Float)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)
