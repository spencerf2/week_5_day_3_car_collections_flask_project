from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify
    
    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database.'

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(75))
    model = db.Column(db.String(100), nullable = True)
    price = db.Column(db.Numeric(precision=10, scale=2))
    battery_size = db.Column(db.String(50), nullable = True)
    range_on_one_charge = db.Column(db.String(100), nullable = True)
    max_speed = db.Column(db.String(100))
    dimensions = db.Column(db.String(100))
    weight = db.Column(db.String(50))
    cost_of_prod = db.Column(db.Numeric(precision = 10, scale = 2))
    year = db.Column(db.String(4))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, make, model, price, battery_size, range_on_one_charge, max_speed, dimensions, weight, cost_of_product, year, user_token, id=''):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.price = price
        self.battery_size = battery_size
        self.range_on_one_charge = range_on_one_charge
        self.max_speed = max_speed
        self.dimensions = dimensions
        self.weight = weight
        self.cost_of_prod = cost_of_product
        self.year = year
        self.user_token = user_token

    def __repr__(self):
        return f'The following Car has been added: {self.make}'
    
    def set_id(self):
        return secrets.token_urlsafe()

# Creation of API Schema via the Marshmallow Object
class CarSchema(ma.Schema):
    class Meta:
        fields = ['id', 'make','model', 'price', 'battery_size', 'range_on_one_charge', 'max_speed', 'dimensions', 'weight', 'cost_of_product', 'year']


car_schema = CarSchema()
cars_schema = CarSchema(many = True)