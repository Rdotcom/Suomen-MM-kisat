create table game (
   id int auto_increment primary key,
   points int(11) null,
   location varchar(10) null,
   screen_name  varchar(40) null,
   player_range int null
);

----------------------------------------------------

create table world (
   id int not null auto_increment primary key,
   name varchar(40) null,
   points int(11) null,
   probability int null
);


insert into world (name, points, probability)
VALUES 
	('Yhdysvallat', 100, 1),
   ('Kanada', 200, 1),
   ('Meksiko', 300, 1),
   ('Marokko', 400, 1),
   ('Brasilia', 800, 1),
	('Ranska', 1200, 1),
	('Argentiina', 2000, 1);
	
-----------------------------------------------------


CREATE TABLE fields (
    id INT(11) NOT NULL,
    ident VARCHAR(40) NOT NULL PRIMARY KEY,
    name VARCHAR(40) NULL,
    latitude_deg DOUBLE NULL,
    longitude_deg DOUBLE NULL,
    continent VARCHAR(40) NULL,
    iso_country VARCHAR(40),
    FOREIGN KEY (iso_country) REFERENCES country(iso_country)
);


INSERT INTO wc_fields (id, ident, name, latitude_deg, longitude_deg, continent, iso_country)
VALUES 
(1, 'CROG', 'Rogers Centre, Kanada', 43.641796, -79.390083, 'NA', 'CA'),
(2, 'CBCP', 'BC Place Vancouver, Kanada', 49.272665576, -123.107166238, 'NA', 'CA'),
(3, 'MMEA', 'Estadio Azteca, Meksiko', 19.3017454597, -99.1502643989, 'NA', 'MX'),
(4, 'MMEJ', 'Estadio Jalisco, Meksiko', 20.703002188, -103.323553706, 'NA', 'MX'),
(5, 'MMEB', 'Estadio de Béisbol Monterrey, Meksiko', 25.7177737956, -100.309448762, 'NA', 'MX'),
(6, 'KMBS', 'Mercedes-Benz Stadium, USA', 33.755489, -84.401993, 'NA', 'US'),
(7, 'KFPB', 'Fenway Park, USA', 42.346268, -71.095764, 'NA', 'US'),
(8, 'KATT', 'AT&T Stadium, USA', 32.747841, -97.093628, 'NA', 'US'),
(9, 'KNRG', 'NRG Stadium, USA', 29.68416393, -95.406498374, 'NA', 'US'),
(10, 'KAHS', 'Arrowhead Stadium, USA', 39.042666496, -94.483664732, 'NA', 'US'),
(11, 'KSFS', 'SoFi Stadium, USA', 33.953587, -118.339630, 'NA', 'US'),
(12, 'KHRS', 'Hard Rock Stadium, USA', 25.957960, -80.239311, 'NA', 'US'),
(13, 'KMLS', 'MetLife Stadium, USA', 40.813778, -74.074310, 'NA', 'US'),
(14, 'KLFF', 'Lincoln Financial Field, USA', 39.900898, -75.168098, 'NA', 'US'),
(15, 'KLSS', 'Levis Stadium, USA', 37.4020148919, -121.968869091, 'NA', 'US'),
(16, 'KCLF', 'CenturyLink Field, USA', 47.590497638, -122.325665364, 'NA', 'US');


--------------------------------------------------------------------------------------

create table arenas
(
	id int auto_increment primary key,
    game int null,
    airport varchar(11) not null,
    goal int null,
    opened tinyint(1) default 0 null
);

---------------------------------------------------------------------------------------

