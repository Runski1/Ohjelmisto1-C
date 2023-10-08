# READ ME (FOR REAL)

## Nämä sitten seuraavassa kurssissa

search pitäisi estää, jos pelaaja on jo etsinyt kaupungista, tai ainakin tulostaa onko hän etsinyt current locationistaan vai ei. Mahdollisesti search voisi olla kokonaan automaattinen, eikä käyttäisi vuoroa. silloin hire on turha, mutta hire voisi mahdollisesti etsiä toisesta kaupungista? siinä pitää tehdä joku juttu, ettei toinen pelaaja yoinkaa sitä laukkua

Peli voi olla melko pitkä, en ole edes varma kuinka pitkä. Pelasin itseäni vastaan kierroksen siten, että tiesin miissä laukku oli. Se on yllättävän jännittävä peli siten, koska pitää miettiä järkevin reitti määränpäähän. Se ei ole mielenkiintoista jos laukku on jossain Tukholmassa, mutta minulla oli Gran Canarialla. **Pitäisikö luoda se mahdollisuus, että pelaajat voivat halutessaan tulostaa uuden pelin valittuaan sen laukun sijainnin?**

## Bugit

- man-funktion virheellinen parametri crashaa pelin
- minkä tahansa matkustusfunktion ajaminen virheellisellä parametrilla (liian kaukana tai väärä syöte) skippaa vuoron

#### pikkubugit

- Jossain on ylimääräinen press ENTER to continue-rivi
- laivalla tulostaa lokaation eikä "travelling to"