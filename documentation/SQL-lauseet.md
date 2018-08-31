
# SQL-versiot

Linux-ympäristössä käytössä on SQLite ja Herokussa PostgreSQL

# CREATE TABLE -lauseet

HUOM: Sovelluksen luokkaa Asiakas vastaava taulu on 'account'

CREATE TABLE tuoteryhma (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE myytava (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	aloitushinta INTEGER NOT NULL, 
	tarjoushinta INTEGER NOT NULL, 
	tuotetietoa VARCHAR(144) NOT NULL, 
	tarjousaikaa INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	tuoteryhma_id INTEGER NOT NULL, 
	tuoteryhmatxt VARCHAR(40) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(tuoteryhma_id) REFERENCES tuoteryhma (id)
);
CREATE TABLE tarjous (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	myytava_id INTEGER NOT NULL, 
	tarjoussumma INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(myytava_id) REFERENCES myytava (id)

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	email VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE rooli (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE asiakasrooli (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	rooli_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(rooli_id) REFERENCES rooli (id)
);

# SQL-kyselyt eri kansioissa

Useimmat kyselyt sovelluksessa on toteutettu SQLAlchemyn avulla.


## auth-kansiot:

1. Etsitään nykyisen käyttäjän "current_user" roolit

Rooli.query.join(Rooli.user_roles).filter_by(account_id=self.id).all()

SELECT rooli.name FROM rooli JOIN asiakasrooli ON rooli.id= asiakasrooli.rooli_id JOIN account ON asiakasrooli.account_id = account.id WHERE account.id = current_user.id;


2. Etsitään roolit käyttäjäĺle, jonka id on account_id, alla olevassa lauseessa "JOKIN_id"

stmt=("SELECT DISTINCT Rooli.name FROM Rooli JOIN AsiakasRooli ON"
                    " Rooli.id = AsiakasRooli.rooli_id WHERE AsiakasRooli.account_id = "
                    "account_id").params(account_id=account_id)

SELECT rooli.name FROM rooli JOIN asiakasrooli ON rooli.id= asiakasrooli.rooli_id JOIN account ON asiakasrooli.account_id = account.id WHERE account_id = JOKIN_id;


3. Etsitään Asiakas jonka käyttäjätunnus ja salasana ovat kuten lomakkeessa. Ensimmäinen löydetty riittää.

Asiakas.query.filter_by(username=form.username.data, password=form.password.data).first()

SELECT * from account WHERE account.username = form.username.data AND account.password=form.password.data LIMIT 1;


4. Luodaan uusi asiakas lomakkeen tiedoista

asiakas = Asiakas(form.name.data,form.email.data, form.username.data, form.password.data)

INSERT INTO account (name,email,username,password) VALUES (form.name.data,form.email.data, form.username.data, form.password.data)


## tuoteryhmä-kansiot:

5. Etsi kaikki tuoteryhmät

Tuoteryhma.query.all()

SELECT * FROM tuoteryhma;


6. Pyydetään tuoteryhmä tuoteryhma_id:n perusteella

tr = Tuoteryhma.query.filter_by(id=tuoteryhma_id).first()

SELECT * FROM tuoteryhma WHERE tuoteryhma.id = tuoteryhma_id LIMIT 1;


7. Selvitetään montako sellaista myytävää jolla tuoteryhmä on tuoteryhma_id

a = Myytava.query.filter_by(tuoteryhma_id=tuoteryhma_id).count()

SELECT COUNT(*) from myytava WHERE tuoteryhma_id = tuoteryhma_id LIMIT 1;


8. Poista tuoteryhmä jonka id on tuoteryhma_id

Tuoteryhma.query.filter_by(id=tuoteryhma_id).delete()

DELETE FROM tuoteryhma WHERE id = tuoteryhma_id;

9. Selvitetään montako sellaista myytävää jolla tuoteryhmä on tuoteryhma_id

db.session.query(Myytava).filter_by(tuoteryhma_id=tr.id).count()

SELECT COUNT(*) from myytava WHERE tuoteryhma_id = tuoteryhma_id LIMIT 1;


10. Luodaan uusi tuoteryhmä

t = Tuoteryhma(form.name.data)

INSERT INTO tuoteryhma (name) VALUES (form.name.data);

## myytava-kansiot:

11. Etsi kaikki myytävät tuotteet

myytavat = Myytava.query.all())

SELECT * FROM myytava;


12. Etsi kaikki myytävät tuotteet joiden tuoteryhma_id on pyydetty tuoteryhma_id

myytavat = Myytava.query.filter_by(tuoteryhma_id=tuoteryhma_id))

SELECT * FROM myytava WHERE tuoteryhma_id = tuoteryhma_id;


13. Poista myytava jonka id on myytava_id

Myytava.query.filter_by(id=myytava_id).delete()

DELETE FROM myytava WHERE id = myytava_id;


1. Luodaan uusi myytava

t = Myytava(form.name.data,1,tuoteryhma.name)

INSERT INTO myytava (name,aloitushinta,password) VALUES (form.name.data,1,tuoteryhma.name);


1. Etsi myytävät joista ei ole tehty tarjouksia

tars= Myytava.query.filter(Myytava.aloitushinta==Myytava.tarjoushinta)

SELECT * FROM myytava WHERE aloitushinta = tarjoushinta;


1. Etsi myytävät joiden tarjousaika on umpeutunut

tars= Myytava.query.filter(Myytava.tarjousaikaa==0)

SELECT * FROM myytava WHERE tarjousaikaa ==0;


1. Pyydetään tuoteryhmä tuoteryhma_id:n perusteella

tuoteryhma = Tuoteryhma.query.get(tuoteryhma_id)

SELECT * FROM tuoteryhma WHERE id = tuoteryhma_id;


1. Pyydetään myytava myytava_id:n perusteella

    myytava = Myytava.query.get(myytava_id)

SELECT * FROM myytava WHERE id = myytava_id;


1. Etsi kaikki myytavat

myytavat = Myytava.query.all()

SELECT * FROM myytava;


1. Etsi myytavan nimi tuotteelle jonka id on syote.id

SELECT myytava.name FROM myytava WHERE myytava.id=syote.id;



1. Etsi myytävän tuoteryhmä kun myytava.id on syote.id

SELECT tuoteryhma_id FROM myytava WHERE myytava.id=syote.id;


## tarjous-kansiot:

1. Etsi nimi myytävälle, jonka id on m-id

stmt = text("SELECT myytava.name FROM myytava WHERE myytava.id = :idi").params(idi=m_id)

SELECT myytava.name FROM myytava WHERE myytava.id=m_id;


1. Poista tarjoukset myytavaltä, jonka id on myytava-id

stmt = text("DELETE FROM tarjous WHERE tarjous.myytava_id = :idi").params(idi=myytava_id)

DELETE FROM tarjous WHERE tarjous.myytava_id = myytava_id

1. Etsi kaikki tarjoukset

tarjoukset = Tarjous.query.all())

SELECT * FROM tarjous;


1. Etsi nykyisen käyttäjän kaikki tarjoukset

t = Tarjous.query.filter_by(account_id=current_user.id)

SELECT * FROM tarjous JOIN account ON tarjous.account_id = account.id WHERE account.id = current_user.id;


1. Luo uusi tarjous

tt = Tarjous(current_user.id,t.id,form.tarjoussumma.data)
INSERT INTO account (account_id,myytava_id, tarjoussumma) VALUES (current_user.id, t.id, form.tarjoussumma.data);


## Application

1. Etsi Asiakas jonka id on käyttäjän id

Asiakas.query.get(user_id)

SELECT * FROM account WHERE id = user_id;


1. Etsi kaikki asiakkaat

asiat = Asiakas.query.all()

SELECT * FROM account;


1. Luo rooli "ADMIN"

admin_rooli = Rooli("ADMIN")

INSERT INTO rooli (name) VALUES ("ADMIN");

1. Luo asiakasrooli ja aseta sille arvot

ar1=AsiakasRooli()
ar1.account_id = admin.id
ar1.rooli_id = admin_rooli.id
db.session.add_all((ar1))
db.session.commit()

INSERT INTO asiakasrooli (account_id,rooli_id) VALUES (admin.id, admin_rooli.id);

Edellinen on esimerkki tilanteesta, jossa taulun alkiota täydennetään yksittäisillä arvoilla
ja vastaavia on sovelluksessa paljon. Ei niitä kannata kaikkia tänne kirjoittaa.






