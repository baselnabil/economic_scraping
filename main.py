from io import StringIO
import requests
from bs4 import BeautifulSoup
import lxml
import json
import pandas as pd
all_countries_links = []
countries= []
columns_dict={}
temp_group=[]
rows_dict ={}


page1 = requests.get("https://data.un.org/")


def main(page):
    source = page.content
    soup = BeautifulSoup(source, 'lxml')
    all_page = soup.find("div", {"class": "CountryList"}).find_all('a', href=True)
    for link in all_page:
        all_countries_links.append(link['href'])
        countries.append(link.text.strip())


def scrape_country(all_countries_links, countries):

        
    for i , country in enumerate(all_countries_links[:3]):
        rows =[]
        first_table=[]
        columns=[]
        country_name = countries[i]
        country_url = f"https://data.un.org/{country}"
        soup=BeautifulSoup(requests.get(country_url).content,"lxml")
        keys_table = soup.css.select('body tr')
        values_table =soup.css.select("details table")
        for key_table in keys_table:
            key_element=key_table.select_one('td')
            value_first_table= key_table.select_one("body td[align='right']")
            if value_first_table:
                first_table.append((value_first_table.text.strip()))
            if key_element:
                key = key_element.text.strip()
                print(key)
                columns.append(key)
        for value_table in values_table:
 
            value = [value.text.strip() for value in value_table.select("body td[style='text-align:right;']")]
            rows.append(first_table)
            rows.append(value)
            first_table=[]

        rows_dict[country_name]=rows
        columns_dict[country_name] = columns
        rows=[]
        columns=[]


            
## last update :: we changed the data scraping to contain dictionraies so you might have to change the data cleaning 
## it's better to proccess all info as 4 tables one for only names and every info about the country in another 
## be aware that there might be missing vlues in the the data and the indicators can also change so you might wanna put them all together after 
## you collect them not collect them and then clean them
# we have to approaches first we can associate every indicator with it's value (this is going to be hard)
# # or we can have to associate every indicator with the country and then connect it with it's value 
main(page1)
scrape_country(all_countries_links, countries)
# with open('columns.json',"w") as f :
#     json.dump(columns_dict,f,indent=4)
#     print("columns have been updated")
# with open('rows.json',"w") as f :
#     json.dump(rows_dict,f,indent=4)
#     print("rows have been updated")
# with open('countries.json',"w") as f :
#     json.dump(countries,f,indent=4)
# #     print("countries have been updated")
# # print(rows_dict)


