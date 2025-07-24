import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--star-maximized")

url_forms = 'https://rpachallenge.com/'

try:
    df = pd.read_excel('data.xlsx')
except FileNotFoundError:
    print(f'O arquivo Excel não foi encontrado.')
    exit()

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get(url_forms)
time.sleep(3)

