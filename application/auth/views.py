from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Asiakas
from application.auth.forms import LoginForm, RegForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    asiakas = Asiakas.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not asiakas:
        return render_template("auth/loginform.html", form = form, error = "Virheellinen käyttäjätunnus tai salasana")

    login_user(asiakas)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/reg", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/regform.html", form = RegForm())

    form = RegForm(request.form)
    if not form.validate():
        return render_template("auth/regform.html", form = form)

    asiakas = Asiakas(form.name.data,form.email.data, form.username.data, form.password.data)
    db.session.add(asiakas)
    db.session.commit()

    return redirect(url_for("index"))
