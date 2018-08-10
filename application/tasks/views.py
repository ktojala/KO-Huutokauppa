from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Tuoteryhma
from application.tasks.forms import TuoteryhmaForm
from application.tasks.models import Myytava
from application.tasks.forms import MyytavaForm

@app.route("/tasks/1/", methods=["GET"])
def tuoteryhmat_index():
    return render_template("tasks/tuoteryhma_list.html", tuoteryhmat = Tuoteryhma.query.all())


@app.route("/tasks/2/", methods=["GET"])
def myytavat_index():
    return render_template("tasks/myytava_list.html", myytavat = Myytava.query.all())


@app.route("/tasks/3/")
@login_required
def tuoteryhma_form():
    return render_template("tasks/uusituoteryhma.html", form = TuoteryhmaForm())


@app.route("/tasks/4/")
@login_required
def myytava_form():
    return render_template("tasks/uusimyytava.html", form = MyytavaForm())


@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tuoteryhma_set_done(task_id):

    t = Tuoteryhma.query.get(task_id)
    t.done = True

# seuraava rivi ei vielä tarpeen
#    t1 = Tuoteryhma(request.form.get("name"))

    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tasks/<task_id>/", methods=["GET"])
def tuoteryhma_delete(task_id):

    Tuoteryhma.query.filter_by(id=task_id).delete()
    db.session().commit()

    return redirect(url_for("tuoteryhmat_index"))



@app.route("/tasks/<myytava_id>/1/", methods=["POST"])
@login_required
def myytava_set_done(myytava_id):

    t = Myytava.query.get(myytava_id)
    t.done = True

# seuraava rivi ei vielä tarpeen
#    t1 = Myytava(request.form.get("name"))

    db.session().commit()
  
    return redirect(url_for("myytavat_index"))


@app.route("/tasks/<myytava_id>/2/", methods=["GET"])
def myytava_delete(myytava_id):

    Myytava.query.filter_by(id=myytava_id).delete()
    db.session().commit()

    return redirect(url_for("myytavat_index"))



@app.route("/tasks/5/", methods=["POST"])
@login_required
def tuoteryhma_create():
    form = TuoteryhmaForm(request.form)

    if not form.validate():
        return render_template("tasks/uusituoteryhma.html", form = form)  

    t = Tuoteryhma(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tasks/6/", methods=["POST"])
@login_required
def myytava_create():
    form = MyytavaForm(request.form)

    if not form.validate():
        return render_template("tasks/uusimyytava.html", form = form)  

    t = Myytava(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))
