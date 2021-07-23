"""**SQLITE3**"""



import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully");

conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         DEPARTMENT        CHAR(50),
         MARKS         REAL);''')
print ("Table created successfully");

conn.close()

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,DEPARTMENT,MARKS) \
      VALUES (1, 'Raj', 21, 'CSE', 75.00 )");

conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,DEPARTMENT,MARKS) \
      VALUES (2, 'Anish', 20, 'ISE', 80.00 )");

conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,DEPARTMENT,MARKS) \
      VALUES (3, 'Harsh', 19, 'CSE', 90.00 )");

conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,DEPARTMENT,MARKS) \
      VALUES (4, 'hari', 22, 'EC', 100.00 )");


conn.commit()
print ("Records created successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT ID, NAME, AGE, DEPARTMENT from STUDENT")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("AGE = ", row[2])
   print ("DEPARTMENT = ", row[3], "\n")

print ("Operation done successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("UPDATE STUDENT set DEPARTMENT = 'ISE' where ID = 1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT ID, NAME, AGE, DEPARTMENT from STUDENT")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("AGE = ", row[2])
   print ("DEPARTMENT = ", row[3], "\n")

print ("Operation done successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("DELETE from STUDENT where ID = 1;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT ID, NAME, AGE, DEPARTMENT from STUDENT")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("AGE = ", row[2])
   print ("DEPARTMENT = ", row[3], "\n")

print ("Operation done successfully");
conn.close()

"""**EXAMPLE 2**"""

import sqlite3

conn = sqlite3.connect('customer.db')

print("Opened database successfully");

conn.execute('''CREATE TABLE CUSTOMER7
         (CID INT PRIMARY KEY     NOT NULL,
         CNAME           TEXT    NOT NULL,
         ADDRESS            VARCHAR(50),
         CITY        CHAR(50),POSTALCODE INT,
         COUNTRY VARCHAR(50));''')
print ("Table created successfully");

conn.close()

import sqlite3
 
conn = sqlite3.connect('customer.db')
print ("Opened database successfully");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (211, 'alfred', 'obre', 'berlin', 12209,'germany')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (212, 'ana', 'avda', 'mexico', 05021,'mexico')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (213, 'antonio', 'mataderos', 'mexico', 05023,'mexico')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (214, 'around', 'hanover', 'london', 1,'uk')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (215, 'berglund', 'bergus', 'lule', 95822,'sweden')");
 
 
 
 
 
 
 
conn.commit()
print ("Records created successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY FROM CUSTOMER7 ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5],   "\n")

print ("Operation done successfully");
conn.close()

#1.select the customer list from berlin

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY FROM CUSTOMER7 WHERE CITY='berlin' ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5],   "\n")

print ("Operation done successfully");
conn.close()

#2.select thecustomer list from berlin and london

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY FROM CUSTOMER7 WHERE CITY IN('berlin','london') ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5],   "\n")

print ("Operation done successfully");
conn.close()

#3.select the customers whose name starts with a
import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY FROM CUSTOMER7 WHERE CNAME LIKE 'a%' ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5],   "\n")

print ("Operation done successfully");
conn.close()

#4.Insert thecolumn name price across all the records

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

conn.execute("ALTER TABLE CUSTOMER7 ADD COLUMN AMOUNT INT");
conn.commit()
print ("table altered");

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT * FROM CUSTOMER7  ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")

print ("Operation done successfully");
conn.close()

#5.updating the column amount

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

conn.execute("UPDATE CUSTOMER7 set AMOUNT = 30000 where CID = 211")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
print ("Operation done successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

conn.execute("UPDATE CUSTOMER7 set AMOUNT = 40000 where CID = 212")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
print ("Operation done successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

conn.execute("UPDATE CUSTOMER7 set AMOUNT = 40000 where CID = 213")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
print ("Operation done successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

conn.execute("UPDATE CUSTOMER7 set AMOUNT = 50000 where CID = 214")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
print ("Operation done successfully");
conn.close()

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

conn.execute("UPDATE CUSTOMER7 set AMOUNT = 70000 where CID = 215")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
print ("Operation done successfully");
conn.close()

#6.Displaying after updation

import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT * FROM CUSTOMER7   ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")

print ("Operation done successfully");
conn.close()

#7.ORDER BY AMOUNT DESCING ORDER
import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT * FROM CUSTOMER7 ORDER BY AMOUNT DESC ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")

print ("Operation done successfully");
conn.close()

#8.select the customer with least amount
import sqlite3
 
conn = sqlite3.connect('customer.db')
print ("Opened database successfully");
 
cursor = conn.execute("SELECT *,min(AMOUNT) FROM CUSTOMER7   ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")
 
print ("Operation done successfully");
conn.close()

#9.select the customer with highest amount
import sqlite3
 
conn = sqlite3.connect('customer.db')
print ("Opened database successfully");
 
cursor = conn.execute("SELECT *,max(AMOUNT) FROM CUSTOMER7   ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")
 
print ("Operation done successfully");
conn.close()

#10.USING GROUP BY AHVING CITY COUNT GREATER THAN 1
import sqlite3
 
conn = sqlite3.connect('customer.db')
print ("Opened database successfully");
 
cursor = conn.execute("SELECT *,count(CITY) FROM CUSTOMER7 GROUP BY COUNTRY having count(CITY)>1 ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")
 
print ("Operation done successfully");
conn.close()

#11. inserting extra 5 records
 import sqlite3
 
conn = sqlite3.connect('customer.db')
print ("Opened database successfully");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (221, 'pooja', 'banga', 'berlin', 12209,'germany')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (222, 'poorvi', 'hassan', 'mexico', 05021,'mexico')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (223, 'santhu', 'mysore', 'mexico', 05023,'mexico')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (224, 'kavya', 'manga', 'london', 1,'uk')");
conn.execute("INSERT INTO CUSTOMER7 (CID,CNAME,ADDRESS,CITY,POSTALCODE,COUNTRY) \
      VALUES (225, 'divya', 'mysore', 'lule', 95822,'sweden')");
 
 
 
 
 
 
 
conn.commit()
print ("Records created successfully");
conn.close()

# 12.displaying the inserted records
 import sqlite3
 
conn = sqlite3.connect('customer.db')
print ("Opened database successfully");
 
cursor = conn.execute("SELECT * FROM CUSTOMER7   ")
for row in cursor:
   print ("cID = ", row[0])
   print ("cNAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("CITY = ", row[3])
   print ("POSTALCODE = ", row[4])   
   print ("COUNTRY = ", row[5])
   print("AMOUNT= ",row[6],       "\n")
 
print ("Operation done successfully");
conn.close()

"""**EXAMPLE 3**"""

import sqlite3
 
conn = sqlite3.connect('library.db')
 
print("Opened database successfully");
conn.execute('''CREATE TABLE lib7
         (ISBN INT PRIMARY KEY ,
         TITLE  VARCHAR(50),
         AUTHOR            VARCHAR(20),
         EDITION       INT ,PUBLICATION VARCHAR(50));''')
print ("Table created successfully");
 
conn.close()

import sqlite3
 
conn = sqlite3.connect('library.db')
print ("Opened database successfully");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (1, 'CBOT', 'gunjan verma',  20014,'thakur')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (2, 'comp network', 'saurabh',  2015,'thakur')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (3, 'c#', 'sharadha',  2000,'sunindia')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (4, 'DS', 'vinay',  2018,'k nath')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (5, 'mad', 'ranjan',  2020,'erag')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (6, 'java', 'gayithri',  1997,'thakur')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (7, 'c++', 'gunjan',  2016,'appsin')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (8, 'python', ' verma',  2003,'sapin')");    
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (9, 'cyber', 'randeep',  2001,'randin')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (10, 'angular js', 'alloy',  1999,'santhur')");  
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (11, 'iot', 'gunjan verma',  2004,'thakur')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (12, 'machine', 'santhosh',  2010,'saurav')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (13, 'AI', 'pachur',  2009,'napdil')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (14, 'deep learning', 'loki',  2000,'sunindia')");
conn.execute("INSERT INTO lib7 (ISBN,TITLE,AUTHOR,EDITION,PUBLICATION) \
      VALUES (15, 'DV', 'anadh',  2005,'riken')");

cursor = conn.execute("SELECT * FROM lib7")
for row in cursor:
   print("ISBN = ",row[0])
   print("TITLE = ",row[1])
   print("AUTHOR = ",row[2])
   print("EDITION = ",row[3])
   print("PUBLICATION = ",row[4],"\n")
 
print ("Operation done successfully");

cursor = conn.execute("SELECT * FROM lib7 WHERE title LIKE 'a%' ")
for row in cursor:
   print("ISBN = ",row[0])
   print("TITLE = ",row[1])
   print("AUTHOR = ",row[2])
   print("EDITION = ",row[3])
   print("PUBLICATION = ",row[4],"\n")
 
print ("Operation done successfully");

cursor = conn.execute("SELECT * FROM lib7 WHERE edition>2000 ")
for row in cursor:
   print("ISBN = ",row[0])
   print("TITLE = ",row[1])
   print("AUTHOR = ",row[2])
   print("EDITION = ",row[3])
   print("PUBLICATION = ",row[4],"\n")
 
print ("Operation done successfully");


