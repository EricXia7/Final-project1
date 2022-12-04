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
    """scrape the release year as an integer"""
    
    year = ''
    try:
        year= table.find('div',{'class': 'lister-item-content'}).find('span',{'class': 'lister-item-year'}).text.replace('(','').replace(')','')

        return int(year)
    except Exception as e:
        return year


def findtype(table):
    """scrape the genre of movies as strings"""
    
    type = ''
    try:
        type= table.find('span',{'class': "genre"}).text.strip()

        return type
    except Exception as e:
        return type


def findscore(table):
    """scrape the rating score as a float"""
    
    score = ''
    try:
        score= table.find('div',{'class': "inline-block"}).text.strip()

        return float(score)
    except Exception as e:
        return score


def findvotes(table):
    """scrape the number of votes as an integer"""
    
    v = ''
    try:
        v= table.find('span',{'name': "nv"}).text.strip().replace(',','')

        return int(v)
    except Exception as e:
        return v


def finddir(table):
    """scrape the director of movies as a string"""
    
    d = ''
    try:
        tmp= str(table)[str(table).find('Director:'):]
        tmp= tmp[tmp.find('>')+1:]
        d = tmp[:tmp.find('<')]
        return d
    except Exception as e:
        return d


def findstars(table):
    """scrape the actors of movies as strings"""
    
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
