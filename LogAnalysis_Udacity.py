#!/usr/bin/env python2
import psycopg2
DBNAME = "news"

# function to run all the queries.


def r_e_s_u_l_t_s(query, string):
    d_b = psycopg2.connect(database=DBNAME)
    cr = d_b.cursor()
    cr.execute(query)
    rslt = cr.fetchall()
    for i in rslt:
        print i[0],
        print ' - ',
        print i[1],
        print string
    d_b.close()
    return


# calling function for first query
print "\n\nWhat are the most popular three articles of all time?\n"

# 'q-1 What are the most popular three articles of all time?'
qr1 = """SELECT *
            FROM log_article_vws
            LIMIT 3;"""
r_e_s_u_l_t_s(qr1, 'views')

# calling function for second query
print "\n\nWho are the most popular authors of all time?\n"

# 'q-2 Who are the most popular authors of all time?'
qr2 = """SELECT name, sum(log_article_vws.views) AS authorslogviews
            FROM log_article_auths, log_article_vws
            WHERE log_article_auths.title = log_article_vws.title
            GROUP BY name
            ORDER BY authorslogviews desc;"""
r_e_s_u_l_t_s(qr2, 'views')

# calling function for third query
print "\n\nOn which days did more than 1% of requests lead to errors?\n"

# 'q-3 On which days did more than 1% of requests lead to errors?'
qr3 = """SELECT err_logs.date, round(100.0*Error_Count/Log_Count,2) as logerrorpercent
            FROM l_o_g_s, err_logs
            WHERE l_o_g_s.date = err_logs.date
            AND Error_Count > Log_Count/100;"""
r_e_s_u_l_t_s(qr3, '%')
