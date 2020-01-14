from flask import Flask, request, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FloatField, IntegerField
from wtforms.validators import Email, input_required, length 
from flask_bootstrap import Bootstrap
from flask_wtf.file import FileField, FileRequired
from app import app
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