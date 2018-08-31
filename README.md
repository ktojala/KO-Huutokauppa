# KO-Huutokauppa

Tietokantasovellusharjoitus - tehtävän kuvaus (kuvaukseen voi tulla vielä muutoksia)

Huutokauppakamari KO-Huutokauppa halusi huutokauppajärjestelmän, jonka avulla se voi kaupata tuotteita verkossa.
Huutokauppakamari luokittelee myyntiin saamansa tuotteet tai tuotetiedot ja laatii niistä myyntiesitteen. Esitteessä on mm. tuotteen kuvaus ja hinta. Siihen voi sisältyä tuotteen kuva. Esitteessä kerrotaan myös kuinka paljon myyntiaikaa on jäljellä. Kun myytävän kohteen huutokauppa on avattu, asiakas saa näkyviinsä sen tuotetiedot ja tämänhetkisen korkeimman tarjouksen.
Kuka tahansa pääsee katsomaan tarjolla olevia myytäviä tuotteita, mutta tarjouksen tekeminen edellyttää rekisteröitymistä asiakkaaksi ja asiakkaana kirjautumista.  Rekisteröitymisen yhteydessä asiakas antaa henkilötietonsa, mukaanlukien sähköpostiosoitteen. 

Meklarit valvovat kauppaa ja ottavat aika ajoin seurantalistoja. Erityisen kiinnostuksen kohteena ovat kohteet joiden myyntiaika on päättynyt ja ne, joista ei ole tehty tarjouksia vielä. Ennen kaupan sulkemista meklari varmistaa tarjouksen sähköpostitse, mikä ei ole osa toteutettavaa järjestelmää tässä vaiheessa. Jos huutokaupan päättyessä korkein tarjous ei toteudu, myydään tavara seuraavaksi korkeimmalle tarjoajalle, jne. Meklari sulkee kaupan kun asiakas on maksanut laskun (järjestelmän ulkopuolella). Toteutumattomat tarjukset poisteaan. Järjestelmän seuraavassa kehitysvaiheessa toteutunut kauppa voidaan tallettaa omaan tauluunsa.

Vain huutokauppakamarin edustaja (admin) voi lisätä huutokaupan sivuille tuotteita ja tuoteryhmiä sekä tarvittaessa poistaa näitä.

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

## Viime hetken SUUNNITELMA työn viimeistelyyn

- Näytä korkeimmat tarjoukset tarjousajaltaan umpeutuneista
- Poista korkein tarjous (jos se osoittautui epäkelvoksi)

## Kirjautuminen asiakkaana:
- Käyttäjätunnus: testi
- Salasana:       kesti
## Kirjautuminen administraattorina:
- Käyttäjätunnus: admin
- Salasana:       kadmin

Voit rekisteröityä myös omana erillisenä testikäyttäjänä, jolla on asiakkaan oikeudet. Älä käytä tunnuksia tai salasanoja, jotka ovat oikeassa käytössä muualla.

## Linkit ja dokumentaatio:

<a href="https://tsoha-ko-huutokauppa.herokuapp.com">Kokeile sovellusta Herokussa</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttotapaus.md">Kayttötapauskaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/tietokantakaavio.md">Tietokantakaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/tietokantakaavio.md">SQL-kyselyt</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/asennusohje.md">Asennusohje</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttoohje.md">Käyttöohje</a>

