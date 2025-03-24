import mysql.connector


# Replace with your actual details
conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    database="sql12768724",
    user="sql12768724",
    password=" LbPLSsGhUz"
)


cursor = conn.cursor()

# Example: Check connection by fetching tables
cursor.execute("SHOW TABLES")
for table in cursor.fetchall():
    print(table)

conn.close()
