import re
import sys
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine


def findname(table):
    '''scrape the name as a string'''
    
    name = ''
    try:
        name= table.find('div',{'class': 'lister-item-content'}).a.text
        return name
    except Exception as e:
        return name


def findyear(table):
    '''scrape the release year as an integer'''
    
    year = ''
    try:
        year= table.find('div',{'class': 'lister-item-content'}).find('span',{'class': 'lister-item-year'}).text.replace('(','').replace(')','')
        tmp=re.findall('\d+', str(year))[0]
        return int(tmp)
    except Exception as e:
        return year


def findtype(table):
    '''scrape the genre of movies as strings'''
    
    type = ''
    try:
        type= table.find('span',{'class': 'genre'}).text.strip()

        return type
    except Exception as e:
        return type


def findscore(table):
    '''scrape the rating score as a float'''
    
    score = ''
    try:
        score= table.find('div',{'class': 'inline-block'}).text.strip()

        return float(score)
    except Exception as e:
        return score


def findvotes(table):
    '''scrape the number of votes as an integer'''
    
    v = ''
    try:
        v= table.find('span',{'name': 'nv'}).text.strip().replace(',','')

        return int(v)
    except Exception as e:
        return v


def finddir(table):
    '''scrape the director of movies as a string'''
    
    d = ''
    try:
        tmp= str(table)[str(table).find('Director:'):]
        tmp= tmp[tmp.find('>')+1:]
        d = tmp[:tmp.find('<')]
        return d
    except Exception as e:
        return d


def findstars(table):
    '''scrape the actors of movies as strings'''
    
    stars = ''
    try:
        tmp= str(table)[str(table).find('Stars:'):]
        tmp= tmp[:tmp.find('p>')]
        index = tmp.find('>')
        while(index!=-1):
            tmp= tmp[index+1:]
            if(len(stars)>1):
                stars = stars+', '
            star = tmp[:tmp.find('</a>')]
            stars = stars+star
            tmp = tmp[tmp.find('<a '):]
            index =  tmp.find('>')

        return stars
    except Exception as e:
        return stars

def save_to_imdb(data):
    '''save the data into our database'''
    con_string = 'mysql+pymysql://root:12345@104.154.81.255:3306/final'
    engine = create_engine(con_string)
    conn = engine.connect()
    data.to_sql(name='imdbdata', con=conn, if_exists='replace')


def crawl_imdb_data():
    '''scrape the information of movies that satisfy the condition from imdb'''
    data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    for i in range(91):
        url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=1970-01-01,2022-11-01&user_rating=7.0,&num_votes=5000,&start='+str(1+i*50)+'&ref_=adv_nxt'
        try:
            response = requests.get(url, headers=headers)
            print('page'+str(i+1)+','+str(response.status_code))

            soup = BeautifulSoup(response.text, 'lxml')

            tables = soup.find_all('div', {'class': 'lister-item'})
            for table in tables:
                name = findname(table)
                year = findyear(table)
                type = findtype(table)
                score = findscore(table)
                votes = findvotes(table)
                director = finddir(table)
                stars = findstars(table)


                data.append([name,year,type,score,votes,director,stars])

        except Exception as e:
            continue
            
    return data


if __name__ == '__main__':
    data =  crawl_imdb_data()
    data = pd.DataFrame(data,columns=['Name','Year','Type','Score','Votes','Director','Actors'])
    save_to_imdb(data)


