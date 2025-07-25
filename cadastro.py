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

buttom_start = browser.find_element(By.XPATH, "//button[text()='Start']")

for index, line in df.iterrows():
    try:
        first_name = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelFirstName']")
        first_name.clear()
        first_name.send_keys(line['First name'])

        time.sleep(0.3)

        last_name = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelLastName']")
        last_name.clear()
        last_name.send_keys(line['Last name'])

        time.sleep(0.3)

        email = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelEmail']")
        email.clear()
        email.send_keys(line['Email'])

        time.sleep(0.3)

        company_name = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelCompanyName']")
        company_name.clear()
        company_name.send_keys(line['Company name'])

        time.sleep(0.3)

        role_in_company = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelRole']")
        role_in_company.clear()
        role_in_company.send_keys(line['Role in company'])

        time.sleep(0.3 )

        phone_number = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelPhone']")
        phone_number.clear()
        phone_number.send_keys(line['Phone number'])

        time.sleep(0.3)

        address = browser.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelAddress']")
        address.clear()
        address.send_keys(line['Address'])

        time.sleep(0.3)

        buttom_submit = browser.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']")
        buttom_submit.click()

        time.sleep(1.5)

    except Exception as e:
        print(f'Unespected error: {e}')
