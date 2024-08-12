from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from error import MainError
import requests
import time

path = r"C:\Users\jabee\Downloads\edgedriver_win64\msedgedriver.exe"

edge_options = Options()
edge_options.add_argument('--headless')

service = Service(executable_path=path)
driver = webdriver.Edge(service=service, options=edge_options)


def processor(img):
    try:
        image = requests.get(img, stream=True)
        temp_file = 'profile2.jpg'
        with open(temp_file, 'wb') as file:
            for chunk in image.iter_content(1024):
                file.write(chunk)
        return True
    except Exception as err:
        raise MainError(400,'Something went wrong. Please try again')


def scrapper(url):
    try:
        driver.get(url)
        time.sleep(3)

        container = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.XPATH, '//*[@class="_aarf"]')))
        img = container.find_element(By.TAG_NAME, 'img')
        src = img.get_attribute('src')
        download = processor(src)

        if download is True:
            return 'Image downloaded. Please Check you Folder'

        return 'Something went wrong. Please try again'

    except Exception as err:
        return 'Something went wrong. Please try again'


def profile_scrapper(url):
    try:
        return scrapper(url)
    except Exception as err:
        return err
