#to import mysql.connector module
import mysql.connector
#------------------------------------------------------------
#to establish connection with mysql
dataconnection = mysql.connector.connect(host = 'localhost',
	user = 'root',
	password = 'UtkarshSingh2004@',
	database = 'studentmanagement'
	)
#------------------------------------------------------------
# to create a cursor object
cursorobj = dataconnection.cursor()
#------------------------------------------------------------
# writing insert query
sql_query = 'insert into student values (%s,%s,%s,%s)'

#------------------------------------------------------------
stdid ='std101'
stdname = 'Anil'
standard = '10th'
age = 15

stdid ='std102'
stdname = 'Rahul'
standard = '9th'
age = 16

stdid ='std103'
stdname = 'Rohit'
standard = '8th'
age = 17

stdid ='std104'
stdname = 'Kunal'
standard = '11th'
age = 18
#put the values to be inserted inside a tuple
values = (stdid,stdname,standard,age)
#------------------------------------------------------------
#to execute the query
cursorobj.execute(sql_query , values)
#------------------------------------------------------------
#to commit changes
dataconnection.commit()
#------------------------------------------------------------
#to check data inserted or not
if(cursorobj.rowcount  > 0):
	print("Data inserted successfully")
else:
	print("Unable to insert data")
#------------------------------------------------------------
#to close cursur object
cursorobj.close()
#to close connection object
dataconnection.close()
#------------------------------------------------------------
