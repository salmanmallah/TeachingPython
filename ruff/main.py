import mysql.connector as mysql

con = mysql.connect(host='localhost', user='root', password='')
cursor = con.cursor()
drop_query = r"DROP DATABASE pythonkinter2 "
quesry = r"CREATE DATABASE pythonkinter2"
cursor.execute(drop_query)
cursor.execute(quesry)
