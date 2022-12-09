-- Name: Jonathan Ojangole  Student No: 101209177

-- Please Note: User and Order in the Relational database are implemented as UserB and OrderB respectively
--             due to naming conflicts with PostgreSql
-- Create Database
CREATE DATABASE Store;

-- Creating tables in Database
CREATE TABLE IF NOT EXISTS Owner (username VARCHAR(255), password VARCHAR(255), PRIMARY KEY(username));
CREATE TABLE IF NOT EXISTS StoreReport (isbn NUMERIC(13,0),username VARCHAR(255), stock INT, threshold INT, sales INT,month_sold VARCHAR(255), PRIMARY KEY(isbn, username), FOREIGN KEY(isbn) REFERENCES Book(isbn), FOREIGN KEY(username) REFERENCES UserB(username));
CREATE TABLE IF NOT EXISTS Book (isbn NUMERIC(13,0), name VARCHAR(255) NOT NULL, author VARCHAR(255) NOT NULL, publisher VARCHAR(255) NOT NULL, price INT, genre VARCHAR(255),pages INT,PRIMARY KEY(isbn));
CREATE TABLE IF NOT EXISTS BookOrder (orderNumber NUMERIC(13,0), isbn NUMERIC(13,0), quantity INT,PRIMARY KEY(orderNumber,isbn), FOREIGN KEY(orderNumber) REFERENCES OrderB(orderNumber),FOREIGN KEY(isbn) REFERENCES Book(isbn));
CREATE TABLE IF NOT EXISTS OrderB (orderNumber NUMERIC(13,0), shipping_service VARCHAR(255), order_tracking_no VARCHAR(24), order_date DATE, billing_address NUMERIC(5,0), shipping_address NUMERIC(5,0), PRIMARY KEY(orderNumber),FOREIGN KEY(billing_address) REFERENCES Address(addressID), FOREIGN KEY(shipping_address) REFERENCES Address(addressID));
CREATE TABLE IF NOT EXISTS Orders (username VARCHAR(255), orderNumber NUMERIC(13,0), PRIMARY KEY(username,orderNumber),FOREIGN KEY(username) REFERENCES UserB(username), FOREIGN KEY(orderNumber) REFERENCES OrderB(orderNumber));
CREATE TABLE IF NOT EXISTS UserB (username VARCHAR(255), password VARCHAR(255), FirstName VARCHAR(255), LastName VARCHAR(255), email VARCHAR(255), user_address NUMERIC(5,0),  PRIMARY KEY(username),FOREIGN KEY(user_address) REFERENCES Address(addressID)  );
CREATE TABLE IF NOT EXISTS Publisher (publisherID NUMERIC(5,0), name VARCHAR(255), email VARCHAR(255), phoneNumber NUMERIC(10,0), bank_account NUMERIC(7,0), publisher_address NUMERIC(5,0), PRIMARY KEY (publisherID),FOREIGN KEY(publisher_address) REFERENCES Address(addressID));
CREATE TABLE IF NOT EXISTS Publishes (isbn NUMERIC(13,0),publisherID NUMERIC(5,0),salesPercentage INT, PRIMARY KEY(isbn,publisherID), FOREIGN KEY(isbn) REFERENCES Book(isbn), FOREIGN KEY(publisherID) REFERENCES Publisher(publisherID));
CREATE TABLE IF NOT EXISTS Address (addressID NUMERIC(5,0), street VARCHAR(255), city VARCHAR(255), province VARCHAR(255),postal_code VARCHAR(255), country VARCHAR(255), PRIMARY KEY(addressID));

-- queries used to initialize data in tables
INSERT INTO Book VALUES
    (9000000000001, "Book1", "Author1", "Publisher1", 100, "Genre1", 500),
    (9000000000002, "Book2", "Author2", "Publisher2", 200, "Genre2", 550),
    (9000000000003, "Book3", "Author3", "Publisher1", 300, "Genre3", 400),
    (9000000000004, "Book4", "Author4", "Publisher2", 400, "Genre4", 450),
ON CONFLICT (isbn) DO NOTHING;

INSERT INTO Address VALUES
    (10001, "street1", "city1", "province1", "postal_code1", "country1"),
    (10002, "street2", "city2", "province2", "postal_code2", "country2"),
ON CONFLICT (addressID) DO NOTHING;

INSERT INTO Publisher VALUES
    (90001, "Publisher1", "publisher1@ojangole.com", 1234567891, 8574638, 10001),
    (90002, "Publisher2", "publisher2@ojangole.com", 1388998383, 9038373, 10002),
ON CONFLICT (publisherID) DO NOTHING;

INSERT INTO Publishes VALUES
    (9000000000001,90001, 10),
    (9000000000002,90002, 10),
    (9000000000003,90001, 20),
    (9000000000004,90002, 20),
 ON CONFLICT (isbn,publisherID) DO NOTHING;

-- queries in functions
-- 1.sql query to register owner
INSERT INTO Owner VALUES 
    ("username","password") 
ON CONFLICT (username) DO NOTHING;

-- 2. sql query to register owner
INSERT INTO UserB VALUES 
("username","password","FirstName","LastName","email","user_address") 
ON CONFLICT (username) DO NOTHING;

-- 3. sql query to add address
INSERT INTO Address VALUES 
("addressID","street","city","province","postal_code","country") 
ON CONFLICT (addressID) DO NOTHING;

-- 4. sql query to authenticate Owner
SELECT FROM Owner 
WHERE username = "username" 
AND password = "password";

-- 5. sql query to authenticate User
SELECT FROM UserB 
WHERE username = "username" 
AND password = "password";

-- 6. sql query to add Book
INSERT INTO Book VALUES 
("isbn", "name", "author", "publisher", "price", "genre", "pages") 
ON CONFLICT (isbn) DO NOTHING;

-- 7. sql queries to delete book by isbn
DELETE FROM StoreReport WHERE isbn = 90000000000001;
DELETE FROM BookOrder WHERE isbn = 90000000000001;
DELETE FROM Publishes WHERE isbn = 90000000000001;
DELETE FROM Book WHERE isbn = 90000000000001;

-- 8. sql query to generate StoreReport
SELECT* FROM StoreReport;

-- 9. sql queries to browse books
SELECT* FROM Book WHERE isbn = 90000000000001;
SELECT* FROM Book WHERE name = "name";
SELECT* FROM Book WHERE author = "author";
SELECT* FROM Book WHERE publisher = "publisher";
SELECT* FROM Book WHERE price = "price";
SELECT* FROM Book WHERE genre = "genre";
SELECT* FROM Book WHERE pages = "pages";

-- 10. sql queries to buy book
INSERT INTO OrderB VALUES 
("orderNumber", "Canpar", str(random.randint(1,1000)),date.today(),"billing_address","shipping_address") 
ON CONFLICT (orderNumber) DO NOTHING;

INSERT INTO Orders VALUES 
("username","orderNumber") 
ON CONFLICT ("username", "orderNumber") DO NOTHING;

SELECT * from Book 
WHERE name = "name";

INSERT INTO BookOrder VALUES 
("orderNumber","isbn","quantity") 
ON CONFLICT ("orderNumber","isbn") DO NOTHING;

INSERT INTO StoreReport VALUES 
("isbn","username",100, 10, sales, datetime.now().strftime("%m")) 
ON CONFLICT (isbn,username) DO NOTHING;

