--Challenge 1

 SELECT au.au_id AS "AUTHOR ID", au.au_lname AS "LAST NAME", 
 au.au_fname AS "FIRST NAME", t.title AS "TITLE",
 pub.pub_name AS "PUBLISHER"
 FROM mydb.titles AS t 

INNER JOIN publishers AS pub ON t.pub_id=pub.pub_id
INNER JOIN titleauthor AS ta ON t.title_id=ta.title_id
INNER JOIN authors AS au ON ta.au_id=au.au_id
ORDER BY au.au_id DESC;;

--Challenge 2

SELECT au.au_id AS "AUTHOR ID", au.au_lname AS "LAST NAME", 
 au.au_fname AS "FIRST NAME", t.title AS "TITLE",
 pub.pub_name AS "PUBLISHER", COUNT(*) as "TITLE COUNT"
 FROM mydb.titles AS t 

INNER JOIN publishers AS pub ON t.pub_id=pub.pub_id
INNER JOIN titleauthor AS ta ON t.title_id=ta.title_id
INNER JOIN authors AS au ON ta.au_id=au.au_id
GROUP BY t.title
ORDER BY au.au_id DESC, count(*) DESC ;


--Challenge 3

SELECT au.au_id AS "AUTHOR ID", au.au_lname AS "LAST NAME", 
 au.au_fname AS "FIRST NAME", 
 sum(t.ytd_sales) AS "TOTAL"
 FROM mydb.titles AS t 
 
JOIN sales AS sa ON t.title_id=sa.title_id
JOIN titleauthor AS ta ON t.title_id=ta.title_id
JOIN authors AS au ON ta.au_id=au.au_id
GROUP BY au.au_id
ORDER BY sum(t.ytd_sales) DESC
LIMIT 3;



--Challenge 4

SELECT au.au_id AS "AUTHOR ID", au.au_lname AS "LAST NAME", 
 au.au_fname AS "FIRST NAME", 
 sum(t.ytd_sales) AS "TOTAL"
 FROM mydb.titles AS t 
 
LEFT JOIN sales AS sa ON t.title_id=sa.title_id
RIGHT JOIN titleauthor AS ta ON t.title_id=ta.title_id
RIGHT JOIN authors AS au ON ta.au_id=au.au_id
GROUP BY au.au_id
ORDER BY sum(t.ytd_sales) DESC;
--No sé cambiar el null por cero!

--Otra opción:

SELECT au.au_id AS "AUTHOR ID", au.au_lname AS "LAST NAME", 
 au.au_fname AS "FIRST NAME", 
 sum(sa.qty) AS "TOTAL"
 FROM mydb.authors AS au

LEFT JOIN titleauthor AS ta ON au.au_id=ta.au_id
LEFT JOIN sales AS sa ON ta.title_id=sa.title_id

GROUP BY au.au_id
ORDER BY sum(sa.qty) DESC;
