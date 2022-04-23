import requests
import json
import os

from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask.views import View, MethodView


from app import app
from app.db import SessionManager
from app.forms import LoginForm, InsertForm, StatsForm
from app.requests import auth, insert_sample, stats_sample_avg, stats_sample_max, stats_sample_min


s = SessionManager(session)


class Login(MethodView):
    def get(self):

        form = LoginForm()
        return render_template("login.html", form=form)

    def post(self):
        data = {
            "email": request.form["email"],
            "password": request.form["password"],
        }
        # url = "http://172.16.0.5:8000/auth/"  # todo: Перенести в .env

        response = auth(data)
        data = json.loads(response.text)

        if response.status_code == 200:
            s.create("jwt", data["access_token"])
            flash('Login successful')

        if response.status_code == 422:
             flash('Invalid email format')

        if response.status_code == 401:
            flash('Wrong email or password')

        return redirect("/login/")


class Stats(MethodView):
    def get(self):

        form = StatsForm()
        return render_template("insert.html", form=form)

    def post(self):
        access_token = s.fetch("jwt")
        if access_token is None:
            return redirect(url_for("login"))
        data = {
            "month": request.form["month"],
        }

        if data["month"] == "":
            flash('Для этого месяца нет данных')
            return redirect(url_for("stats"))

        min = stats_sample_min(access_token, data)
        avg = stats_sample_avg(access_token, data)
        max = stats_sample_max(access_token, data)
        payload = [['Статистика за ', data['month'], ' месяц:'],['min',min.text], ['avg',avg.text], ['max',max.text]]

        if min.status_code == 200 and avg.status_code == 200 and max.status_code == 200:
            print("i am here")
            return render_template("stats.html", context=payload)
        if min.status_code == 403 or avg.status_code == 403 or max.status_code == 403:
            flash('Требуется авторизация')
            return redirect(url_for("stats"))
        if min.status_code == 500 or avg.status_code == 500 or max.status_code == 500: # todo По не существующим месяцам api возвращает 500
            flash('Для этого месяца нет данных')
            return redirect(url_for("stats"))


class Insert(MethodView):
    def get(self):

        form = InsertForm()
        return render_template("insert.html", form=form)

    def post(self):
        access_token = s.fetch("jwt")
        if access_token is None:
            return redirect(url_for("login"))

        data = {
            "title": request.form["title"],
            "month": request.form["month"],
            "Fe": request.form["Fe"],
            "Ca": request.form["Ca"],
            "S": request.form["S"],
            "Si": request.form["Si"],
            "Al": request.form["Al"],
        }

        response = insert_sample(access_token, data)
        data = json.loads(response.text)
        print(response.status_code)

        if response.status_code == 200:
            flash('Данные добавлены!')
            return redirect(url_for("insert"))


        if response.status_code == 403:
            flash('Требуется авторизация')
            return redirect(url_for("login"))

        if response.status_code == 422:
            flash('Перепроверьте данные и повторите!')
            return redirect(url_for("insert")) # todo Распарсить ответ и вытащить на что именно ругается бэк

        return render_template("insert.html")


class Index(MethodView):
    def get(self):
        return render_template("index.html")

app.add_url_rule("/login/", view_func=Login.as_view("login"))
app.add_url_rule("/stats/", view_func=Stats.as_view("stats"))
app.add_url_rule("/insert/", view_func=Insert.as_view("insert"))
app.add_url_rule("/", view_func=Index.as_view("index"))


