import mysql.connector
def get_data():
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="qwer")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM todolist")
    result=mycursor.fetchall()
    mydb.close()
    return result