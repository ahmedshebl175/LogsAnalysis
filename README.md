# LogsAnalysis
## First Project - Nano Degree -1MAC - UDACITY

# Pre-requisite:
    -Git Bash(https://git-scm.com/downloads)
    - Vagrant(https://www.vagrantup.com/)
    - Download the VM configuration(https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/   5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
    - Virtual Box(https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
    - DB file: newsdata.sql(https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

# Instructions:
    - In the vagrant directory in your vm, run Git Bash
    - run command "vagrant up"
    - run command "vagrant ssh"
    - To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
    - Creating Views(shown below) using command psql news to communicate to DB
    - run command "python logsanalysis.py"


# The views that I created in the database “news”:
###  log_slug: To set up “path” field in “log” table to a relation with “slug” field in the “articles” table
CREATE VIEW log_slug as
(
SELECT substring(path from 10) as slug FROM log
);

### most_three_articles: To get the requirement 1 ( the most popular three articles of all time)
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

### most_all_authors: To get the requirement 2 ( the most popular article authors of all tim)
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

### more_errors: To get the requirement 3 ( which days did more than 1% of requests lead to errors)
CREATE VIEW more_errors as
(
SELECT TO_CHAR(DATE(time), ‘month dd, yyyy’) as date, (COUNT(status) filter(where status not like ‘%200%’)*1.0/COUNT(status)*1.0) *100 as percent
FROM log
GROUP BY date
HAVING (COUNT(status) filter(where status not like ‘%200%’)*1.0/COUNT(status)*1.0)*100 > 1
);

### In python file (logsanalysis.py)
    - I connect to the DB then I query(SELECT) the views to get the results and print them out in the command line.

# Version:
    - 1.2

# Author:
    - Ahmed Shebl AbdElKader
