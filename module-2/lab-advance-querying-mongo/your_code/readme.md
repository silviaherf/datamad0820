1. All the companies whose name match 'Babelgum'. Retrieve only their name field.

FILTER ({name:'Babelgum'}
PROJECT {name:1}

2. All the companies that have more than 5000 employees. Limit the search to 20 companies and sort them by number of employees.

FILTER {number_of_employees: {$gt: 500} }
SORT {number_of_employees:1}
MAXITEMS 20

3. All the companies founded between 2000 and 2005, both years included. Retrieve only the name and founded_year fields.
FILTER {"$and": [{founded_year: {$gte: 2000}},{founded_year: {$lte: 2005}}] }
PROJECT  {name:1,founded_year:1}


4. All the companies that had a Valuation Amount of more than 100.000.000 and have been founded before 2010. Retrieve only the name and ipo fields.
FILTER  {"$and": [{"ipo.valuation_amount": {$gt: 100000000}},{founded_year: {$lte: 2010}}] } 
PROJECT  {name:1,ipo:1}



5. All the companies that have less than 1000 employees and have been founded before 2005. Order them by the number of employees and limit the search to 10 companies.
FILTER 
PROJECT
SORT 
MAXITEMS 20

6. All the companies that don't include the partners field.
FILTER 
PROJECT
SORT 
MAXITEMS 20
7. All the companies that have a null type of value on the category_code field.
FILTER 
PROJECT
SORT 
MAXITEMS 20
8. All the companies that have at least 100 employees but less than 1000. Retrieve only the name and number of employees fields.
FILTER 
PROJECT
SORT 
MAXITEMS 20
9. Order all the companies by their IPO price in a descending order.
1
# Your Code
10. Retrieve the 10 companies with more employees, order by the number of employees
FILTER 
PROJECT
SORT 
MAXITEMS 20
11. All the companies founded on the second semester of the year. Limit your search to 1000 companies.
FILTER 
PROJECT
SORT 
MAXITEMS 20
12. All the companies founded before 2000 that have an acquisition amount of more than 10.000.00
FILTER 
PROJECT
SORT 
MAXITEMS 20
13. All the companies that have been acquired after 2010, order by the acquisition amount, and retrieve only their name and acquisition field.
FILTER 
PROJECT
SORT 
MAXITEMS 20
14. Order the companies by their founded year, retrieving only their name and founded year.
1
# Your Code
15. All the companies that have been founded on the first seven days of the month, including the seventh. Sort them by their acquisition price in a descending order. Limit the search to 10 documents.
1
# Your Code
16. All the companies on the 'web' category that have more than 4000 employees. Sort them by the amount of employees in ascending order.
1
# Your Code
17. All the companies whose acquisition amount is more than 10.000.000, and currency is 'EUR'.
1
# Your Code
18. All the companies that have been acquired on the first trimester of the year. Limit the search to 10 companies, and retrieve only their name and acquisition fields.
1
# Your Code
Bonus
19. All the companies that have been founded between 2000 and 2010, but have not been acquired before 2011.
1
# Your Code
20. All the companies that have been 'deadpooled' after the third year