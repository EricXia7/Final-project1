

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




if __name__ == '__main__':
    # print(get_3_data({'scoremax': '10', 'scoremin': '6', 'votemax': '2800000', 'votemin': '5000', 'year': '1973', 'director': '', 'actor': ''}))
    print(find_table())
