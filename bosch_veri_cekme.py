# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:04:52 2021

@author: Deniz
"""
"""


"""
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import pandas as pd
from openpyxl.workbook import Workbook

driver = webdriver.Firefox(executable_path=r'C:\Users\Deniz\Desktop\yazilim\geckodriver.exe')
url = "https://www.bosch-home.com.tr/urun-listesi/json/productlist?pageNumber=1&categoryString=fridgesandfreezers/fridgefreezers/freestandingfridgefreezerswithfreezeratbottom&type=PRODUCT_LIST"
driver.get(url)

page_source = driver.page_source

soup = BeautifulSoup(page_source,'html.parser')
json_data = json.loads(soup.text)
driver.close()



df = pd.DataFrame(columns=("product_name", "product_code", "product_score")) #empty dataframe

for item in json_data["response"]["items"]:

    name = item["headers"][0] + " " + item["headers"][1]
    code = item["sku"]
    score = item["review"]["rating"]
    
    new_data = {'product_name': name, 'product_code':code, 'product_score':score}
    df = df.append(new_data, ignore_index=True)
    

print(df)
df.to_excel("soru2_output.xlsx")
