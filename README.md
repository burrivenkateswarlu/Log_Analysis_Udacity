# Loganalysis Project

### By Burri Venkateswarlu

Logs Analysis Project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project Overview

A Reporting tool that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Files in the project

This project consists the following files:

* LogAnalysis_Udacity.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* newsdata.sql - database file
* OutPut.png

## Requirement tools for the project

1. Python
2. Vagrant
3. VirtualBox


## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install and Run the project
Install Vagrant & VirtualBox
- For Create Vagrant file :`vagrant init ubuntu/xenial64`
- For Connect to VirtualMachine :`vagrant up`
- For Login to VirtualMachine : `vagrant ssh`
- For Exit from current directory : `cd ..`
- We should Again exit directory :cd ..`
- For Changing directory path :cd vagrant`
- For Update ubunut version using :`sudo apt-get update``

## We have to install postgresql

- Install postgresql using  `sudo apt-get install postgresql`
- Connect to postgres using  `psql su - postgres`

## We have to install modules

- Import psycopg2 module to connect database using command `pip install psycopg2`
- Create super user vagrant
- Create news database with owner vagrant using command `create database news;`
- Change ownership of database using command `alter database news owner to vagrant;`
- Exit the current running status using command `\q`
- Logout from the current user using command `logout`
- load the data in local database using the command:
  ```
    $ psql -d news -f newsdata.sql
	$ psql -d news -f views.sql
  ```
- run `python LogAnalysis_Udacity.py` 

# Creating views
## To create views we have to connect to the psql.

## views used in this project
view_1:  CREATE VIEW log_article_auths AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;

	
view_2:	CREATE VIEW log_article_vws AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;


view_3:	CREATE VIEW l_o_g_s AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;


view_4: CREATE VIEW err_logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;


### Final OutPut
```

 What are the most popular three articles of all time ?

 Candidate is jerk, alleges rival -- 338647 views
 Bears love berries, alleges bear -- 253801 views
 Bad things gone, say good people -- 170098 views

 Who are the most popular article authors of all time ?

 "Ursula La Multa" -- 507594 views
 "Rudolf von Treppenwitz" -- 423457 views
 "Anonymous Contributor" -- 170098 views
 "Markoff Chaney" -- 84557 views

 Days on which more than 1% of requests lead to errors ?
 On 17-JUL-2016   ===>   2.3% errors
```

## Miscellaneous
![output.png]((https://github.com/burrivenkateswarlu/Log_Analysis_Udacity/blob/master/output.png))
