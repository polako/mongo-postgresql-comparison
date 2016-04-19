import psycopg2
def gogo(inicio, fim):
    for i in range(inicio,fim):

        # Connect to an existing database
        conn = psycopg2.connect("dbname=testedb user=teste")

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a command: this creates a new table
        #cur.execute("CREATE TABLE testesc.test (id serial PRIMARY KEY, num integer, data_ varchar);")

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no more SQL injections!)
        cur.execute("INSERT INTO testesc.test (num, data_) VALUES (%s, %s)", (i, "abc"))

        # Query the database and obtain data as Python objects
        cur.execute("SELECT * FROM testesc.test;")
        #result = cur.fetchone()
        result = cur.fetchmany(i)
        # Make the changes to the database persistent
        conn.commit()

        # Close communication with the database
        cur.close()
        conn.close()

        print i
