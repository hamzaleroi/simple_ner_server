import mysql.connector
conn = mysql.connector.connect(
   user='user', password='password', host='db', database='logs'
)
cursor = conn.cursor()
sql ='''CREATE TABLE IF NOT EXISTS logs(
   id INT PRIMARY KEY AUTO_INCREMENT,
   request_query TEXT,
   ners TEXT,
   execution_time FLOAT,
   timestamp date
)'''
cursor.execute(sql)
conn.commit()


#Closing the connection
conn.close()