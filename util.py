

import pymysql

from collections import Counter



def fetcher(list_of_tups, ind):
    return [x[ind] for x in list_of_tups]



def get_conn():
    '''
    Connect to database
    '''
    conn = pymysql.connect(database='final', user='root', password='12345', host='104.154.81.255', port=3306)
   
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
    data for histogram
    '''
    words = panduan(form)
    if words:
        print(words)
        year = words.get('year', '%%')
        type = words.get('type', '%%')
        type = f'%%{type}%%'
        director = words.get('director', '%%')
        actor = words.get('actor', '%%')
        sql = 'select Score from imdbdata where year like %s and type like %s and director like %s and actors like %s"
        res = query(sql, year, type, director, actor)
    else:
        sql = 'select Score from imdbdata'
        res = query(sql)
    data = fetcher(res, 0)
    data.sort()
    return data


def get_2_data(form):  
    '''
    line chart data
    '''
    words = panduan(form)
    if words:
        print(words)
        votemax = words.get('votemax', '2800000')
        votemin = words.get('votemin', '5000')
        scoremax = words.get('scoremax', '10')
        scoremin = words.get('scoremin', '6')
        sql1 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Comedy%%'AND (VOTEs between %s AND %s) and (score between %s and %s)GROUP BY Year'
        sql2 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Drama%%'AND (VOTEs between %s AND %s) and (score between %s and %s) GROUP BY Year'
        sql3 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Horror%%'AND (VOTEs between %s AND %s) and (score between %s and %s) GROUP BY Year'
        sql4 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Action%%'AND (VOTEs between %s AND %s) and (score between %s and %s) GROUP BY Year'
        res1 = query(sql1, votemin, votemax, scoremin, scoremax);
        res2 = query(sql2, votemin, votemax, scoremin, scoremax)
        res3 = query(sql3, votemin, votemax, scoremin, scoremax);
        res4 = query(sql4, votemin, votemax, scoremin, scoremax)
        years = fetcher(res1, 0);
        data1 = fetcher(res1, 1);
        data2 = fetcher(res2, 1);
        data3 = fetcher(res3, 1);
        data4 = fetcher(res4, 1)

    else:
        sql1 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Comedy%%' GROUP BY Year '
        sql2 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Drama%%' GROUP BY Year '
        sql3 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Horror%%' GROUP BY Year '
        sql4 = 'SELECT YEAR,COUNT(*) FROM imdbdata WHERE TYPE LIKE '%%Action%%' GROUP BY Year '
        res1 = query(sql1);
        res2 = query(sql2);
        res3 = query(sql3);
        res4 = query(sql4)
        years = fetcher(res1, 0)
        data1 = fetcher(res1, 1);
        data2 = fetcher(res2, 1);
        data3 = fetcher(res3, 1);
        data4 = fetcher(res4, 1)

    return data1, data2, data3, data4, years 

def get_3_data(form):  
    '''
    piechart data
    '''
    types, c = find_types(form)
    data = [{'value': v, 'name': k} for (k, v) in c.most_common()]
    return types, data


def find_years():  
    sql = 'select year from imdbdata group by Year'
    res = query(sql)
    data = fetcher(res, 0)
    data.sort()
    return data


def find_types(form):  
    if form:
        words = panduan(form)
        if words:
            print(words)
            votemax = words.get('votemax', '2800000')
            votemin = words.get('votemin', '5000')
            scoremax = words.get('scoremax', '10')
            scoremin = words.get('scoremin', '6')
            year = words.get('year', '%%')
            director = words.get('director', '%%')
            actor = words.get('actor', '%%')
            sql = 'select Type from imdbdata where year like %s and (VOTEs between %s AND %s) and (score between %s and %s) and (director like %s) and (actors like %s)'
            res = query(sql, year, votemin, votemax, scoremin, scoremax, director, actor)
        else:
            sql = 'select Type from imdbdata'
            res = query(sql)
    else:
        sql = 'select Type from imdbdata'
        res = query(sql)
    res1 = fetcher(res, 0)
    all = [x for i in res1 for x in i.split(', ')]
    c = Counter()  #count frequency
    text = []
    for x in all:
        if x != '\r\n':
            text.append(x)
            c[x] += 1
    types = list(set(text))
    return types, c


def find_table():  
    '''
    search for movie detail
    '''
    sql = 'select * from imdbdata'
    res = query(sql)
    return res

if __name__ == '__main__':
    # print(get_3_data({'scoremax': '10', 'scoremin': '6', 'votemax': '2800000', 'votemin': '5000', 'year': '1973', 'director': '', 'actor': ''}))
    print(find_table())
