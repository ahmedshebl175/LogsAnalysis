# LogsAnalysis
First Project - Nano Degree -1MAC - UDACITY

I just connect to the DB "news" 
then execute 3 queries fetch the results of the 3 queries in three variables(result1- result2- result3)
then with 3 for-loops I print the results in the command line program with a title for each.

# The views that I created in the database "news":

# log_slug: To set up  "path" field in "log" table to a relation with "slug" field in the "articles" table
CREATE VIEW log_slug as 
(
SELECT substring(path from 10) as slug FROM log
);

# most_three_articles: To get the requirement 1 ( the most popular three articles of all time)
CREATE VIEW most_three_articles as
(
SELECT a.title, COUNT(*) as num
FROM articles a
JOIN log_slug ls
ON a.slug = ls.slug
GROUP BY a.title
ORDER BY num desc
limit 3
);
----------------------------------------
# most_all_authors: To get the requirement 2 ( the most popular article authors of all tim)
CREATE VIEW most_all_authors as 
(
SELECT au.name as name, COUNT(*) as num
FROM authors au
JOIN articles a
ON au.id = a.author
JOIN log_slug ls
ON a.slug = ls.slug
GROUP BY name
ORDER BY num desc
);
---------------------------------------------------------------------
# more_errors: To get the requirement 3 ( which days did more than 1% of requests lead to errors)
CREATE VIEW more_errors as
( 
SELECT TO_CHAR(DATE(time), 'month dd, yyyy') as date, (COUNT(status) filter(where status not like '%200%')*1.0/COUNT(status)*1.0) *100 as percent 
FROM log
GROUP BY date 
HAVING (COUNT(status) filter(where status not like '%200%')*1.0/COUNT(status)*1.0)*100 > 1
);
