from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from tqdm import tqdm

chrome_options = webdriver.ChromeOptions()
path_to_chromedriver = r'C:/tmp/chromedriver'
df = pd.DataFrame()
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
driver.get("https://opensea.io/collection/boredapeyachtclub")
_input = WebDriverWait(driver, 20, 1).until(
                         expect.visibility_of_element_located(
                         (By.XPATH, "//input[@placeholder='Search']")))
lista_name = []
lista_link = []
lista_m = (list(range(9800
, 10000,1)))
#lista_m = [1,2]
for i in lista_m:
        try:
                _input.send_keys(i)
                _input.send_keys(Keys.ENTER)
                time.sleep(6)
                _img = driver.find_element(by=By.CLASS_NAME, value='AssetMedia--img')
                lista_link.append(_img.get_attribute("src"))
                lista_name.append(i)
                _input.send_keys(Keys.CONTROL+ "a")
                _input.send_keys(Keys.DELETE)
                df['id'] =  [i]
                df['link'] =  [_img.get_attribute("src")]
                print(_img.get_attribute("src"))
                break
                df.to_csv("E:\Bored\sucess.csv",index=False,mode='a',header=False)
                time.sleep(2) 

        except:
                print("oi")
                df['id'] =  [i]
                df['link'] =  [""]
                df.to_csv("E:\Bored\_Nsucess.csv",index=False,mode='a',header=False)
                _input.send_keys(Keys.CONTROL+ "a")
                _input.send_keys(Keys.DELETE)
                time.sleep(2)
                pass
driver.close()
#print(lista_name)
#print(lista_link)
