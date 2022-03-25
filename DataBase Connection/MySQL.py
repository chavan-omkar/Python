import mysql.connector

mydb = mysql.connector.connect(host="localhost",user ="####",passwd = "####",database="####")

mycursor = mydb.cursor()

mycursor.execute("select * from dept")
# result = mycursor.fetchall()
result = mycursor.fetchone()
for i in result:
    print(i)