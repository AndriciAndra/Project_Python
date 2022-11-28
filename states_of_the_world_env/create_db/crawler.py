import requests
from bs4 import BeautifulSoup


def open_country_page(received_url):
    global capital, area, population, density, time_zone
    response = requests.get(url=received_url)
    page_content = BeautifulSoup(response.content, 'html.parser')

    name = page_content.find(id="firstHeading")

    lines_in_table = page_content.find("table", class_="infobox ib-country vcard").find_all("tr")

    languages_list = ""
    for line in lines_in_table:
        if "Capital" in line.text:
            capital = line.find_next("a").text
        if "Population" == line.text:
            population = line.find_next("td", class_="infobox-data").text.split("[")[0].strip()
            if "(" in population:
                population = population.split("(")[0]
        if "Density" in line.text:
            density = line.find_next("td").text.split("(")[0].split("/")[0].strip()
        if "Area" in line.text:
            area = line.find_next("td").text.split("k")[0].strip()
            if "[" in area:
                area = area.split("[")[0]
        if "languages" in line.text:
            languages = line.find_next("td").find_all("a")
            for language in languages:
                if "[" not in language.text:
                    languages_list = languages_list + language.text + ", "
        if "Time zone" in line.text:
            time_zone = line.find_next("td").text.split(" ")[0]
    languages_list = languages_list[:-2]
    parameters = (name.text, capital, languages_list, area, population, density, time_zone)
    return parameters
