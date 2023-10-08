# READ ME (FOR REAL)

search pitäisi estää, jos pelaaja on jo etsinyt kaupungista, tai ainakin tulostaa onko hän etsinyt current locationistaan vai ei. Mahdollisesti search voisi olla kokonaan automaattinen, eikä käyttäisi vuoroa. silloin hire on turha, mutta hire voisi mahdollisesti etsiä toisesta kaupungista? siinä pitää tehdä joku juttu, ettei toinen pelaaja yoinkaa sitä laukkua

Peli voi olla melko pitkä, en ole edes varma kuinka pitkä. Pelasin itseäni vastaan kierroksen siten, että tiesin miissä laukku oli. Se on yllättävän jännittävä peli siten, koska pitää miettiä järkevin reitti määränpäähän. Se ei ole mielenkiintoista jos laukku on jossain Tukholmassa, mutta minulla oli Gran Canarialla. **Pitäisikö luoda se mahdollisuus, että pelaajat voivat halutessaan tulostaa uuden pelin valittuaan sen laukun sijainnin?**

## Bugit

- email-event triggerääntyy joka kerta, kun löytää minkä tahansa laukun
- takaisin helsinkiin päässeen pelaajan vuoro jää voimaan, jollei pääse sysmään, pitääs skipata esim searchilla
- man-funktion virheellinen parametri crashaa pelin
- minkä tahansa matkustusfunktion ajaminen virheellisellä parametrilla (liian kaukana tai väärä syöte) skippaa vuoron


## Changelog

#### UIP.py

***Commenttasin event_randomizerin lentofunktiosta.*** Lentämistä pystyy tekemään niin harvoin, ettei sillä ole juuri merkitystä pelin kannalta. Lisäksi siitä seuraa: *pelaaja ei voi olla lukossa lennon jälkeen.* Silloin printerissä toimii ehto, että mikäli pelaajalla on lockstatea ja sijainti, pelaaja on matkalla siihen sijaintiin.

#### helsinki_sysma.py

exit() lisätty voittotekstin jälkeen

#### functions.py

##### generate_additional_bags

generoi nyt oikean määrän laukkuja (pelaajamäärä - 1)

##### event_randomizer

kommentoin pois no events for you -printin

your PP updates -> your PP changes

##### printer

jos pelaajalla on total_dice, printtaa sijainnin sijaan you're travelling to...

lockstate-termit vaihdettu kansankielisimmiksi

#### end_game_email.py

tulostaa laukkujen lkm ja sijainnit kuten alunperin, mutta ei luo laukkuja eikä arvo random kaupunkeja


useampi press enter to continue-rivi **ctrl+shift+F** tarkemmat sijainnit

asdfasdf
