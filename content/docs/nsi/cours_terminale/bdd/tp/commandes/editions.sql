CREATE TABLE "vendeur" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"Nom"	        TEXT NOT NULL,
	"Prenom"	    TEXT NOT NULL,
	"Grade"	        INTEGER NOT NULL,
	"Embauche"	    TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "client" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"Nom"	        TEXT NOT NULL,
	"Prenom"	    NUMERIC NOT NULL,
	"Ville"	        TEXT NOT NULL,
	"code_postal"	TEXT NOT NULL,
	"Adresse"	    TEXT NOT NULL,
	"email"	        TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "commande" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"id_vendeur"	INTEGER NOT NULL,
	"id_client"	    INTEGER NOT NULL,
	"montant"	    INTEGER NOT NULL,
	"reglement"	    TEXT NOT NULL,
	"date"	        TEXT NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_client")  REFERENCES "client"("id"),
	FOREIGN KEY("id_vendeur") REFERENCES "vendeur"("id")
);

INSERT INTO vendeur ("Nom", "Prenom", "Grade", "Embauche") VALUES("Kezac", "Annie", 3, "2020/04/12");
INSERT INTO vendeur ("Nom", "Prenom", "Grade", "Embauche") VALUES("Ramon", "Marc", 2, "2019/02/10");
INSERT INTO vendeur ("Nom", "Prenom", "Grade", "Embauche") VALUES("Lucerne", "Paul", 1, "2020/05/11");
INSERT INTO vendeur ("Nom", "Prenom", "Grade", "Embauche") VALUES("Villani", "Pieter", 3, "2021/01/04");
INSERT INTO vendeur ("Nom", "Prenom", "Grade", "Embauche") VALUES("Rudin", "Farid", 2, "2021/03/19");
INSERT INTO vendeur ("Nom", "Prenom", "Grade", "Embauche") VALUES("Queffelec", "Philip", 4, "2021/06/17");


INSERT INTO client ("Nom", "Prenom", "Ville", "code_postal", "Adresse", "email") VALUES("Germain", "Felix", "Lille", "59000", "1 rue Solferino", "fg@exemple.com");
INSERT INTO client ("Nom", "Prenom", "Ville", "code_postal", "Adresse", "email") VALUES("Franoux", "Armand", "Lille", "59000", "2 rue Basse", "armando@exemple.com");
INSERT INTO client ("Nom", "Prenom", "Ville", "code_postal", "Adresse", "email") VALUES("Pommier", "Daphne", "Lomme", "59160", "50 rue Clémenceau", "daphne.pommier@exemple.com");
INSERT INTO client ("Nom", "Prenom", "Ville", "code_postal", "Adresse", "email") VALUES("Kibali", "Roger", "Hazebrouck", "59190", "33 rue de la Paix", "rk@exemple.com");
INSERT INTO client ("Nom", "Prenom", "Ville", "code_postal", "Adresse", "email") VALUES("Nguyen", "Trang", "Roubaix", "59100", "77 Grand rue", "trang.nguyen@exemple.com");
INSERT INTO client ("Nom", "Prenom", "Ville", "code_postal", "Adresse", "email") VALUES("Koulibali", "Ahmid", "Lille", "59000", "1 avenue des Fleurs", "ahmid@exemple.com");


INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(1, 1, 159, "CB", "2021/02/12");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(1, 2, 987, "Espèce", "2021/03/02");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(2, 3, 1987, "Espèce", "2021/03/03");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(2, 4, 910, "Chèque", "2021/04/29");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(2, 4, 1298, "CB", "2021/04/30");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(3, 3, 9876, "Virement", "2021/05/18");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(4, 1, 983, "Virement", "2021/06/11");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(4, 4, 210, "Virement", "2021/06/14");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(5, 6, 3210, "Espèce", "2021/07/15");
INSERT INTO commande (id_vendeur, id_client, montant, reglement, date) VALUES(6, 5, 1345, "CB", "2021/08/17");
