# Viite-apuri

Viite-apuri on suomalaisen Wikipedian viitteitten automaattiseen luomiseen tarkoitettu apuväline.

## Asennus
- Kloonaa ensin projekti omalle koneellesi
- Luo Pythonilla virtuaaliympäristö (venv)
- Aktivoi virtuaaliympäristö ja asenna sitten vaaditut paketit komennolla: pip install -r requirements.txt

## Käyttö
Asennuksen jälkeen riittää, että ajat app.py ja annat argumentiksi urlin, esim "py app.py https://kaaoszine.fi/lorna-shoren-will-ramosin-yhteistyo-gnarly-neighborin-kanssa-kuunneltavissa-uudella-riptide-kappaleella/" tuottaisi seuraavan tuloksen:

<ref>{{Verkkoviite | Osoite = https://kaaoszine.fi/lorna-shoren-will-ramosin-yhteistyo-gnarly-neighborin-kanssa-kuunneltavissa-uudella-riptide-kappaleella/ | Nimeke = Lorna Shoren Will Ramosin yhteistyö Gnarly Neighborin kanssa kuunneltavissa uudella ”Riptide”-kappaleella | Tekijä = Arto Mäenpää | Sivusto = kaaoszine.fi | Ajankohta = 17.2.2024 | Viitattu = 19.2.2024 }}</ref>

Tulos asetetaan ajon yhteydessä suoraan leikepöydälle, joten jäljelle jää enää tuloksen liittäminen wiki-editoriin.

Skripti tunnistaa myös jos kyse on arvostelusta, jolloin luodaan rivi jonka voi suoraan liittää == Arvostelut == alle, esim. https://kaaoszine.fi/tutulla-konseptilla-mutta-silti-jotain-jai-puuttumaan-arviossa-temple-ballsin-avalanche/ tuottaa seuraavan tuloksen:

* [[Kaaoszine]]: {{Arvostelutähdet|3|5}}<ref>{{Verkkoviite | Osoite = https://kaaoszine.fi/tutulla-konseptilla-mutta-silti-jotain-jai-puuttumaan-arviossa-temple-ballsin-avalanche/ | Nimeke = Tutulla konseptilla mutta silti jotain jäi puuttumaan – arviossa Temple Ballsin ”Avalanche” | Tekijä = Aleksi Parkkonen | Sivusto = kaaoszine.fi | Ajankohta = 6.2.2024 | Viitattu = 19.2.2024 }}</ref>

## Jatkokehitys
Suunnitteilla on ainakin laajentaa tukea muihin suomalaisiin (ja miksei ulkomaisiin) verkkozineihin mitä itse usein käytän viitteissä.

Mahdollisesti voisin myös luoda jonkinlaisen graafisen käyttöliittymän, ettei tarvitsisi komentoriviltä ajella tätä mutta sen prioriteetti on aika matalalla.
