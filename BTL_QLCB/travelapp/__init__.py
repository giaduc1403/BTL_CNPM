from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_admin import Admin
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)

app.secret_key = '$#&*&%$(*&^(*^*&%^%$#^%&^%*&56547648764%$#^%$&12312^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/btl_qlcb?charset=utf8mb4' % quote(
    'Duc@1403')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name='QUẢN TRỊ VIÊN', template_mode='bootstrap4')

login = LoginManager(app=app)

cloudinary.config(cloud_name='dgz1wkqrt', api_key='512592613742133', api_secret='-ZHOru7h2yd4UnOdzTcJVvKMQBA')
