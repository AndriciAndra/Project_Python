import mysql.connector
import requests
from bs4 import BeautifulSoup
from crawler import open_country_page


def create_connection():
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


def insert_db(sql_insert_query, parameters):
    cursor = my_connection.cursor()  # Creating an instance which is used to execute the 'SQL' statements
    cursor.execute(sql_insert_query, parameters)
    print(parameters[0], "was inserted!")
    my_connection.commit()


def parse_list_of_countries():
    sql_insert_query = """INSERT INTO Country (Name, Capital, Languages, `Area(km2)`, Population, `Density(/km2)`, Time_Zone)
                                                  VALUES (%s, %s, %s, %s, %s, %s, %s); """
    response = requests.get(
        url="https://simple.wikipedia.org/wiki/List_of_countries",
    )
    content_page = BeautifulSoup(response.content, 'html.parser')

    all_links = content_page.find(id="mw-content-text").find_all("a")
    for link in all_links:
        if link['href'].find(
                "/wiki/") != -1 and link.text != "sovereign states" and link.text != "List of states with limited recognition":
            insert_db(sql_insert_query, open_country_page("https://en.wikipedia.org" + link['href']))


def populate():
    create_connection()
    try:
        parse_list_of_countries()
    except mysql.connector.Error as e:
        print(e)
    finally:
        if my_connection.is_connected():
            my_connection.close()
            print("MySQL connection is closed!")


if __name__ == "__main__":
    populate()
