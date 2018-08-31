# KO-Huutokauppa

Nykyinen sovellus on kenen tahansa kokeiltavissa Heroku-palvelussa: https://tsoha-ko-huutokauppa.herokuapp.com

Sovellus on ladattavissa osoitteesta https://github.com/ktojala/KO-Huutokauppa

## Asennusohje Linux-koneellesi - alkutilanne

Sinulla on koneellesi asennettuna Python-versio 3.5 tai uudempi.
Käytössäsi tulee myös olla Pythonin pip-kirjasto apukirjastojen lataamiseen sekä venv-kirjasto

(venv-kirjastolla voit luoda toisistaan riippumattomia Python-projekteja virtuaaliympäristöihin) 

Tarvitset omalle koneellesi SQL-tietokantaohjelmiston.
SQLite ja PostgreSQ käyvät tähän tarkoitukseen.

## Asennustoimet

1. Paina github-sivun oikeasta ylälaidasta vihreää nappulaa "Clone or download" ja valitse "Download zip"
2. Lataamisen jälkeen pura tiedostot komennolla "Extract To" esimerkiksi kansioon "home/username/gitti"
3. Komentorivillä mene kansioon gitti/KO-Huutokauppa-master/
4. Luo virtuaaliymäristö komennolla python3 -m venv myvenv (tämä tarvitsee tehdä vain kerran)
5. Aktivoi virtuaaliympäristö komennolla source myvenv/bin/activate
6. Tarvitset myös Pythonin Flask-kirjaston. Jos sitä ei vielä ole, ota se käyttöön komennolla pip install Flask
7. Jos saat tiedon siitä, että käytössäsi oleva pip on vanha, päivitä se komennolla pip install --upgrade pip
8. Sovellukseen liittyvät vaatimukset asennetaan komennolla pip install -r requirements.txt (vain kerran)
9. Käynnistä sovellus virtuaaliympäristössä komennolla python run.py
10. Pääset käynnissä olevan sovelluksen etusivulle selaimessa osoitteessa http://127.0.0.1:5000

## Hyödyllinen tieto

Jos sovellusta käynnistettäessä seuraavat taulut account, rooli, asiakasrooli ovat tyhjät, sovellus luo
automaattisesti kaksi oletuskäyttäjää: "testi" ja "admin". Käyttäjällä testi on ASIAKAS-rooli ja sitä vastaavat oikeudet, 
käyttäjällä admin sen lisäksi ADMIN-rooli ja sitä vastaavat oikeudet.

