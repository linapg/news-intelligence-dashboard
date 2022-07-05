# import modules to adress environment variables
import dotenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
print('.env file found and working')
import os





# Import the Python packages for get_data() function

import psycopg2
import pandas as pd


# Insert the get_data() function definition below

# Copy get_data() and implement read_sql_query()

def get_data(sql_query):  #query is a string
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # create a connection to the PostgreSQL server
        conn = psycopg2.connect(host=os.getenv('host'), port=os.getenv('port'),
                        database=os.getenv('database'),
                        options='-c search_path='+os.getenv('schema'), 
                        user=os.getenv('user'),
                        password=os.getenv('password'))
        #asigning read_sql function
        data_frame = pd.read_sql_query(sql_query, conn)
        # close the connection to the PostgreSQL database
        conn.close()
        return data_frame

    # the code below makes the function more robust, you can ignore this part
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# sqlalchemy engine for writing data to a database

from sqlalchemy import create_engine

engine = create_engine(f'postgresql+psycopg2://{os.getenv("user")}:{os.getenv("password")}@{os.getenv("host")}:{os.getenv("port")}/{os.getenv("database")}',  
connect_args={'options': '-csearch_path={}'.format(os.getenv("schema"))})