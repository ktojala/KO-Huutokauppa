from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Tuoteryhma
from application.tasks.forms import TuoteryhmaForm
from application.myytava.models import Myytava
from application.myytava.forms import MyytavaForm
from application.auth.models import Asiakas
from application.auth.forms import RegForm
# from application.tasks.forms import UusialoitushintaForm


@app.route("/tasks/2/", methods=["GET"])
def myytavat_index():
    return render_template("myytava/myytava_list.html", myytavat = Myytava.query.all())


@app.route("/tasks/4/")
@login_required
def myytava_form():
    return render_template("myytava/uusimyytava.html", form = MyytavaForm())


@app.route("/myytava/<myytava_id>/7/", methods=["POST"])
@login_required
def myytava_nosta_aloitushintaa(myytava_id):

    t = Myytava.query.get(myytava_id)
    t.aloitushinta+=1
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))



@app.route("/tasks/<myytava_id>/8/", methods=["GET"])
@login_required
def myytava_delete(myytava_id):

    Myytava.query.filter_by(id=myytava_id).delete()
    db.session().commit()

    return redirect(url_for("myytavat_index"))




@app.route("/tasks/10/", methods=["POST"])
@login_required
def myytava_create():
    form = MyytavaForm(request.form)

    if not form.validate():
        return render_template("myytava/uusimyytava.html", form = form)  

    t = Myytava(form.name.data)
    t.aloitushinta = form.aloitushinta.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))



