import mysql.connector

conn=mysql.connector.connect(
    host ='localhost',
    user='root',
    password='',
    database='project_tennis'
)

c=conn.cursor()

def competitor():
    c.execute("select * from competitors")
    data = c.fetchall()
    return data


def sidebar():
    c.execute("SELECT * FROM competitions")
    data=c.fetchall()
    return data


def category():
    c.execute("select * from categories")
    data=c.fetchall()
    return data


def ranking():
    c.execute("select * from competitor_rankings")
    data=c.fetchall()
    return data

def venues():
    c.execute("select * from venues")
    data=c.fetchall()
    return data


def cust1():
    c.execute("SELECT competitors.competitor_id, competitors.name, competitor_rankings.rank FROM competitors JOIN competitor_rankings ON competitors.competitor_id = competitor_rankings.competitor_id ORDER BY competitor_rankings.rank asc LIMIT 3")
    data=c.fetchall()
    return data


def cust2():
    c.execute("SELECT competitors.competitor_id, competitors.name, competitor_rankings.rank FROM competitors JOIN competitor_rankings ON competitors.competitor_id = competitor_rankings.competitor_id ORDER BY competitor_rankings.rank asc LIMIT 5")
    data=c.fetchall()
    return data


def cust3():
    c.execute("SELECT competitors.competitor_id, competitors.name, competitor_rankings.rank FROM competitors JOIN competitor_rankings ON competitors.competitor_id = competitor_rankings.competitor_id ORDER BY competitor_rankings.rank asc LIMIT 10")
    data=c.fetchall()
    return data


def points():
    c.execute("SELECT competitors.name,competitor_rankings.points from competitors JOIN competitor_rankings on competitors.competitor_id=competitor_rankings.competitor_id ORDER by competitor_rankings.points  DESC ")
    data=c.fetchall()
    return data

