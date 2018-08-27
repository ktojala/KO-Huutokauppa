# KO-Huutokauppa

Tietokantasovellusharjoitus - tehtävän kuvaus (kuvaukseen voi tulla vielä muutoksia)

Huutokauppakamari haluaa rakentaa huutokauppajärjestelmän, jonka avulla se voi kaupata tuotteita verkossa.
Huutokauppakamari luokittelee myyntiin saamansa tuotteet ja laatii niistä myyntiesitteen. Esitteessä on mm. tuotteen kuvaus ja vähimmäishinta. Siihen voi sisältyä tuotteen kuva. Esitteessä kerrotaan myös milloin kauppa päättyy. Kun huutokauppa on avattu, asiakas saa näkyviinsä myös tämänhetkisen korkeimman tarjouksen.
Kuka tahansa pääsee katsomaan tarjolla olevia tuotteita, mutta tarjouksen tekeminen edellyttää kirjautumista asiakkaaksi. Tarjouksen yhteydessä asiakas antaa henkilötietonsa. 

Meklarit valvovat kauppaa ottamalla aika ajoin seurantalistoja, joista pitäisi käydä esiin korkein tarjous, onko tarjousta tehty lainkaan ja erityisesti huomattavat poikkeamat tarjoushinnassa. Tällaisissa tapauksissa meklari varmistaa tarjouksen aitouden (tämä automatisoidaan). Näin tehdään myös aina ennen kaupan sulkemista. Varmistus voidaan hoitaa sähköpostitse. Jos huutokaupan päättyessä viimeisin tarjous ei ollut aito myydään tavara edelliselle tarjoajalle, jne. Meklari sulkee kaupan kun asiakas on maksanut laskun (järjestelmän ulkopuolella).

Vain huutokauppakamarin edustaja voi lisätä huutokaupan sivuille tuotteita ja tuoteryhmiä sekä tarvittaessa muokata ja poistaa näitä, samoin kuin verkossa näkyviä toimintaohjeita.

Toimintoja:
- Tuotetietojen (=myytava) syöttö ja muokkaus
- Myytävän poistaminen ja tarvittaessa siirto toteutuneiden kauppojen luetteloon
- Tuoteluokkien muokkaus, lisäys ja poisto
- Myytavan tuotteen tietojen katselu
- Asiakkaaksi rekisteröityminen, kirjautuminen, oman profiilin muokkaaminen (ehkä)
- Tarjouksen tekeminen
- Meklarin seurantalistan tuottaminen ja epäkelvon tarjouksen poistaminen
- Lasku asiakkaalle
- Kaupan sulkeminen tuotteen osalta
- Kamarin edustaja voi tuottaa tietokannasta rajoitetusti myyntitilastoja

HUOM: 
- Tarjousten teko toimii nyt uudesta tarjouksentekonäkymästä.
- Toistaiseksi YHTEENVETOKYSELY löytyy /application/auth/model.py -tiedostosta.

## Viime hetken SUUNNITELMA työn viimeistelyyn
- Yläpalkkiin perusasiakkaan tehtävät
- Yläpalkissa asiakas näkee vain omat tarjouksensa
- Liian suurta tarjousta ei hyväksytä tarjouksentekovaiheessa
- Välitilaan adminin tehtävät
- Meklari ja huutokauppakamari käytännössä sama asia eli admin
- Myytävälle lisätään kenttä "tarjousaikaa jäljellä", yksikkönä päivä
- Adminille lisätoiminnallisuuksia:
- vähennä tarjousajasta 1 päivä, käsittele ja poista tarjousajaltaan umpeutuneet
- admininille ja asiakkaalle selkeämmin omat näkymät

## Kirjautuminen:
- Käyttäjätunnus: testi
- Salasana:       kesti
## Kirjautuminen administraattorina:
- Käyttäjätunnus: admin
- Salasana:       kadmin

## Linkit:

<a href="https://tsoha-ko-huutokauppa.herokuapp.com">Sovellus Herokussa</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttotapaus.md">Kayttötapauskaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kasite.md">Käsitekaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttoohje.md">Käyttöohje</a>

