

import pymysql

from collections import Counter



def fetcher(list_of_tups, ind):
    return [x[ind] for x in list_of_tups]



def get_conn():
    '''
    Connect to database
    '''
    conn = pymysql.connect(database="final", user="root", password="12345", host="104.154.81.255", port=3306)
   
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor): 
    if cursor:
        cursor.close()
    if conn:
        conn.close()


 def query(sql, *args):  
    '''
    
    '''
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()  
    close_conn(conn, cursor)
    return res



def try_convert(x):
    '''
    Convert float to int
    '''
    try:
        return int(x)
    except ValueError:
        pass
    try:
        return float(x)
    except ValueError:
        return x



def panduan(form):
    '''
    process conditional data, skip if empty
    '''

    words = {}
    for (k, v) in form.items():
        if v:
            words[k] = try_convert(v)
    return words




def get_1_data(form):  
    '''
    data for line chart
    '''
    words = panduan(form)
    if words:
        print(words)
        year = words.get("year", '%%')
        type = words.get("type", '%%')
        type = f'%%{type}%%'
        director = words.get("director", '%%')
        actor = words.get("actor", '%%')
        sql = "select Score from imdbdata where year like %s and type like %s and director like %s and actors like %s"
        res = query(sql, year, type, director, actor)
    else:
        sql = "select Score from imdbdata"
        res = query(sql)
    data = fetcher(res, 0)
    data.sort()
    return data





if __name__ == '__main__':
    # print(get_3_data({'scoremax': '10', 'scoremin': '6', 'votemax': '2800000', 'votemin': '5000', 'year': '1973', 'director': '', 'actor': ''}))
    print(find_table())
