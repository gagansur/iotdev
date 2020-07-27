import socket
import mysql.connector
from mysql.connector import errorcode
import time

def date_time(): #get unix time 
    secs = float(time.time())
    secs = secs*1000
    return secs

def temp_read(temp_in_bytes): #read temperature
    temperature = float(temp_in_bytes.decode("utf-8"))
    return temperature

def humidity_read(humidity_in_bytes): #read humidity
    humidity = float(humidity_in_bytes.decode("utf-8"))
    return humidity

def connect():
    db = mysql.connector.connect(user="gagansur", passwd="Euchemist@1", host="localhost", db="sensor")
    return db

def insert_record(record_data):
    cur = db.cursor()
    secs = date_time()
    arr = record_data.split()
    temperature = temp_read(arr[4])
    humidity = humidity_read(arr[2])

    sql = ("INSERT INTO dhtsensor (at_time, temperature, humidity) VALUES ('%s',%s,%s)", (secs, float(temperature), float(humidity)))
    
    try:
        print ("Writing to the database...")
        print (sql)
        cur.execute(*sql)
        db.commit()
        print ("Write complete")
    except mysql.connector.Error as err:
        print(err)
        print ("Couldn't write to the table; try again!!")
        db.rollback()
    cur.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('192.168.1.190', 1024))
serv.listen(5)
db = connect()

for i in range(1, 10):
    conn, addr = serv.accept()
    for j in range(1, 12000):
        data = conn.recv(4096)
        print (data)
        insert_record(data)
        conn.send(bytes("Complete processing input stream".encode()))

db.close()
conn.close()

