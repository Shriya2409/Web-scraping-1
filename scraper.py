from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("D:\chromedriver")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["Proper name", "Distance (ly)", "Mass (M☉)", "Radius (R☉)"]
    star_data=[]
    soup=BeautifulSoup(browser.page_source, "html.parser")
    
    
    for tr_tag in soup.find_all("tr"):
        td_tags=tr_tag.find_all("td")
        temp_list=[]

        for index, td_tag in enumerate(td_tags):

            if index == 0:
                temp_list.append(td_tag.contents[0])
            else:
                temp_list.append("")   

        star_data.append(temp_list)

    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper.csv", "w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)  


scrape()
