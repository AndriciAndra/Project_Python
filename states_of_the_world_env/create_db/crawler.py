import re
import requests
from bs4 import BeautifulSoup


def add_all_countries():
    """
    Parse a Wikipedia page with a list of all countries in the world to retrieve each country URL
    @return: list of all countries
    """
    response = requests.get(
        url="https://simple.wikipedia.org/wiki/List_of_countries",
    )
    content_page = BeautifulSoup(response.content, 'html.parser')

    all_links = content_page.find(id="mw-content-text").find_all("a")
    list_countries = list()
    for link in all_links:
        if link['href'].find("/wiki/") != -1 \
                and link.text != "sovereign states" \
                and link.text != "List of states with limited recognition" \
                and link.text != "Holy See":
            list_countries.append(link['href'])
            if "Zimbabwe" in link.text:
                break
    return list_countries


def open_country_page(received_url):
    """
    Parse a Wikipedia page by html code
    @param received_url: URL to the country's Wikipedia page
    @return: list of information about country
    """
    global capital, area, population, density, time_zone, government
    response = requests.get(url=received_url)
    page_content = BeautifulSoup(response.content, 'html.parser')

    name = page_content.find(id="firstHeading")

    lines_in_table = page_content.find("table", class_="infobox ib-country vcard")
    if lines_in_table is None:
        lines_in_table = page_content.find("table", class_="infobox ib-pol-div vcard").find_all("tr")
    else:
        lines_in_table = lines_in_table.find_all("tr")

    languages_list = ""
    for line in lines_in_table:
        if "Capital" in line.text:
            capital = line.find_next("a").text
        if "Population" == line.text:
            population = line.find_next("td", class_="infobox-data").text.split("[")[0].strip()
            if "(" in population:
                population = population.split("(")[0]
            aux_population = population.replace(",", "")
            aux_population = re.search(r"\d+", aux_population)[0]
            population = int(aux_population)
        if "Density" in line.text:
            density = line.find_next("td").text.split("(")[0].split("/")[0].strip()
            if "[" in density:
                density = density.split("[")[0]
            aux_density = density.replace(",", "")
            density = float(aux_density)
        if "Area" in line.text and "Area" in line.find_next("a").text:
            area = line.find_next("td").text.split("k")[0].strip()
            if "[" in area:
                area = area.split("[")[0]
            if "–" in area:
                area = area.split("–")[1]
            aux_area = area.replace(",", "")
            aux_area = re.search(r"(\d+\.\d+)|\d+", aux_area)[0]
            area = float(aux_area)
        if ("languages" in line.text or "language" in line.text) and line.find_next("td",class_="infobox-data") is not None:
            languages = line.find_next("td").find_all("a")
            for language in languages:
                if "[" not in language.text and "See full list" not in language.text and "Others" not in language.text:
                    if re.search(r"^[A-Za-z\, ]+", language.text) is not None:
                        language_split = re.search(r"^[A-Za-z\, ]+", language.text)[0]
                        languages_list = languages_list + language_split + ", "
                    else:
                        languages_list = languages_list + language.text + ", "
        if "Government" in line.text:
            government = line.find_next("td").text
            aux_government = government.split("[")
            government = aux_government[0]
        if "Time zone" in line.text:
            time_zone = line.find_next("td").text
            time_zone = re.findall(r"(UTC([-|+|−](\d+)(\.\d+)?)?)", time_zone)[0]
            time_zone = time_zone[0]
            if "−" in time_zone:
                aux_time = time_zone.replace("−", "-")
                time_zone = aux_time
    languages_list = languages_list[:-2]
    parameters = (name.text, capital, languages_list, government, area, population, density, time_zone)
    return parameters
