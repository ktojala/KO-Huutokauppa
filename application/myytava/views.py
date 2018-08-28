from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

from application.tuoteryhma.models import Tuoteryhma
from application.myytava.models import Myytava
from application.myytava.forms import MyytavaForm
from application.auth.models import Asiakas
from application.auth.forms import RegForm
from application.tarjous.models import Tarjous

@app.route("/myytava/", methods=["GET"])
def myytavat_index():
    return render_template("myytava/myytava_list.html", myytavat = Myytava.query.all())


@app.route("/myytava/<tuoteryhma_id>/open/", methods=["POST"])
def tuoteryhma_avaa(tuoteryhma_id):
    return render_template("myytava/myytava_list.html", myytavat = Myytava.query.filter_by(tuoteryhma_id=tuoteryhma_id))


@app.route("/myytava/uusi/")
@login_required()
def myytava_form():
    return render_template("myytava/uusimyytava.html", form = MyytavaForm())


@app.route("/myytava/<myytava_id>/poista/", methods=["GET"])
@login_required()
def myytava_poista(myytava_id):

# Poistetaan ensin tarjoukset jotka tehty poistettavasta myytävästä

    Tarjous.myytavan_tarjoukset_poista(myytava_id)

    Myytava.query.filter_by(id=myytava_id).delete()
    db.session.commit()
    return render_template("myytava/myytava_umpeutuneet.html", tars= Myytava.query.filter(Myytava.tarjousaikaa==0))


@app.route("/myytava/<tuoteryhma_id>/luo/", methods=["POST"])
@login_required()
def myytava_luo(tuoteryhma_id):
    form = MyytavaForm(request.form)
    tuoteryhma = Tuoteryhma.query.get(tuoteryhma_id)

    if not form.validate():
        return render_template("myytava/uusimyytava.html", form = form, tuoteryhma = tuoteryhma)  

    t = Myytava(form.name.data,1,tuoteryhma.name)
    t.aloitushinta = form.aloitushinta.data
    t.tarjoushinta = form.aloitushinta.data
    t.tuotetietoa = form.tuotetietoa.data
    t.tarjousaikaa = form.tarjousaikaa.data
    t.account_id = current_user.id
    t.tuoteryhma_id = tuoteryhma_id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("myytavat_index"))


@app.route("/myytava/<myytava_id>/tietoa/", methods=["POST"])

def myytava_tietoa(myytava_id):

    myytava = Myytava.query.get(myytava_id)
    return render_template("myytava/myytavan_tiedot.html", myytava = myytava)


@app.route("/myytava/yhteenveto/")
@login_required()
def myytava_yhteenveto():

    return render_template("myytava/myytava_yhteenveto.html", tars= Myytava.query.filter(Myytava.aloitushinta==Myytava.tarjoushinta))


@app.route("/myytava/vahenna_paiva/")
@login_required()
def myytava_vahenna_paiva():
    myytavat = Myytava.query.all()
    for m in myytavat:
        if m.tarjousaikaa > 0:
            m.tarjousaikaa -= 1
    db.session().add(m)
    db.session().commit()    
    return redirect(url_for("myytavat_index"))


@app.route("/myytava/umpeutuneet_nayta/")
@login_required()
def myytava_umpeutuneet_nayta():

    return render_template("myytava/myytava_umpeutuneet.html", tars= Myytava.query.filter(Myytava.tarjousaikaa==0))





