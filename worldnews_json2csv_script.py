import json
import time, datetime
import pandas as pd
import os

def time_to_int(time_str):
    hh, mm , ss = map(int, time_str.split(':'))
    return ss + 60*(mm + 60*hh)

def create_worldnews_csv():
    df = pd.DataFrame()
    dates = []
    titles = []
    times = []
    with open("d:\git\project1\worldnews.json", "r", encoding='utf-8') as read_file:
        i = 0
        for line in read_file:
            #i+=1
            #if (i == 10): break
            data = json.loads(line)
            datetime_string = data['Item']['created']['S']
            date_timestamp = int(time.mktime(datetime.datetime.strptime(datetime_string.split()[0], "%Y-%m-%d").timetuple()))
            time_int = time_to_int(datetime_string.split()[1])
            title = data['Item']['title']['S']
            #print(datetime_string)
            #print(datetime_timestamp)s
            #print(title)
            dates.append(date_timestamp)
            times.append(time_int)
            titles.append(title)
            
    df['date'] = dates
    df['time'] = times
    df['title'] = titles
    #print (df)
    df.to_csv('d:\git\project1\datetime_news.csv', index = False)


def add_column_change(period):
    change = []
    print(df.shape[0])

    for i in range(df.shape[0]):
        #if i > 10: break;
        if (i >= period):
            change.append(df.Open[i] - df.Open[i-period])
        else:
            change.append(0)

#df = pd.read_csv("d:\git\project1\datetime_news.csv")
#print(df)