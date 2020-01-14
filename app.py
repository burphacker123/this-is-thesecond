from flask import Flask, request, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FloatField, IntegerField
from wtforms.validators import Email, input_required, length 
from flask_bootstrap import Bootstrap
from flask_wtf.file import FileField, FileRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Cart(FlaskForm):
    id = IntegerField("id", validators=[None])
    image = FileField('image', validators=[FileRequired()])
    name = StringField('name', validators=[input_required(), length(min=4, max=50)])
    price = FloatField('price', validators=[input_required()])
    description = StringField('description', validators=[input_required(), length(min=40, max=5000)])
class ProdForm(FlaskForm):
    id = IntegerField("id", validators=[None])
    image = FileField('image', validators=[FileRequired()])
    name = StringField('name', validators=[input_required(), length(min=4, max=50)])
    price = FloatField('price', validators=[input_required()])
    description = StringField('description', validators=[input_required(), length(min=40, max=5000)])
class Prod1(FlaskForm):
    id = IntegerField("id", validators=[None])
    image = FileField('image', validators=[FileRequired()])
    name = StringField('name', validators=[input_required(), length(min=4, max=50)])
    price = FloatField('price', validators=[input_required()])
    description = StringField('description', validators=[input_required(), length(min=40, max=5000)])
class ProdForm2(FlaskForm):
    id = IntegerField("id", validators=[None])
    image = FileField('image', validators=[FileRequired()])
    name = StringField('name', validators=[input_required(), length(min=4, max=50)])
    price = FloatField('price', validators=[input_required()])
    description = StringField('description', validators=[input_required(), length(min=40, max=5000)])
class Prod2(FlaskForm):
    id = IntegerField("id", validators=[None])
    image = FileField('image', validators=[FileRequired()])
    name = StringField('name', validators=[input_required(), length(min=4, max=50)])
    price = FloatField('price', validators=[input_required()])
    description = StringField('description', validators=[input_required(), length(min=40, max=5000)])
class loginform(FlaskForm):
    username = StringField('username', validators=[input_required(), length(min=4, max=40)])
    password = PasswordField('password', validators=[input_required(), length(min=8, max=40)])
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/cart")
def cart():
    return render_template('cart.html')
@app.route("/checkout")
def checkout():
    return render_template('checkout.html')
@app.route("/contact")
def contact():
    return render_template('contact-us.html')
@app.route("/shop")
def shop():
    prods = Prod1.query.order_by(Prod1.id).all()   
    return render_template('shop.html', prods = prods)
@app.route("/natural")
def shopnd():
    return render_template('shop2.html')
@app.route("/add")
def add():
    pass
@app.route('/seccessful/admin', methods=['GET', 'POST'])
def admin():
    prod = ProdForm()
    nat = Prod1(name=prod.name.data, price=prod.price.data, image=prod.image.data, des=prod.description.data)
    db.session.add(nat)
    return render_template('admin.html', prodst = prod)
class User():
    login = 'hmned@gmail.com'
    password = 123456789
@app.route('/login', methods=['GET', 'POST'])

def login():
    Form = loginform()
    user = User()
    if Form.validate_on_submit():
        if Form.username.data == user.login and Form.password.data == user.password:
            return redirect('/seccessful/admin')
        else:
            return redirect('/seccessful/admin')
    else:
        return render_template('login.html', form = Form)
@app.route('/description/prod<int>')
def show():
    pass


if __name__  == '__main__':
    app.run(debug=True)