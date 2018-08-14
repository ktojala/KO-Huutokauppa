from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tuoteryhma.models import Tuoteryhma
from application.tuoteryhma.forms import TuoteryhmaForm

from application.auth.models import Asiakas
from application.auth.forms import RegForm
# from application.tasks.forms import UusialoitushintaForm

@app.route("/tuoteryhma/1/", methods=["GET"])
def tuoteryhmat_index():
    return render_template("tuoteryhma/tuoteryhma_list.html", tuoteryhmat = Tuoteryhma.query.all())


@app.route("/tuoteryhma/3/")
@login_required
def tuoteryhma_form():
    return render_template("tuoteryhma/uusituoteryhma.html", form = TuoteryhmaForm())


@app.route("/tuoteryhma/<task_id>/5/", methods=["POST"])
@login_required
def tuoteryhma_set_done(task_id):

    t = Tuoteryhma.query.get(task_id)
    t.done = True

# seuraava rivi ei vielä tarpeen
#    t1 = Tuoteryhma(request.form.get("name"))

    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tuoteryhma/<task_id>/6/", methods=["GET"])
@login_required
def tuoteryhma_delete(task_id):

    Tuoteryhma.query.filter_by(id=task_id).delete()
    db.session().commit()

    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tuoteryhma/9/", methods=["POST"])
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









