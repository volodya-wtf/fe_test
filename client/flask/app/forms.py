from wtforms import Form, StringField, PasswordField, SubmitField, validators
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField("Email")
    password = PasswordField("Password")
 
    submit = SubmitField("Log In")


class InsertForm(FlaskForm):
    title = StringField("Название пробы")
    month = StringField("Месяц")
    Fe = StringField("Fe")
    Ca = StringField("Ca")
    S = StringField("S")
    Si = StringField("Si")
    Al = StringField("Al")

    submit = SubmitField("Отправить данные")


class StatsForm(Form):
    month = StringField("Месяц")
 
    submit = SubmitField("Log In")
