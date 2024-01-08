import sqlite3
import pandas as pd


def insert_db(pandas_df, connection):

    # Inserting data using to_sql() function of pandas
    print(pandas_df)
    pandas_df.to_sql('Weather', connection, if_exists='append', index=True)
    print("Uploaded to database!")


    # The below code uses manual query to insert the data into the database
    # cursor = connection.cursor()
    # # Insert data into the table
    # for index, row in pandas_df.iterrows():
    #     cursor.execute(f'''
    #         INSERT INTO Weather (dt, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, name)
    #         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    #     ''', (index, row['temp'], row['temp_min'], row['temp_max'], row['pressure'], row['humidity'], row['wind_speed'], row['wind_deg'], row['name']))

    # connection.commit()



if __name__ == "__main__":
    import doctest
    doctest.testmod()