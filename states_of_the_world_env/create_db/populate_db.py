import mysql.connector
from crawler import open_country_page, add_all_countries


def create_connection():
    """
    Create a connection to database
    """
    try:
        # Creating connection object
        global my_connection
        my_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="student",
            database="PythonDatabase"
        )
    except mysql.connector.Error as e:
        print(e)


def insert_bd():
    """
    Parse list of countries and insert dates in database's table
    """
    sql_insert_query = """INSERT INTO Country (Name, Capital, Languages, Government, `Area(km2)`, Population, `Density(/km2)`, Time_Zone)
                                                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """
    list_countries = add_all_countries()
    for index in range(0, len(list_countries)):
        parameters = open_country_page("https://en.wikipedia.org" + list_countries[index])
        cursor = my_connection.cursor()  # Creating an instance which is used to execute the 'SQL' statements
        cursor.execute(sql_insert_query, parameters)
        my_connection.commit()
        print(parameters[0], "was inserted!")


def main():
    create_connection()
    try:
        insert_bd()
    except mysql.connector.Error as e:
        print(e)
    finally:
        if my_connection.is_connected():
            my_connection.close()
            print("MySQL connection is closed!")


if __name__ == "__main__":
    main()
