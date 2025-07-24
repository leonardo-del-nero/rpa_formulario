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
    print(f'Excel file not found.')
    exit()

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get(url_forms)
time.sleep(3)

for index, line in df.iterrows():
    try:
        first_name = browser.find_element(By.ID, 'T10u6')
        first_name.send_keys(line['First name'])

        time.sleep(0.3)

        last_name = browser.find_element(By.ID, 'FoQlW')
        last_name.send_keys(line['Last name'])

        time.sleep(0.3)

        email = browser.find_element(By.ID, 'XKiCY')
        email.send_keys(line['Email'])

        time.sleep(0.3)

        company_name = browser.find_element(By.ID, 'J91D6')
        company_name.send_key(line['Company name'])

        time.sleep(0.3)

        role_in_company = browser.find_element(By.Id, 'RLSnx')
        role_in_company.send_keys(line['Role in company'])

        time.sleep(0.3 )

        phone_number = browser.find_element(By.ID, 'QcjX3')
        phone_number.send_keys(line['Phone number'])

        time.sleep(0.3)

        address = browser.find_element(By.Id, 'r4HzH')
        phone_number.send_keys(line['Address'])

        time.sleep(0.3)

    except Exception as e:
        print(f'Unespected error: {e}')
