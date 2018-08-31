# CREATE TABLE lauseet

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

# SQL kyselyt

Useimmat kyselyt sovellukseessa on toteutettu SQLAlchemyn avulla.



# SQLpoistot




