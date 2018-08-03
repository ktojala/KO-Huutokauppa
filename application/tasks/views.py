
from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.tasks.models import Tuoteryhma


@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks", methods=["GET"])
def tuoteryhmat_index():
    return render_template("tasks/tuoteryhmat_list.html", tuoteryhmat = Tuoteryhma.query.all())


@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/tasks/new/")
def tuoteryhmat_form():
    return render_template("tasks/newtuoteryhma.html")


@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("tasks_index"))


@app.route("/tasks/<tuoteryhma_id>/", methods=["POST"])
def tuoteryhma_muokkaa(task_id):

    t = Tuoteryhma.query.get(tuoteryhma_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))


@app.route("/tasks/", methods=["POST"])
def tasks_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
def tuoteryhma_create():
    t = Tuoteryhma(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tuoteryhmat_index"))






