from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.myytava.models import Myytava
from application.myytava.forms import MyytavaForm
from application.auth.models import Asiakas
from application.auth.forms import RegForm

# from application.tasks.forms import UusialoitushintaForm


@app.route("/myytava/", methods=["GET"])
def myytavat_index():
    return render_template("myytava/myytava_list.html", myytavat = Myytava.query.all())

# tarkista myöhemmin => get lisätietoja toiminto

@app.route("/myytava/uusi/")
@login_required
def myytava_form():
    return render_template("myytava/uusimyytava.html", form = MyytavaForm())


@app.route("/myytava/<myytava_id>/", methods=["POST"])
@login_required
def myytava_nosta_aloitushintaa(myytava_id):

    t = Myytava.query.get(myytava_id)
    t.aloitushinta+=1
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))



@app.route("/myytava/<myytava_id>/delete/", methods=["GET"])
@login_required
def myytava_delete(myytava_id):

    Myytava.query.filter_by(id=myytava_id).delete()
    db.session().commit()

    return redirect(url_for("myytavat_index"))




@app.route("/myytava/create/", methods=["POST"])
@login_required
def myytava_create():
    form = MyytavaForm(request.form)

    if not form.validate():
        return render_template("myytava/uusimyytava.html", form = form)  

    t = Myytava(form.name.data,2)
    t.aloitushinta = form.aloitushinta.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))



