import sqlite3
import os
import pandas as pd 



conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM schedule")
tasks=cursor.fetchall()
print(tasks)

df = pd.DataFrame()
for x in tasks:
    df2 =pd.DataFrame(list(x)).T
    df = pd.concat([df,df2])
df.to_html('sql-data.html')