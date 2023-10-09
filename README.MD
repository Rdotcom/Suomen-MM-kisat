# Suomen MM-kisat peli
Pelin nimi on Suomen MM-kisat. Peli on Jalkapallon MM-kisojen inspiroima. Pelin tarkoitus on kierrellä tulevien MM-kisojen jalkapallostadioneita ja etsiä vastustajia.

#### Katso nämä videot:
Näitä videoita käytettiin apuvälineinä pelin tekemisessä.
[![Watch the videos](https://i.ytimg.com/vi/AVAs9eFomD8/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhBIFUoZTAP&rs=AOn4CLCT0c5w686gZCkuXoLKE4GQnl4lHw)](https://youtube.com/playlist?list=PLKenVLUxjmH9AyGZUeNDs8RinDVLQIQXY)

### Tarina
Olet Huuhkajien kapteeni. Saavuit Yhdysvaltoihin osallistuaksesi vuoden 2026 FIFAn MM-kisoihin. Olet taistellut urhoollisesti karsintavaiheen läpi ja tehnyt maastasi ylpeän. Nyt alkaa todellinen taistelu!
Oletko valmis? Aloitit tiesi kunniaan ja kuuluisuuteen ensimmäiseltä lentokentältä.Olet päättänyt tuoda iloa ja tehdä maanmiehistäsi ylpeitä. 
Saavut ensimmäiselle jalkapallokentälle ja pidät siellä valmistautumisleirin. Jatkat sieltä seuraavalle kentälle ja pelaat siellä ensimmäisen rangaistuspotkukilpailusi. 
Pelaat viisaasti ja voitat Yhdysvallat, joka oli ensimmäinen vastustajasi. Pelaat loput lohkopelisi ja voitat kaksi ensimmäistä peliä. Varmistat itsellesi paikan pudotuspeleihin ja kolmanteen peliin menet rennolla fiiliksellä.
Pudotuspelivaihe alkaa ja nyt on kyllä kovan paikka. Se on Messin johtama Argentiina. Tiedät jo, että mikäli voitat heidät, palkinto tulee olemaan valtava. 
Menet sinne ja näytät heille, mistä olet tehty. Teet turnauksen ensimmäisen yllätyksen ja voitat heidät! Etenet 8-parhaan joukkoon.
Tarinan edetessä siirryt seuraaville lentokentille ja dominoit vastustajiasi. Viimein saavut jollekin jäljellä olevaan lentokenttään ja sieltä löydät viimeisen vastustajasi.
Finaali aika koittaa. Sinun ja maailmanmestaruuden välillä on enää yksi ottelu. Olet synnynnäinen voittaja, eikä häviö ole edes vaihtoehto, kuten olemme jo sen saaneet tietää,
Pelaat finaalin viileästi ja voitat sen. OLET MAAILMANMESTARI!!! Saavutit tavoitteesi ja voitit vastustajasi. Onnittelut!!!


### Relaatiotietokanta

Tämä peli käyttää relaatiotietokantakurssin tietokantaa pohjana.

1. Luo uusi relaatiotietokanta 'footy': `CREATE DATABASE footy;`
2. Vaiha tietokantaan: `USE footy;`
3. Tuo sama `lp.sql` niinkuin teit aikaisemmin kurssilla: `source path/to/lp.sql`
4. Voit pitää `airport` and `contry` taulukot. Poista loput: 
   - `SET FOREIGN_KEY_CHECKS = 0;`
   - `DROP TABLE game;`
   - `DROP TABLE goal;`
   - `DROP TABLE goal_reached;`
   - `SET FOREIGN_KEY_CHECKS = 1;`
5. Luo seuraavat taulukot:
   ```sql
     create table game
     (
         id           int auto_increment
             primary key,
         money        int(8)      null,
         location     varchar(10) null,
         screen_name  varchar(40) null,
         player_range int         null
     )
      charset = latin1;
   
   ```
   ```sql
    create table goal
    (
        id          int         not null
            primary key,
        name        varchar(40) null,
        money       int         null,
        probability int         null
    )
        charset = latin1;
    
    insert into goal (id, name, money, probability)
    values  (1, 'TOPAZ', 300, 4),
            (2, 'EMERALD', 600, 3),
            (3, 'RUBY', 1000, 2),
            (4, 'DIAMOND', 0, 1),
            (5, 'BANDIT', -1, 3);
   ```
   ```sql
    create table ports
    (
        id      int auto_increment
            primary key,
        game    int                  null,
        airport varchar(11)          not null,
        goal    int                  null,
        opened  tinyint(1) default 0 null
    );
   ```
6. Check that you have the necessary tables: `SHOW TABLES;`
   - The result should be like this:
   ```text
    +----------------+
    | Tables_in_test |
    +----------------+
    | airport        |
    | country        |
    | game           |
    | goal           |
    | ports          |
    +----------------+
   ```
