
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

SELECT rooli.name FROM rooli JOIN asiakasrooli ON rooli.id= asiakasrooli.rooli_id JOIN account ON asiakasrooli.account_id = account.id WHERE account_id = current_user.id;

2. Etsitään roolit käyttäjäĺle, jonka id on account_id, alla olevassa lauseessa "JOKIN_id"

stmt=("SELECT DISTINCT Rooli.name FROM Rooli JOIN AsiakasRooli ON"
                    " Rooli.id = AsiakasRooli.rooli_id WHERE AsiakasRooli.account_id = "
                    "account_id").params(account_id=account_id)

SELECT rooli.name FROM rooli JOIN asiakasrooli ON rooli.id= asiakasrooli.rooli_id JOIN account ON asiakasrooli.account_id = account.id WHERE account_id = JOKIN_id;

3. Etsitään Asiakas jonka käyttäjätunnus ja salasana ovat kuten lomakkeessa. Ensimmäinen löydetty riittää.

Asiakas.query.filter_by(username=form.username.data, password=form.password.data).first()

SELECT * from account WHERE account.username = form.username.data AND account.password=form.password.data LIMIT 1;

4. Luodaan uusia asiakas lomakkeen tiedoista

asiakas = Asiakas(form.name.data,form.email.data, form.username.data, form.password.data)

INSERT INTO account (name,email,username,password) VALUES (form.name.data,form.email.data, form.username.data, form.password.data)

## tuoteryhmä-kansiot:






# SQL-poistot




