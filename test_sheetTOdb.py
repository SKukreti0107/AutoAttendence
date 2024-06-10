import gspread
from mysql.connector import connect

# Connect to Google Sheets
gc = gspread.service_account(filename='hack-419417-8faf80747eec.json')  # Replace with your credentials file
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Ei9Wh0wC56k1Rqu8hs3WSNKnt7hxtBCH3XYgS9K_COA/edit?usp=sharing')

# Access the first worksheet
worksheet = sheet.get_worksheet(0)

# Connect to MySQL Database
conn = connect(
    host="localhost",
    user="root",
    password="@Ironman0107#",
    database="hack"
)
cursor = conn.cursor()

# Extract data from Google Sheets
data = worksheet.get_all_records()

# Insert data into MySQL
for row in data:
    query = "INSERT INTO students (Reg_no, Name, MAC) VALUES (%s, %s, %s)"
    values = (row['Registration Number'], row['Name'], row['MAC address'])
    cursor.execute(query, values)

# Commit changes and close connection
conn.commit()
conn.close()
