import psycopg2
from config import Config

conn = psycopg2.connect(
    user="u_name",
    password="p_word",
    host="h_name",
    port="port"
)

cursor = conn.cursor()

rename_table_query = "ALTER TABLE ADDRESS RENAME TO COLOR;"
cursor.execute(rename_table_query)
print("Table renamed successfully")

conn.commit()

cursor.close()
conn.close()

# cursor = conn.cursor()

# create_table_query = '''CREATE TABLE day
#                   (ADDRESS        VARCHAR(50));'''
# cursor.execute(create_table_query)
# print("Table created successfully")

# conn.commit()

# cursor.close
# conn.close()
