from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Tuoteryhma
from application.tasks.forms import TuoteryhmaForm
from application.tasks.models import Myytava
from application.tasks.forms import MyytavaForm

@app.route("/tasks/", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Tuoteryhma.query.all())


@app.route("/tasks/", methods=["GET"])
def myytavat_index():
    return render_template("tasks/myytava_list.html", myytavat = Myytava.query.all())


@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TuoteryhmaForm())


@app.route("/tasks/new/")
@login_required
def myytavat_form():
    return render_template("tasks/uusimyytava.html", form = MyytavaForm())


@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Tuoteryhma.query.get(task_id)
    t.done = True

# seuraava rivi ei vielä tarpeen
#    t1 = Tuoteryhma(request.form.get("name"))

    db.session().commit()
  
    return redirect(url_for("tasks_index"))


@app.route("/tasks/<task_id>/", methods=["GET"])
def tasks_delete(task_id):

    Tuoteryhma.query.filter_by(id=task_id).delete()
    db.session().commit()

    return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TuoteryhmaForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)  

    t = Tuoteryhma(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
@login_required
def lisaa_myytava():
    form = MyytavaForm(request.form)

    if not form.validate():
        return render_template("tasks/uusimyytava.html", form = form)  

    t = Myytava(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))
