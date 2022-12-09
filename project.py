# Name: Jonathan Ojangole  Student No: 101209177
import psycopg2
import random
from datetime import datetime
from datetime import date

conn = psycopg2.connect("dbname=store user=postgres password=legally5")
mycursor = conn.cursor()

# functions
def registerOwner():
    ownerInput1 = input("Enter a username: ")
    ownerInput2 = input("Enter a password: ")
    initOwnersql = "INSERT INTO Owner VALUES (%s,%s) ON CONFLICT (username) DO NOTHING"
    initOwnerval = (ownerInput1,ownerInput2)
    mycursor.execute(initOwnersql,initOwnerval)
    conn.commit()

def registerUser():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    fn = input("Enter a first name: ")
    ln = input("Enter a last name: ")
    email = input("Enter an email:")
    address = inputandCreateAddress()

    Usersql = "INSERT INTO UserB VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (username) DO NOTHING"
    Userval = (username,password,fn,ln,email,address)
    mycursor.execute(Usersql,Userval)
    conn.commit()

def inputandCreateAddress():
    addID = random.randint(10003, 19999)
    street = input("Enter your street: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal = input("Enter your postal code: ")
    country = input("Enter your country: ")

    addSql = "INSERT INTO Address VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (addressID) DO NOTHING"
    addval = (addID,street,city,province,postal,country)
    mycursor.execute(addSql,addval)
    conn.commit()
    return addID

def authenticateOwner():
    print("\nAuthenticate to continue!!!")
    username = input("Username: ")
    password = input("Password: ")
    rs = False
    authSQl = "SELECT FROM Owner WHERE username = %s AND password = %s"
    authval = (username,password)

    mycursor.execute(authSQl,authval)
    myresult = mycursor.fetchall()

    if(len(myresult) == 0):
        print("\nOwner Authentication failed. Please provide username and password")
    else:
        print("\nAuthentication Successful")
        rs = True
    return rs

def authenticateUser(username):
    password = input("Password: ")
    rs = False
    authSQl = "SELECT FROM UserB WHERE username = %s AND password = %s"
    authval = (username,password)

    mycursor.execute(authSQl,authval)
    myresult = mycursor.fetchall()

    if(len(myresult) == 0):
        print("\nOwner Authentication failed. Please provide username and password")
    else:
        print("\nAuthentication Successful")
        rs = True
    return rs

def addBook():
    Booksql = "INSERT INTO Book VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (isbn) DO NOTHING"
    
    isbnIN = input("\nEnter book isbn: (Must be 13 digits) ")
    nameIn = input("Enter book name: ")
    authorIn =  input("Enter book author: ")
    publisherIN = input("Enter book publisher: ")
    priceIN =  input("Enter book price (MUST be a number): ")
    genreIN =  input("Enter book genre: ")
    pagesIN =  input("Enter book pages (MUST be a number): ")
    
    Bookval = (isbnIN, nameIn, authorIn, publisherIN, priceIN, genreIN , pagesIN)
    
    mycursor.execute(Booksql,Bookval)
    conn.commit()

def removeBook():
    isbnDel = input("\nEnter book isbn: (Must be 13 digits) ")
    delBSql = "DELETE FROM Book WHERE isbn = %s"
    delPSql = "DELETE FROM Publishes WHERE isbn = %s"
    delBOSql = "DELETE FROM BookOrder WHERE isbn = %s"
    delSRSql = "DELETE FROM StoreReport WHERE isbn = %s"
    delVal = (isbnDel,)

    mycursor.execute(delSRSql, delVal)
    conn.commit()
    mycursor.execute(delBOSql, delVal)
    conn.commit()
    mycursor.execute(delPSql, delVal)
    conn.commit()
    mycursor.execute(delBSql, delVal)
    conn.commit()

def generateReport():
    mycursor.execute("SELECT* FROM StoreReport")
    data = mycursor.fetchall()
    for x in data:
        print(x)
    if (len(data) == 0):
        print("\nThere is nothing to show here. We need more customers.")

def browseBooks():
    print("\nHow would you like to browse today? \n1. By isbn?\n2. By name?\n3. By author? \n 4. By publisher? \n5. By price? \n6. By genre? \n 7. By pages?")
    browse = input("Input:")
    browseSQL = ""
    browseType = ""
    if browse == "1":
        print("\nBrowisng by isbn")
        browseType = "isbn"
        browseSQL = "SELECT* FROM Book WHERE isbn = %s"
    elif browse == "2":
        print("\nBrowisng by name")
        browseType = "name"
        browseSQL = "SELECT* FROM Book WHERE name = %s"
    elif browse == "3":
        print("\nBrowisng by author")
        browseType = "author"
        browseSQL = "SELECT* FROM Book WHERE author = %s"
    elif browse == "4":
        print("\nBrowisng by publisher")
        browseType = "publisher"
        browseSQL = "SELECT* FROM Book WHERE publisher = %s"
    elif browse == "5":
        print("\nBrowisng by price")
        browseType = "price"
        browseSQL = "SELECT* FROM Book WHERE price = %s"
    elif browse == "6":
        print("\nBrowisng by genre")
        browseType = "genre"
        browseSQL = "SELECT* FROM Book WHERE genre = %s"
    elif browse == "7":
        print("\nBrowisng by pages")
        browseType = "pages"
        browseSQL = "SELECT* FROM Book WHERE pages = %s"

    In = input("Enter book " + browseType + ": ")
    
    if browseType == "price" or browseType == "pages" or browseType == "isbn":
        In = (int(In))

    browseVal = (In,)
    mycursor.execute(browseSQL, browseVal)
    data = mycursor.fetchall()
    for x in data:
        print(x)
    if (len(data) == 0):
        print("\nSorry, we don't have such a book.")

def buyBook():
    print("\n Ready to buy a book?\n 1. Yes \n 0. No")
    i = input("Input: ")
    if(i=="1"):
        bookName = input("Input Book name that you'd like to buy:")
        bookQuant = input("How many books would you like? (MUST BE INT:")

        print("\nAuthenticate to continue!!!")
        username = input("Username: ")
        authenticateUser(username)

        #creating order
        print("\nInput Billing Address:")
        billing = inputandCreateAddress()
        print("\nInput Shipping Address:")
        shipping = inputandCreateAddress()
        print("Your order is being created:)")
        ordersql = "INSERT INTO OrderB VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (orderNumber) DO NOTHING"
        orderNumber = int(random.randint(7000000000000,7999999999999))
        orderVal = (orderNumber, "Canpar", str(random.randint(1,1000)),date.today(),billing,shipping)
        mycursor.execute(ordersql,orderVal)
        conn.commit()

        #creating Orders
        sorderSql = "INSERT INTO Orders VALUES (%s,%s) ON CONFLICT (username, orderNumber) DO NOTHING"
        sordersVal = (username,orderNumber)
        mycursor.execute(sorderSql,sordersVal)
        conn.commit()

        # creating book order
        #getting isbn and price and publisher
        getISBNsql = "SELECT * from Book WHERE name = %s"
        getISBNval = (bookName,)
        mycursor.execute(getISBNsql,getISBNval)
        result = mycursor.fetchone()
        bookIsbn = result[0]
        bookPrice = result[4]
        #bookPublisher = result[3]

        bookOsql = "INSERT INTO BookOrder VALUES (%s,%s,%s) ON CONFLICT (orderNumber,isbn) DO NOTHING"
        bookOval = (orderNumber,bookIsbn,bookQuant)
        mycursor.execute(bookOsql,bookOval)
        conn.commit()

        #creating store report
        SRsql = "INSERT INTO StoreReport VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (isbn,username) DO NOTHING"
        sales =  int(int(bookPrice)*int(bookQuant))
        SRval = (bookIsbn,username,100, 10, sales, datetime.now().strftime("%m"))
        mycursor.execute(SRsql,SRval)
        conn.commit()

        print("\nYou're order has been created.")
    else:
        print("\nYou can always come back when you are ready to buy something")




# CONTROL FLOW
def main():
    # Deleting tables if exist
    # mycursor.execute("DROP TABLE IF EXISTS Publishes")
    # mycursor.execute("DROP TABLE IF EXISTS Orders")
    # mycursor.execute("DROP TABLE IF EXISTS BookOrder")
    # mycursor.execute("DROP TABLE IF EXISTS StoreReport")
    # mycursor.execute("DROP TABLE IF EXISTS Owner")
    # mycursor.execute("DROP TABLE IF EXISTS Publisher")
    # mycursor.execute("DROP TABLE IF EXISTS UserB")
    # mycursor.execute("DROP TABLE IF EXISTS OrderB")
    # mycursor.execute("DROP TABLE IF EXISTS Book")
    # mycursor.execute("DROP TABLE IF EXISTS Address")

# creating tables
    OWNERsql = "CREATE TABLE IF NOT EXISTS Owner (username VARCHAR(255), password VARCHAR(255), PRIMARY KEY(username))"
    STOREREPORTsql = "CREATE TABLE IF NOT EXISTS StoreReport (isbn NUMERIC(13,0),username VARCHAR(255), stock INT, threshold INT, sales INT,month_sold VARCHAR(255), PRIMARY KEY(isbn, username), FOREIGN KEY(isbn) REFERENCES Book(isbn), FOREIGN KEY(username) REFERENCES UserB(username))"
    BOOKsql = "CREATE TABLE IF NOT EXISTS Book (isbn NUMERIC(13,0), name VARCHAR(255) NOT NULL, author VARCHAR(255) NOT NULL, publisher VARCHAR(255) NOT NULL, price INT, genre VARCHAR(255),pages INT,PRIMARY KEY(isbn))"
    BOOKORDERsql = "CREATE TABLE IF NOT EXISTS BookOrder (orderNumber NUMERIC(13,0), isbn NUMERIC(13,0), quantity INT,PRIMARY KEY(orderNumber,isbn), FOREIGN KEY(orderNumber) REFERENCES OrderB(orderNumber),FOREIGN KEY(isbn) REFERENCES Book(isbn))"
    ORDERsql = "CREATE TABLE IF NOT EXISTS "+ "OrderB"+ " (orderNumber NUMERIC(13,0), shipping_service VARCHAR(255), order_tracking_no VARCHAR(24), order_date DATE, billing_address NUMERIC(5,0), shipping_address NUMERIC(5,0), PRIMARY KEY(orderNumber),FOREIGN KEY(billing_address) REFERENCES Address(addressID), FOREIGN KEY(shipping_address) REFERENCES Address(addressID))"
    ORDERSsql = "CREATE TABLE IF NOT EXISTS Orders (username VARCHAR(255), orderNumber NUMERIC(13,0), PRIMARY KEY(username,orderNumber),FOREIGN KEY(username) REFERENCES UserB(username), FOREIGN KEY(orderNumber) REFERENCES OrderB(orderNumber))"
    USERsql = "CREATE TABLE IF NOT EXISTS " + "UserB" + "(username VARCHAR(255), password VARCHAR(255), FirstName VARCHAR(255), LastName VARCHAR(255), email VARCHAR(255), user_address NUMERIC(5,0),  PRIMARY KEY(username),FOREIGN KEY(user_address) REFERENCES Address(addressID)  )"
    PUBLISHERsql = "CREATE TABLE IF NOT EXISTS Publisher (publisherID NUMERIC(5,0), name VARCHAR(255), email VARCHAR(255), phoneNumber NUMERIC(10,0), bank_account NUMERIC(7,0), publisher_address NUMERIC(5,0), PRIMARY KEY (publisherID),FOREIGN KEY(publisher_address) REFERENCES Address(addressID))"
    PUBLISHESsql = "CREATE TABLE IF NOT EXISTS Publishes (isbn NUMERIC(13,0),publisherID NUMERIC(5,0),salesPercentage INT, PRIMARY KEY(isbn,publisherID), FOREIGN KEY(isbn) REFERENCES Book(isbn), FOREIGN KEY(publisherID) REFERENCES Publisher(publisherID))"
    ADDRESSsql = "CREATE TABLE IF NOT EXISTS Address (addressID NUMERIC(5,0), street VARCHAR(255), city VARCHAR(255), province VARCHAR(255),postal_code VARCHAR(255), country VARCHAR(255), PRIMARY KEY(addressID))"

    mycursor.execute(ADDRESSsql)
    mycursor.execute(BOOKsql)
    mycursor.execute(ORDERsql)
    mycursor.execute(USERsql)
    mycursor.execute(PUBLISHERsql)
    mycursor.execute(OWNERsql)
    mycursor.execute(STOREREPORTsql)
    mycursor.execute(BOOKORDERsql)
    mycursor.execute(ORDERSsql)
    mycursor.execute(PUBLISHESsql)

    # Intialization of table data presumed to be already known 
    initBooksql = "INSERT INTO Book VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (isbn) DO NOTHING"
    initBookval = [
    (9000000000001, "Book1", "Author1", "Publisher1", 100, "Genre1", 500),
    (9000000000002, "Book2", "Author2", "Publisher2", 200, "Genre2", 550),
    (9000000000003, "Book3", "Author3", "Publisher1", 300, "Genre3", 400),
    (9000000000004, "Book4", "Author4", "Publisher2", 400, "Genre4", 450)
    ]
    mycursor.executemany(initBooksql,initBookval)
    conn.commit()

    initAddresssql = "INSERT INTO Address VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (addressID) DO NOTHING"
    initAddressval = [
    (10001, "street1", "city1", "province1", "postal_code1", "country1"),
    (10002, "street2", "city2", "province2", "postal_code2", "country2")
    ]
    mycursor.executemany(initAddresssql,initAddressval)
    conn.commit()

    initPublishersql = "INSERT INTO Publisher VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (publisherID) DO NOTHING"
    initPublisherval = [
    (90001, "Publisher1", "publisher1@ojangole.com", 1234567891, 8574638, 10001),
    (90002, "Publisher2", "publisher2@ojangole.com", 1388998383, 9038373, 10002)
    ]
    mycursor.executemany(initPublishersql,initPublisherval)
    conn.commit()

    initPsql = "INSERT INTO Publishes VALUES (%s, %s, %s) ON CONFLICT (isbn,publisherID) DO NOTHING"
    initPval = [
    (9000000000001,90001, 10),
    (9000000000002,90002, 10),
    (9000000000003,90001, 20),
    (9000000000004,90002, 20)
    ] 
    mycursor.executemany(initPsql,initPval)
    conn.commit()
    # Displaying menu (owner or user)
    input1 = input("Who are you? \n Enter 0 if you are the owner: \n Enter anything else if you are a user: ")
    
    if input1 == "0":
        #owner
        # register owner
        registerOwner()
        print("\nYou've been registered! Please remember your username and password.")

        # owner actions
        print("\nHello Owner, what would you like to do today?")
        ownerInput3 = input("Enter a corresponding number.\n 1. Add a book \n 2. Remove a book \n 3. Generate Report \n Input: ")

        if ownerInput3=="1":
            print("\nAdding book.")
            if authenticateOwner():
                addBook()
                print("\nAdd Successful")
        elif ownerInput3 == "2":
            print("\nRemoving Book.")
            if authenticateOwner():
                removeBook()
                print("\nRemove Successfull")
        elif ownerInput3 =="3":
            print("\nGenerating Report.")
            if authenticateOwner():
                generateReport()
                print("\nGeneration of report successful")
        
        print("\nExiting the Owner program. Hasta La Vista Baby!")
    else:
        print("\nWelcome To the book store")
        #user
        #registering user
        registerUser()
        #browsing books
        browseBooks()
        #buy book
        buyBook()
        print("\nExiting the User program. Hasta La Vista Baby!")


if __name__ == "__main__":
    main()