# to import mysql.connector module
import mysql.connector

# ------------------------------------------------------------
# to establish connection with mysql
dataconnection = mysql.connector.connect(host='localhost',
    user='root',
    password='UtkarshSingh2004@',
    database='studentmanagement'
    )
# ------------------------------------------------------------
# to create a cursor object
cursorobj = dataconnection.cursor()
# ------------------------------------------------------------
# input stdid from the user
stdid = input("Enter the Student ID to delete: ")
# ------------------------------------------------------------
# validate if the stdid exists in the table
check_query = "select * from student where stdid = %s"
cursorobj.execute(check_query, (stdid,))
result = cursorobj.fetchone()

if result is None:
    print("No student found with ID:", stdid)
else:
    # show the record that will be deleted
    print("Record found:", result)
  
 # ------------------------------------------------------------
# writing delete query
delete_query = "delete from student where stdid = %s"
cursorobj.execute(delete_query, (stdid,))

# to commit changes
dataconnection.commit()

# to check data deleted or not
if cursorobj.rowcount > 0:
    print("Data deleted successfully")
else:
    print("Unable to delete data")

# ------------------------------------------------------------
# to close cursor object
cursorobj.close()
# to close connection object
dataconnection.close()
# ------------------------------------------------------------