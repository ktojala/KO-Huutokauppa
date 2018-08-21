# KO-Huutokauppa

Tietokantasovellusharjoitus - tehtävän kuvaus (kuvaukseen voi tulla vielä muutoksia)

Huutokauppakamari haluaa rakentaa huutokauppajärjestelmän, jonka avulla se voi kaupata tuotteita verkossa.
Huutokauppakamari luokittelee myyntiin saamansa tuotteet ja laatii niistä myyntiesitteen. Esitteessä on mm. tuotteen kuvaus ja vähimmäishinta. Siihen voi sisältyä tuotteen kuva. Esitteessä kerrotaan myös milloin kauppa alkaa ja päättyy. Kun huutokauppa on avattu, asiakas saa näkyviinsä myös tämänhetkisen korkeimman tarjouksen.
Kuka tahansa pääsee katsomaan tarjolla olevia tuotteita, mutta tarjouksen tekeminen edellyttää kirjautumista asiakkaaksi. Tarjouksen yhteydessä asiakas antaa henkilötietonsa. 

Meklarit valvovat kauppaa ottamalla aika ajoin seurantalistoja, joista pitäisi käydä esiin tuotteista tehtyjen tarjousten määrä, nykyinen korkein tarjous ja erityisesti huomattavat poikkeamat tarjoushinnassa. Tällaisissa tapauksissa meklari varmistaa tarjouksen aitouden. Näin tehdään myös aina ennen kaupan sulkemista. Varmistus voidaan hoitaa sähköpostitse. Jos huutokaupan päättyessä viimeisin tarjous ei ollut aito myydään tavara edelliselle tarjoajalle, jne. Meklari sulkee kaupan kun asiakas on maksanut laskun (järjestelmän ulkopuolella).

Vain huutokauppakamarin edustaja voi lisätä huutokaupan sivuille tuotteita ja tuoteryhmiä sekä tarvittaessa muokata ja poistaa näitä, samoin kuin verkossa näkyviä toimintaohjeita.

Toimintoja:
- Tuotetietojen (=myytava) syöttö ja muokkaus
- Myytävän poistaminen ja tarvittaessa siirto toteutuneiden kauppojen luetteloon
- Tuoteluokkien muokkaus, lisäys ja poisto
- Myytavan tuotteen tietojen katselu
- Asiakkaaksi rekisteröityminen, kirjautuminen, oman profiilin muokkaaminen ja rekisteristä irtisanoutuminen
- Tarjouksen tekeminen
- Meklarin seurantalistan tuottaminen ja epäkelvon tarjouksen poistaminen
- Lasku asiakkaalle
- Kaupan sulkeminen tuotteen osalta
- Kamarin edustaja voi tuottaa tietokannasta myyntitilaston, esimerkiksi ostomäärät ostajien paikkakunnan mukaan

HUOM: 
- Tarjousten teko toimii nyt uudesta tarjouksentekonäkymästä.
- MONIMUTKAISTA YHTEENVETOKYSELYÄ ei ihan sellaisenaan ole, mutta jossakin mielessä vastaavaa toiminnallisuutta löytyy, miten Tuoteryhmän listauksesta voidaan klikata "Lisää myytävä", jolloin luodaan uusi myytävä tuote jolloin myytava-tauluun viedään automaattisesti se tuoteryhmä jonka kohdalla klikkaus tapahtui.
Myytävän tuotteen näkymässä näkyy tuoteryhmän nimi, joka haetaan eri taulusta.

## Kirjautuminen:
- Käyttäjätunnus: testi
- Salasana:       kesti

## Linkit:

<a href="https://tsoha-ko-huutokauppa.herokuapp.com">Sovellus Herokussa</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttotapaus.md">Kayttötapauskaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kasite.md">Käsitekaavio</a>

Testilinkki muuhun dokumentaatioon: <a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/eka.md">Eka doc</a>

