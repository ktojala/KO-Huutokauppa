from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

from application.myytava.models import Myytava
from application.tarjous.forms import TarjousForm
from application.auth.models import Asiakas


@app.route("/tarjous/<myytava_id>/", methods=["POST"])
@login_required
def tarjous_create(myytava_id):
    form = TarjousForm(request.form)
    t = Myytava.query.get(myytava_id)
    if not form.validate():
        return render_template("tarjous/uusitarjous.html", form = form, myytava=t)

    if form.validate():
        if form.tarjoussumma.data > t.tarjoushinta:
            t.tarjoushinta = form.tarjoussumma.data
    db.session().commit()

    return render_template("myytava/myytavan_tiedot.html", myytava = t)
