# KO-Huutokauppa

Sovellus on pääosin rakennettu siten, että valikot kertovat käyttäjälle sen mitä hän voi tehdä.
Sovellus on kenen tahansa kokeiltavissa Heroku-palvelussa: https://tsoha-ko-huutokauppa.herokuapp.com

Sovelluksessa on kolmentasoisia käyttäjiä eli rooleja: ANY, ASIAKAS ja ADMIN.
Voidaan ajatella, että kuka tahansa uusi vierailija joka avaa sovelluksen, toimii roolissa "ANY".

## Käyttöohje - kuka tahansa - ANY

- Kuka tahansa voi selata tarjolla olevia tuotteita ja tuoteryhmiä.
- Ylärivin valikosta linkkien "Selaa tuoteryhmiä" ja "Selaa myytäviä" toiminnot ovat käytössä.
- Toiminto "Selaa tuoteryhmiä" avaa tuoteryhmistä näkymän, joka kertoo tuoteryhmät ja montako tuotetta kussakin ryhmässä on myytävänä.
- Tuoteryhmärivillä olevasta nappulasta "Avaa tuoteryhmä" voi klikata näkyviin kyseisessä tuoteryhmässä myytävänä olevat tuotteet. 
- Näkymä "myytävät tuotteet" kertoo tuotteesta tuoteryhmän, tuotteen nimen, voimassa olevan korkeimman tarjouksen ja sen, paljonko tarjousaikaa on jäljellä. 
- Näkymässä voi klikata "Tietoa tuotteesta", jolloin saa uuden näkymän, jossa on lisää tietoa tuotteesta. Tähän näkymään on tulevaisuudessa mahdollisat liittää myös kuva tuotteesta. Tuotenäkymässä on kaksi nappulaa, "Tee tarjous" ja "Paluu".
- Tarjouksen tekeminen edellyttää asiakkaaksi kirjautumista. Kirjautuminen ei onnistu, ellei ole rekisteröitynyt asiakkaaksi.
- Jos henkilö ei ole kirjautunut asiakkaaksi, on kaikilla sivuilla näkyvissä kehote ja linkki asiakkaaksi rekisteröitymistä varten.


## Käyttöohje - ASIAKAS

- Asiakkaaksi rekisteröitynyt voi tehdä myös ostotarjouksia
- Asiakas voi laittaa tuotteita myyntiin vain ottamalla ensin yhteyttä osoitteeseen Bull@Trumbull.bt (eli ei voi)

## Käyttöohje - ADMIN

- Admin-oikeuksilla voi perustaa tuoteryhmiä ja asettaa tuotteita myytäväksi
- Admin-oikeuksilla voi myös poistaa tuotteita näkyvistä ja saada yhteenvetotietoa

