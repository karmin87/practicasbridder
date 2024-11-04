import time
import os
import pandas

while True:
    if os.path.exists("files/tempos_today.csv"):
        data = pandas.read_csv("files/tempos_today.csv") 
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)

  
