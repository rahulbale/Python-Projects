import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from tkinter import *
import matplotlib.pyplot as plt
from datetime import datetime,date



def get_stock(stockname,filename,time, txt):    # Defining the method to get Current stock and the plot of Past Stock

    period = 1611253800
    val = 86400             # Second in each day

    test = 0

    time_list = []
    time =int(time)
    while (test < time):           #Checks if the test is greater then stop the loop
        period = period - val
        time_list.append(period)          #Appending the retrived values in list
        test += 1
    period1 = time_list[-1]               # Takes the last value from the list as a given time
    period1 = str(period1)

    print(time_list)
    print(period1)


    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    stock_url = "https://in.investing.com/equities/"+stockname+"-historical-data?end_date=1611253800&st_date="+period1+"&interval_sec=weekly&interval_sec=daily"


    r = Request(stock_url, headers=headers)     # Requesting the given url
    htmlcontent = urlopen(r).read()

    page = soup(htmlcontent, "html.parser")


    div = page.find('div',{'class':'last-price-and-wildcard'}).find('bdo').text

    div2 = page.find('div',{'class':'inner-header-top'}).find('h1').text




    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    today = date.today()
    today_date = today.strftime("%B %d, %Y")


    today_price = "Current Stock Price of " + div2 + "is : "+div+\
                    "\nCurrent Date "+today_date+" and Time : "+current_time


    txt.insert(INSERT, today_price)          # Gives Current Stock, Date and Time


    table = page.find('table', {'class': 'common-table medium js-table'})

    column = table.find('thead').find_all('th')

    column_name = [col.text for col in column]         #Column name for the table

    table_rows = table.find('tbody').find_all('tr')

    data = []
    for tr in table_rows:
        td = tr.find_all('td')  #finding all table data from tr of tbody tag and storing in td.
        row = [str(tr.get_text()) for tr in td]  #Converting each rows of td to string (text).
        data.append(row)                #Appending the each value of td (row)


    df = pd.DataFrame(data, columns=column_name)        #Converting all the values into Data Frame

    df.columns = df.columns.str.replace('\n', '')       #Replacing next line of columns
    df = df.replace('\n', '', regex=True)               #Replacing next line for rows


    name = filename+".csv"
    df.to_csv(name)
    data = pd.read_csv(name)

    print(data.head())

    #data.sort_values(['Date'], inplace=True, ascending=True)
    plt.figure(figsize=(6,5))
    plt.grid(True)
    plt.xlabel('Dates')
    plt.ylabel('Close Prices')      #Plot the Close Price of given Stock Company Name
    plt.plot(data['Price'])
    plt.show()






