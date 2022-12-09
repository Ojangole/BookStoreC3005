Name: Jonathan Ojangole  Student No: 101209177

Program: The program is a book store which has two pages: one for an owner and another for a user. 

All user input is taken in from a CLI.

The program registers users, allows them to browse and buy books. Authentication is required to complete each action.
The program registers owners, allows them to add or remove books and generate a store report. Authentication is required to complete each action.

ASSUMPTIONS and notes
- The Owner has a deal with a limited number of publishers set at initialization and can only add their books
- The Owner adds 100 books at a time.

Please Note: User and Order in the Relational database are implemented as UserB and OrderB respectively
due to naming conflicts with PostgreSql.

How to connect
- The program uses PostgreSql to access a database. Please have one set up through pgadmin4. 
Please remember your pgadmin4 database password. 
- In pgadmin4, run this sql query 

CREATE DATABASE Store;

- Keep pgadmin4 open and connect using psycopg2 by replacing the password in line 7 of the project.py file
with your pgadmin4 database password. The line of code is shown below.

conn = psycopg2.connect("dbname=store user=postgres password=[yourPassword]")

Here is a complete tutorial if you are having any issues
https://pynative.com/python-postgresql-tutorial/.
