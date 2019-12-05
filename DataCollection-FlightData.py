from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import datetime
import csv
from os.path import join as pjoin


def main():
    
    Today = datetime.datetime.now() ## Initialize today's date

    Tomorrow = Today + datetime.timedelta(days=1)
    tomorrowdate = Tomorrow.strftime("%m-%d-%Y")

    tom_month = Tomorrow.strftime("%m") # to be inserted in url

    tom_day = Tomorrow.strftime("%d")
    
    year = Tomorrow.strftime("%y")
    
    ## Web Scraper using Selenium and BeautifulSoup, site is euro.expedia.net. Airlines are AirMalta, Alitalia & AirItaly. Destination is 'Catania Fontanarossa'
    
    driver2 = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver2.implicitly_wait(30)
    driver2.get("https://euro.expedia.net/Flights-Search?trip=oneway&leg1=from%3ALuqa%2C%20Malta%20(MLA)%2Cto%3ACatania%2C%20Italy%20(CTA)%2Cdeparture%3A"+tom_day+"%2F"+tom_month+"%2F"+year+"TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy%2Cmaxhops%3A0&mode=search&origref=euro.expedia.net")
    soup2 = Soup(driver2.page_source, 'lxml')
    expedia_prices = soup2.findAll("span",{"class":"full-bold no-wrap","data-test-id":"listing-price-dollars"})
    airlines = soup2.findAll("span",{"data-test-id":"airline-name"})
    depart_time = soup2.findAll("span",{"data-test-id":"departure-time"})
    arrival_time = soup2.findAll("span",{"data-test-id":"arrival-time"})
    duration = soup2.findAll("span",{"class":"duration-emphasis","data-test-id":"duration"})
    
    filename = "expediadata-"+tom_day+"-"+tom_month+".csv"
    path_to_file = pjoin("/home/joncauchi/Assignment/Part 1/data/", filename)
    f = open(path_to_file,"w")
    writer = csv.writer(f)
    writer.writerow(["Date","Airline", "Price", "DepartTime", "ArrivalTime","Duration"])
    
    Date = tomorrowdate
    
    for i in range(len(expedia_prices)): 
        Airline = airlines[i].text
        Price = expedia_prices[i].text
        Depart = depart_time[i].text
        Arrival = arrival_time[i].text
        Duration = duration[i].text

        writer.writerow([Date, Airline, Price, Depart, Arrival, Duration])
    
    f.close() 
    


    
if __name__ == '__main__':
    main()
