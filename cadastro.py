import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

Options = Options()
opcoes.add_argument("--star-maximized")

url_form = ...

try:
    df = pd.read_excel('dados.xlsx')
except FileNotFoundError:
    print(f'O arquivo Excel não foi encontrado.')
    exit()

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(url_form)
time.sleep(3)

