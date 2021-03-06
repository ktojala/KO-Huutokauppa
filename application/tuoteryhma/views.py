from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

# Uusi lisä
from application.myytava.models import Myytava

from application.tuoteryhma.models import Tuoteryhma
from application.tuoteryhma.forms import TuoteryhmaForm

from application.auth.models import Asiakas
from application.auth.forms import RegForm


@app.route("/tuoteryhma/", methods=["GET"])
def tuoteryhmat_index():
    return render_template("tuoteryhma/tuoteryhma_list.html", tuoteryhmat = Tuoteryhma.query.all())


@app.route("/tuoteryhma/uusi/")
@login_required()
def tuoteryhma_form():
    return render_template("tuoteryhma/uusituoteryhma.html", form = TuoteryhmaForm())

    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tuoteryhma/<tuoteryhma_id>/delete/", methods=["GET"])
@login_required()
def tuoteryhma_poista(tuoteryhma_id):

    tr = Tuoteryhma.query.filter_by(id=tuoteryhma_id).first()
    a = Myytava.query.filter_by(tuoteryhma_id=tuoteryhma_id).count()
    if a>0:
        return render_template("tuoteryhma/tuoteryhma_error.html")

    else:
        Tuoteryhma.query.filter_by(id=tuoteryhma_id).delete()
        db.session().commit()

    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tuoteryhma/create/", methods=["POST"])
@login_required()
def tuoteryhma_luo():
    form = TuoteryhmaForm(request.form)

    if not form.validate():
        return render_template("tuoteryhma/uusituoteryhma.html", form = form)  

    t = Tuoteryhma(form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))





