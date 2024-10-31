# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.orm import relationship
from datetime import date

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Customer(name='{self.name}', email='{self.email}')>"


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Product(name='{self.name}', price='{self.price}')>"


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(String, nullable=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=True)
    order_date = Column(DateTime, default=datetime.now)
    status = Column(String, nullable=True)
    total_amount = Column(Float, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Order(order_number='{self.order_number}', status='{self.status}')>"


class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=True)
    quantity = Column(Integer, nullable=True)
    item_price = Column(Float, nullable=True)
    total_price = Column(Float, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<OrderItem(order_id='{self.order_id}', product_id='{self.product_id}', quantity='{self.quantity}')>"


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Cart(customer_id='{self.customer_id}')>"


class CartItem(Base):
    __tablename__ = 'cart_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=True)
    quantity = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<CartItem(cart_id='{self.cart_id}', product_id='{self.product_id}', quantity='{self.quantity}')>"


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Category(name='{self.name}')>"


class ProductCategoryLink(Base):
    __tablename__ = 'product_category_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<ProductCategoryLink(product_id='{self.product_id}', category_id='{self.category_id}')>"


class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    contact_info = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Supplier(name='{self.name}')>"


class ProductSupplierLink(Base):
    __tablename__ = 'product_supplier_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=True)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<ProductSupplierLink(product_id='{self.product_id}', supplier_id='{self.supplier_id}')>"


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=True)
    rating = Column(Integer, nullable=True)
    review_text = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Review(product_id='{self.product_id}', customer_id='{self.customer_id}', rating='{self.rating}')>"


class Discount(Base):
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=True)
    description = Column(String, nullable=True)
    percentage = Column(Float, nullable=True)
    valid_from = Column(DateTime, nullable=True)
    valid_to = Column(DateTime, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<Discount(code='{self.code}', percentage='{self.percentage}')>"


class OrderDiscountLink(Base):
    __tablename__ = 'order_discount_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=True)
    discount_id = Column(Integer, ForeignKey('discount.id'), nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=True)
    updated_date = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f"<OrderDiscountLink(order_id='{self.order_id}', discount_id='{self.discount_id}')>"


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# ALS/GenAI: Prepare for sample data

# Populating the database with sample data
from sqlalchemy.orm import Session

session = Session(bind=engine)

# Customers
customer_1 = Customer(name="John Doe", email="john.doe@example.com", created_by="system")
session.add(customer_1)
session.commit()

# Products
product_1 = Product(name="Men's Golf Shoe A", description="High quality golf shoe", price=120.00, created_by="admin")
product_2 = Product(name="Men's Golf Shoe B", description="Premium leather golf shoe", price=150.00, created_by="admin")
session.add_all([product_1, product_2])
session.commit()

# Orders
order_1 = Order(order_number="ORD1001", customer_id=customer_1.id, status="Pending", total_amount=270.00, created_by="system")
session.add(order_1)
session.commit()

# Order Items
order_item_1 = OrderItem(order_id=order_1.id, product_id=product_1.id, quantity=1, item_price=120.00, total_price=120.00, created_by="system")
order_item_2 = OrderItem(order_id=order_1.id, product_id=product_2.id, quantity=1, item_price=150.00, total_price=150.00, created_by="system")
session.add_all([order_item_1, order_item_2])
session.commit()

# Carts
cart = Cart(customer_id=customer_1.id, created_by="auto")
session.add(cart)
session.commit()

# Cart Items
cart_item = CartItem(cart_id=cart.id, product_id=product_1.id, quantity=1, created_by="auto")
session.add(cart_item)
session.commit()

# Categories
category = Category(name="Shoes", description="Footwear category", created_by="system")
session.add(category)
session.commit()

# Product-Category Links
product_category_link = ProductCategoryLink(product_id=product_1.id, category_id=category.id, created_by="system")
session.add(product_category_link)
session.commit()

# Suppliers
supplier = Supplier(name="Golf Supplies Inc.", contact_info="123-456-7890", created_by="admin")
session.add(supplier)
session.commit()

# Product-Supplier Links
product_supplier_link = ProductSupplierLink(product_id=product_1.id, supplier_id=supplier.id, created_by="admin")
session.add(product_supplier_link)
session.commit()

# Reviews
review = Review(product_id=product_1.id, customer_id=customer_1.id, rating=5, review_text="Excellent shoe!", created_by="auto")
session.add(review)
session.commit()

# Discounts
discount = Discount(code="SAVE20", description="Save 20% on your next purchase", percentage=20.0, 
                    valid_from=datetime(2023, 1, 1), valid_to=datetime(2023, 12, 31), created_by="marketing")
session.add(discount)
session.commit()

# Order-Discount Links
order_discount_link = OrderDiscountLink(order_id=order_1.id, discount_id=discount.id, created_by="system")
session.add(order_discount_link)
session.commit()

session.close()


session.add_all([customer_1, product_1, product_2, order_1, order_item_1, order_item_2, cart, cart_item, category, product_category_link, supplier, product_supplier_link, review, discount, order_discount_link])
session.commit()
