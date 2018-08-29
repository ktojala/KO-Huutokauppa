from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

from application.myytava.models import Myytava
from application.tarjous.models import Tarjous
from application.tarjous.forms import TarjousForm
from application.auth.models import Asiakas

@app.route("/tarjous/", methods=["GET"])
@login_required()
def tarjous_index():
    return render_template("tarjous/tarjous_list.html", tarjoukset = Tarjous.query.all())


@app.route("/tarjous/omat", methods=["GET"])
@login_required()
def tarjous_index_omat():

    t = Tarjous.query.filter_by(account_id=current_user.id)
    return render_template("tarjous/tarjous_list_omat.html", tarjoukset = t)


@app.route("/tarjous/<myytava_id>/", methods=["POST"])
@login_required()
def tarjous_luo(myytava_id):
    form = TarjousForm(request.form)
    t = Myytava.query.get(myytava_id)
    if not form.validate():
        return render_template("tarjous/uusitarjous.html", form = form, myytava=t)

    if form.validate():
        if form.tarjoussumma.data != 0:
            if form.tarjoussumma.data > t.tarjoushinta and form.tarjoussumma.data <= 3*t.tarjoushinta:
                t.tarjoushinta = form.tarjoussumma.data
                db.session().commit()
                tt = Tarjous(current_user.id,t.id,form.tarjoussumma.data)
                db.session().add(tt)
                db.session().commit()
                return render_template("tarjous/tarjousvahvistus.html", myytava = t)
            elif form.tarjoussumma.data > 3*t.tarjoushinta:
                return render_template("tarjous/tarjous_error2.html", myytava = t)
            else:
                return render_template("tarjous/tarjous_error1.html", myytava = t)

    return render_template("myytava/myytavan_tiedot.html", myytava = t)



