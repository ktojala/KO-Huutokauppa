from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

# Uusi lisä
from application.myytava.models import Myytava

from application.tuoteryhma.models import Tuoteryhma
from application.tuoteryhma.forms import TuoteryhmaForm

from application.auth.models import Asiakas
from application.auth.forms import RegForm

# from application.tasks.forms import UusialoitushintaForm

@app.route("/tuoteryhma/", methods=["GET"])
def tuoteryhmat_index():
    return render_template("tuoteryhma/tuoteryhma_list.html", tuoteryhmat = Tuoteryhma.query.all())


@app.route("/tuoteryhma/uusi/")
@login_required
def tuoteryhma_form():
    return render_template("tuoteryhma/uusituoteryhma.html", form = TuoteryhmaForm())


@app.route("/tuoteryhma/<tuoteryhma_id>/", methods=["POST"])
@login_required
def tuoteryhma_open(tuoteryhma_id):

    t = Tuoteryhma.query.get(tuoteryhma_id)
    t.done = True

# seuraava rivi ei vielä tarpeen
#    t1 = Tuoteryhma(request.form.get("name"))

    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))
#    return redirect(url_for("myytava_create"))


@app.route("/tuoteryhma/<tuoteryhma_id>/delete/", methods=["GET"])
@login_required
def tuoteryhma_delete(tuoteryhma_id):

    Tuoteryhma.query.filter_by(id=tuoteryhma_id).delete()
    db.session().commit()

    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tuoteryhma/create/", methods=["POST"])
@login_required
def tuoteryhma_create():
    form = TuoteryhmaForm(request.form)

    if not form.validate():
        return render_template("tuoteryhma/uusituoteryhma.html", form = form)  

    t = Tuoteryhma(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))






