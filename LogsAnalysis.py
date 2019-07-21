#! /usr/bin/env python

import psycopg2

DBNAME = "news"

# Connect to DB "news"
try:
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)

# requirement 1: the most popular three articles of all time
try:
    c.execute("SELECT * FROM most_three_articles")
    result1 = c.fetchall()
except psycopg2.Error as e:
    print(e.pgerror)

# requirement 2: the most popular article authors of all time
try:
    c.execute("SELECT * FROM most_all_authors")
    result2 = c.fetchall()
except psycopg2.Error as e:
    print(e.pgerror)

# requirement 3: the days did more than 1% of requests lead to errors
try:
    c.execute("SELECT * FROM more_errors")
    result3 = c.fetchall()
except psycopg2.Error as e:
    print(e.pgerror)

# Close cursor and connection
c.close()
db.close()

# Print results
print
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

