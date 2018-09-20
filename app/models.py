"""Import flask modules"""
import psycopg2

#connect using psycopg
conn = psycopg2.connect("dbname=drm92ntpe135k user=exhrffnwuhrotl password=df30d489b7f282f538412a484f40f845e17bb6d3f14230582ff378fc293c590a host=ec2-50-17-194-129.compute-1.amazonaws.com")
#Activate connection cursor
cur = conn.cursor()

#create tables
cur.execute('''CREATE TABLE IF NOT EXISTS questions(
    id serial PRIMARY KEY,
    title varchar (50) NOT NULL,
    content varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    username varchar (50) NOT NULL,
    email varchar (100) NOT NULL,
    password varchar (100) NOT NULL,
    password_confirmation varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')

cur.execute('''CREATE TABLE IF NOT EXISTS answers(
    id serial PRIMARY KEY,
    body varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')

cur.execute('''CREATE TABLE IF NOT EXISTS comments(
    id serial PRIMARY KEY,
    body varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')
conn.commit()