import sqlite3
import csv      

def dbToCsv(aDbFileName,excuteName):
# Connect to the database file
    conn = sqlite3.connect('aDbFileName.db')
    cursor = conn.cursor()

# Execute a SELECT statement to retrieve data from the database
    cursor.execute('SELECT * FROM excuteName')

# Write the results to a CSV file
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)

    # Write the header row
        writer.writerow([i[0] for i in cursor.description])

    # Write the data rows
        writer.writerows(cursor.fetchall())

# Close the cursor and database connection
    cursor.close()
    conn.close()
    return 
dbToCsv(schedule,schedule)