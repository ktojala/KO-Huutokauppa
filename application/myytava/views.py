from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

from application.tuoteryhma.models import Tuoteryhma

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


@app.route("/myytava/<myytava_id>/delete/", methods=["GET"])
@login_required
def myytava_delete(myytava_id):

    Myytava.query.filter_by(id=myytava_id).delete()
    db.session().commit()

    return redirect(url_for("myytavat_index"))


@app.route("/myytava/<tuoteryhma_id>/create/", methods=["POST"])
@login_required
def myytava_create(tuoteryhma_id):
    form = MyytavaForm(request.form)
    tuoteryhma = Tuoteryhma.query.get(tuoteryhma_id)

    if not form.validate():
        return render_template("myytava/uusimyytava.html", form = form, tuoteryhma = tuoteryhma)  

    t = Myytava(form.name.data,1,tuoteryhma.name)
    t.tuotetietoa = form.tuotetietoa.data
    t.aloitushinta = form.aloitushinta.data
    t.tarjoushinta = form.aloitushinta.data
    t.account_id = current_user.id
    t.tuoteryhma_id = tuoteryhma_id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))



@app.route("/myytava/<myytava_id>/", methods=["POST"])
@login_required
def myytava_nosta_tarjoushintaa(myytava_id):

    t = Myytava.query.get(myytava_id)
    t.tarjoushinta+=1
    db.session().commit()

    return render_template("myytava/myytavan_tiedot.html", myytava = t)


@app.route("/myytava/<myytava_id>/tietoa/", methods=["POST"])

def myytava_tietoa(myytava_id):

    myytava = Myytava.query.get(myytava_id)

#    return redirect(url_for("myytavat_index"), myytava = myytava)
    return render_template("myytava/myytavan_tiedot.html", myytava = myytava)




@app.route("/myytava/yhteenveto/")
@login_required
def myytava_yhteenveto():
    
#    return Myytava.loyda_kaikki()
    return redirect(url_for("myytavat_index"))

#    return render_template("myytava/myytava_yhteenveto.html")

@app.route("/myytava/<myytava_id>/laske/")
@login_required
def tuoteryhma_laske(myytava_id):
    
    return myytava_id


#   <li><a href="{{ url_for('myytava_form') }}">Lisää uusi myytävä tuote</a></li>

# @app.route("/tuoteryhma/<tuoteryhma_id>/", methods=["POST"])
# @login_required
# def tuoteryhma_open(tuoteryhma_id):
#
#    t = Tuoteryhma.query.get(tuoteryhma_id)
#    t.done = True

# seuraava rivi ei vielä tarpeen
#    t1 = Tuoteryhma(request.form.get("name"))

#    db.session().commit()
  
#    return redirect(url_for("tuoteryhmat_index"))
#    return redirect(url_for("myytava_create"))
