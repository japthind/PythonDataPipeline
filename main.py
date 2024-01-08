from sqlitedb import create_connection, close_connection
from createDataframe import convert_dict_to_df
from updateDB import insert_db
from etlPipeline import keep_columns, change_col_name, convert_kelvin_to_celsius, set_datetime_col_as_row_index
from fetchWeatherData import fetch_current_weather_data, create_json
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--city_name", default="London")
parser.add_argument("--frequency", default=900, type=int)
args = parser.parse_args()

def start():
    # This creates a connection with the Database
    returned_connection = create_connection()

    #The below line of code fetches the weather data from the API using city name and creates a JSON file
    filename = create_json(fetch_current_weather_data(args.city_name))

    #In the below line of code we are doing some processing of the data before inserting it to the database
    new_df_to_sql = set_datetime_col_as_row_index(convert_kelvin_to_celsius(change_col_name(keep_columns(convert_dict_to_df(filename)))))
    
    # Insert the data into the sqlite db
    insert_db(new_df_to_sql, returned_connection)

    # Close the DB Connection
    close_connection(returned_connection)

while True:
    start()
    time.sleep(args.frequency)