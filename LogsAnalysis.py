# Database code for the DB news

import psycopg2

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

c.execute("SELECT * FROM most_three_articles")    # requirement 1
result1 = c.fetchall()

c.execute("SELECT * FROM most_all_authors")    # requirement 2
result2 = c.fetchall()

c.execute("SELECT * FROM more_errors")    # requirement 3
result3 = c.fetchall()

db.close()
print()
print("The most popular three articles of all time")
print("--------------------------------------------")
for row in result1:
    print('"' + row[0] + '" - ' + str(row[1]) + ' views') 

print
print("The most popular article authors of all time")
print("--------------------------------------------")
for row in result2:
    print(row[0] + ' - ' + str(row[1]) + ' views') 

print
print("Days did more than 1% of requests lead to errors")
print("--------------------------------------------")
for row in result3:
    print(row[0] + ' - ' + str(round(row[1], 1)) + '% errors') 
print