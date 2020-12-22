# -*- coding: utf-8 -*-
#Functions for connecting/inserting/fetching from Database
import mysql.connector as mysql
from mysql.connector import errorcode

#Connect do Database
def database_connection_check():
    try:
        db = mysql.connect(
            host="localhost",
            user="admin",
            passwd="datalogger",
            database="IOT_PROTOTYP_TEMP"
        )
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    print(db)
    return(db)
    
#Insert Data to Database
def insert_data_temperatureTable(date,timestamp, sensor_id, temperature, humidity):
    
    #SQL Query
    query = "INSERT INTO sensor_raw_temp(datum,uhrzeit,sensor_id, temperature, humidity) " \
            "VALUES(%s,%s,%s, %s, %s)"
    #Values for SQL Query
    args = (date,timestamp, sensor_id, temperature, humidity)

    #Connection to DB
    try:
        db = database_connection_check()

    #Pointer on db
        cursor = db.cursor()
    #Executing of the SQL command
        cursor.execute(query, args)
        db.commit()
    # Errorhandling
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        db.close()

#Fetch ColumnNames
def retrieve_ColumnNames():
    try:
        db = database_connection_check()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sensor_raw_temp LIMIT 1")
        #get rows, and column Names
        rows = cursor.fetchall()
        ColumnNames = cursor.column_names
        print(ColumnNames)
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        db.close()
        return(ColumnNames)
#Fetch All Data
def retrieve_data_fetchall():
    try:
        db = mysql.connect(
            host="localhost",
            user="admin",
            passwd="datalogger",
            database="IOT_PROTOTYP_TEMP"
        )
        cursor = db.cursor()
# SQL Query for fetching the data
        cursor.execute("SELECT * FROM sensor_raw_temp")
        #get rows, and column Names
        rows = cursor.fetchall()
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        db.close()
        return(rows)

def reihenanzahl(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row
#Retrieve Certain Number of Rows from the Database
def retrieve_last_rows(size):
    try:
        db = mysql.connect(
            host="localhost",
            user="admin",
            passwd="datalogger",
            database="IOT_PROTOTYP_TEMP"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sensor_raw_temp")
        RowList = []
        for row in reihenanzahl(cursor, size):
            RowList.append(row)
    finally:
        cursor.close()
        db.close()
    return(RowList)
        