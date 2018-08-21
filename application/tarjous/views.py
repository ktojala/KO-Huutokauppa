from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

from application.myytava.models import Myytava
from application.tarjous.models import Tarjous
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
        if form.tarjoussumma.data != 0:
            if form.tarjoussumma.data > t.tarjoushinta:
                t.tarjoushinta = form.tarjoussumma.data
                db.session().commit()
                tt = Tarjous(current_user.id,t.id,form.tarjoussumma.data)
                db.session().add(tt)
                db.session().commit()
                return render_template("tarjous/tarjousvahvistus.html", myytava = t)
            else:
                return render_template("tarjous/tarjous_error.html", myytava = t)

    return render_template("myytava/myytavan_tiedot.html", myytava = t)

#    def __init__(self, asiakasid,myytavaid,summa):
#        self.account_id = asiakasid
#        self.myytava_id = myytavaid
#        self.tarjoussumma = summa

