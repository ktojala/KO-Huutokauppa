# KO-Huutokauppa

Tietokantasovellusharjoitus - tehtävän kuvaus (kuvaukseen voi tulla vielä muutoksia)

Huutokauppakamari KO-Huutokauppa halusi huutokauppajärjestelmän, jonka avulla se voi kaupata tuotteita verkossa.
Huutokauppakamari luokittelee myyntiin saamansa tuotteet tai tuotetiedot ja laatii niistä myyntiesitteen. Esitteessä on mm. tuotteen kuvaus ja hinta. Siihen voi sisältyä tuotteen kuva. Esitteessä kerrotaan myös kuinka paljon myyntiaikaa on jäljellä. Kun myytävän kohteen huutokauppa on avattu, asiakas saa näkyviinsä sen tuotetiedot ja tämänhetkisen korkeimman tarjouksen.
Kuka tahansa pääsee katsomaan tarjolla olevia myytäviä tuotteita, mutta tarjouksen tekeminen edellyttää rekisteröitymistä asiakkaaksi ja asiakkaana kirjautumista.  Rekisteröitymisen yhteydessä asiakas antaa henkilötietonsa, mukaanlukien sähköpostiosoitteen. 

Meklarit valvovat kauppaa ja ottavat aika ajoin seurantalistoja. Erityisen kiinnostuksen kohteena ovat kohteet joiden myyntiaika on päättynyt ja ne, joista ei ole tehty tarjouksia vielä. Ennen kaupan sulkemista meklari varmistaa tarjouksen sähköpostitse, mikä ei ole osa toteutettavaa järjestelmää tässä vaiheessa. Jos huutokaupan päättyessä korkein tarjous ei toteudu, myydään tavara seuraavaksi korkeimmalle tarjoajalle, jne. Meklari sulkee kaupan kun asiakas on maksanut laskun (järjestelmän ulkopuolella). Toteutumattomat tarjukset poisteaan. Järjestelmän seuraavassa kehitysvaiheessa toteutunut kauppa voidaan tallettaa omaan tauluunsa.

Vain huutokauppakamarin edustaja (admin) voi lisätä huutokaupan sivuille tuotteita ja tuoteryhmiä sekä tarvittaessa poistaa näitä.

# User storyt

- Vierailija "ANY" voi selata tuoteryhmiä, myytäviä tuotteita ja tuotetietoja
- Vierailija voi rekisteröityä Asiakkaaksi
- Asiakas voi tehdä kaiken sen mitä vierailija
- Asiakas voi tarjouksia myytävistä tuotteista (kohteista)
- Asiakas näkee omat tarjouksensa
- Asiakas näkee onko oma tarjous mennyt läpi
- Admin voi tehdä kaiken sen mitä Asiakas
- Admin voi lisätä tuoteryhmiä
- Admin voi poistaa tuoteryhmän jossa ei ole tuotteita myytävänä
- Admin voi listata tuotteet jotka ovat myynnissä ja joista ei ole tehty tarjouksia vielä
- Admin voi vähentää kaikista tarjousajoista päivän. (Tämä pitää tehdä jokaisen päivän lopussa)
- Admin voi listata tuotteet joiden tarjousaik on umpeutunut (eli tarjousaikaa = 0)
- Admin voi poistaa sellaisen myytävän tuotteen jonka tarjousaika on umpeutunut. Samalla poistuvat kaikki kyseisestä kohteesta tehdyt tarjoukset.

- Näytä korkeimmat tarjoukset ja tarjojan sähköpostiosoite tarjousajaltaan umpeutuneista ei ehtinyt valmiiksi

## Kirjautuminen asiakkaana:
- Käyttäjätunnus: testi
- Salasana:       kesti
## Kirjautuminen administraattorina:
- Käyttäjätunnus: admin
- Salasana:       kadmin

Voit rekisteröityä myös omana erillisenä testikäyttäjänä, jolla on asiakkaan oikeudet. Älä käytä tunnuksia tai salasanoja, jotka ovat oikeassa käytössä muualla.

## Linkit ja dokumentaatio:

<a href="https://tsoha-ko-huutokauppa.herokuapp.com">Kokeile sovellusta Herokussa</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttotapaus.md">Alkuperäinen kayttötapauskaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/tietokantakaavio.md">Tietokantakaavio</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/SQL-lauseet.md">SQL-kyselyt</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/asennusohje.md">Asennusohje</a>

<a href="https://github.com/ktojala/KO-Huutokauppa/blob/master/documentation/kayttoohje.md">Käyttöohje</a>

