#Challenge 1

 SELECT au.au_id AS "AUTHOR ID", au.au_lname AS "LAST NAME", 
 au.au_fname AS "FIRST NAME", t.title AS "TITLE",
 pub.pub_name AS "PUBLISHER"
 FROM mydb.titles AS t 

INNER JOIN publishers AS pub ON t.pub_id=pub.pub_id
INNER JOIN titleauthor AS ta ON t.title_id=ta.title_id
INNER JOIN authors AS au ON ta.au_id=au.au_id;

#Challenge 2


