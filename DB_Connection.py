
   
import mysql.connector

class DB_Connect:
	def __init__(self):
		pass

	def connection(self):
		self.con = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  password="AuntJoy@0329",
		  database="students3"
		)
		return self.con


db = DB_Connect()

con = db.connection()
mycursor = con.cursor()

print(con)