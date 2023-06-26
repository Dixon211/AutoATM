from dotenv import load_dotenv
import robin_stocks.robinhood as rs
import os
import requests
import time
import json



def get_top_100():
    top100listOfDicts = rs.get_top_100()
    top_100_data = top100listofDicts.json
    top_100_file_path= "./Top_100.json"
    with open(top_100_file_path, "w+") as file:
        json.dump(top_100_data, file)
        print("updating Top_100.json")
    return(top100listofDicts)




#the staging area
while True: 
#Hooking it up
    load_dotenv()
    robin_user = os.environ.get("robinhood_user")
    robin_pass = os.environ.get("robinhood_pass")
    rs.login(username=robin_user,
             password=robin_pass,
             expiresIn=86400,
             by_sms=True)
    get_top_100()
    timeitself += 1 #(Very poetic)
    print(timeitself)
    