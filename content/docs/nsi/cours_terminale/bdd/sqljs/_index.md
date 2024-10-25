---
title: "Editeur SQL"
weight: 1000

---

Cette partie présente différentes manières d'intégrer une BDD dynamique dans une page web.

Il n'y a pas grand chose à faire, simplement s'assurer qu'on obtient des réponses et qu'elles sont cohérentes.


Lorsque la page est chargée par le navigateur, celui-ci crée en mémoire une base de donnée par bloc respectif.
Celles sont indépendantes et sont réinitialisées à chaque chargement. Pensez à écrire vos requêtes à l'extérieur avant de recharger.
Plusieurs requêtes peuvent être exécutées dans une seule fenêtre d'édition :

```sql
SELECT * FROM employees;
SELECT id, name FROM employees;
```

Va afficher deux tables.

Ainsi, on peut modifier la BDD et afficher le résultat immédiatement.

# Sql dans le navigateur



{{< sql title="Depuis un fichier init" init="init.sql">}}
SELECT * FROM employees;
{{< /sql >}}



{{< sql title="depuis un fichier bdd" dbfile="employees.db" >}}
SELECT * FROM employees;
{{< /sql >}}


{{< sql title="Autre fichier init" init="init_2.sql">}}
SELECT * FROM employees;
{{< /sql >}}


{{< sql title="depuis un fichier bdd 2" dbfile="employees.db" >}}
SELECT * FROM employees;
{{< /sql >}}

{{< sql title="sans contenu préchargé">}}
DROP TABLE IF EXISTS employees;
CREATE TABLE employees( id          integer,  name    text,
                          designation text,     manager integer,
                          hired_on    date,     salary  integer,
                          commission  float,    dept    integer);

  INSERT INTO employees VALUES (1,'JOHNSON','ADMIN',6,'1990-12-17',18000,NULL,4);
  INSERT INTO employees VALUES (2,'HARDING','MANAGER',9,'1998-02-02',52000,300,3);
  INSERT INTO employees VALUES (3,'TAFT','SALES I',2,'1996-01-02',25000,500,3);
  INSERT INTO employees VALUES (4,'HOOVER','SALES I',2,'1990-04-02',27000,NULL,3);
  INSERT INTO employees VALUES (5,'LINCOLN','TECH',6,'1994-06-23',22500,1400,4);
  INSERT INTO employees VALUES (6,'GARFIELD','MANAGER',9,'1993-05-01',54000,NULL,4);
  INSERT INTO employees VALUES (7,'POLK','TECH',6,'1997-09-22',25000,NULL,4);
  INSERT INTO employees VALUES (8,'GRANT','ENGINEER',10,'1997-03-30',32000,NULL,2);
  INSERT INTO employees VALUES (9,'JACKSON','CEO',NULL,'1990-01-01',75000,NULL,4);
  INSERT INTO employees VALUES (10,'FILLMORE','MANAGER',9,'1994-08-09',56000,NULL,2);
  INSERT INTO employees VALUES (11,'ADAMS','ENGINEER',10,'1996-03-15',34000,NULL,2);
  INSERT INTO employees VALUES (12,'WASHINGTON','ADMIN',6,'1998-04-16',18000,NULL,4);
  INSERT INTO employees VALUES (13,'MONROE','ENGINEER',10,'2000-12-03',30000,NULL,2);
  INSERT INTO employees VALUES (14,'ROOSEVELT','CPA',9,'1995-10-12',35000,NULL,1);

SELECT designation,COUNT(*) AS nbr, (AVG(salary)) AS avg_salary FROM employees GROUP BY designation ORDER BY avg_salary DESC;
SELECT name,hired_on FROM employees ORDER BY hired_on;
{{< /sql >}}
