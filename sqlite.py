# Script to extract the required fields from the PSQL and to insert it in SQLITE3 DB.


# Script to create tables in sqlite db. 

import sqlite3
import sys
import psycopg2

def create_connection(db_file):
	""" create a database connection to the SQlite database specified by db_file
	:param db_file: database file
	:return : connection object or None
	"""
	conn = sqlite3.connect(db_file)
	return conn



def create_table(conn, create_table_sql):
	"""create a table from the create_table_Sql statement
	:param conn: connection object
	:param create_table_sql : a CREATE TABLE statement
	:return:
	"""
	c = conn.cursor()
	c.execute(create_table_sql)


# Function to create a table in the SQLite DB.
def main():
	database = "link.db"
	
	sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects(
			 			id  integer PRIMARY KEY,
						name text NOT NULL,
						begin_date text,
						end_date text
					);"""



	sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks(
						id integer PRIMARY KEY,
						name text NOT NULL,
						priority integer, 
						status_id integer NOT NULL,
						project_id integer NOT NULL,
						begin_date text NOT NULL,
						end_date text NOT NULL,
						FOREIGN KEY (project_id) REFERENCES projects(id)
				    );"""




	sql_create_link_table  = """ CREATE TABLE IF NOT EXISTS caller(
						firstname text NULL,  
						lastname text NULL
				    );"""


	
	#create a database connection
	conn = create_connection(database)
	if conn is not None:
	    # Create projects table
	    create_table(conn, sql_create_projects_table)
	    # Create tasks table
            create_table(conn, sql_create_tasks_table)
	    # Create link talbe
	    create_table(conn, sql_create_link_table)
	    print "Table creation is done.!"
	else:

	    print ("Error! cannot create the database connection.")




def extract_sqlite_data():
	""" This function connects to the sqlite db and psql db. 
	    Extract only required columns from the psql table 
            and puts it in sqlite db table."""
	
	# connect a sqlite db.
	sqliteConnection = sqlite3.connect("link.db")
	sqliteCursor = sqliteConnection.cursor()
	# ref: http://hakanu.net/sql/2015/08/25/sqlite-unicode-string-problem/
	sqliteConnection.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')

	# connect to postgresql.
	pgConnectString = "host='localhost' dbname='sqliteconverter' user='postgres' password='kmv!!123'"
	pgConnection=psycopg2.connect(pgConnectString)
	pgCursor = pgConnection.cursor()

	# select from the psql db table.
	pgCursor.execute("SELECT * from company")
	rows = pgCursor.fetchall()

	# loop and insert into sqlite db table.
	for row in rows:
    		sqliteCursor.execute("INSERT INTO caller (firstname,lastname ) VALUES (:firstname,:lastname)", {"firstname": row[0],"lastname":row[1]})
	    	sqliteConnection.commit()


	# close all connections.
	sqliteConnection.close()
	pgConnection.close()
                     



if __name__ == "__main__":
	main()
	extract_sqlite_data()


			



