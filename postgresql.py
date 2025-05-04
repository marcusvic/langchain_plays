import psycopg

conn = psycopg.connect(dbname="langchain",
                       user="postgres",
                       host='localhost',
                       password="celular",
                       port=5432)
