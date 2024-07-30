import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class ImageScraper:
    def __init__(self, save_path):
        self.save_path = save_path
        self.driver = webdriver.Chrome()
        self.session = requests.Session()
        self._initialize_directory()

    def _initialize_directory(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def fetch_images(self, query, num_images):
        url = f'https://www.google.com/search?q={query}&tbm=isch'
        self.driver.get(url)
        time.sleep(2)
        self._scroll_to_load_images()
        images = self.driver.find_elements(By.CSS_SELECTOR, '.mNsIhb')
        self._download_images(images, query, num_images)

    def _scroll_to_load_images(self):
        SCROLL_PAUSE_TIME = 3
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    self.driver.find_element(By.CLASS_NAME, "mye4qd").click()
                except:
                    break
            last_height = new_height

    def _download_images(self, images, query, num_images):
        count = 0
        for image in images:
            if count >= num_images:
                break
            try:
                self.driver.execute_script("arguments[0].click();", image)
                time.sleep(2)
                img_url = self.driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]').get_attribute('src')
                if self._save_image(img_url, query, count + 1):
                    count += 1
            except Exception as e:
                print(f"Error downloading image {count + 1}: {e}")
                continue

    def _save_image(self, img_url, query, count):
        try:
            response = self.session.get(img_url, timeout=7)
            if response.status_code == 200:
                image_path = os.path.join(self.save_path, f'{query}_{count}.jpg')
                with open(image_path, 'wb') as file:
                    file.write(response.content)
                return True
            else:
                print(f"Failed to download image {count}: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"Timeout occurred while downloading image {count}")
        except Exception as e:
            print(f"Error occurred while downloading image {count}: {e}")
        return False

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    carList = ['BMW series 5', 'BMW i8', 'BMW x6', 'Benz E Class', 'Benz G class', 'Genesis g80', 'Genesis gv80', 'KIA K5', 'MINI cooper', 'KIA morning']
    # idx = 0
    # for car in carList:
    #     query = car
    #     num_images = 1000
    #
    #     save_path = f'/Users/johangmin/Desktop/Dev/AIIA/AFAC/dataset/train/{query}'
    #
    #     scraper = ImageScraper(save_path)
    #     scraper.fetch_images(query, num_images)
    #     scraper.close()

query = 'KIA morning'
num_images = 1000

save_path = f'/Users/johangmin/Desktop/Dev/AIIA/AFAC/dataset/train/{query}'

scraper = ImageScraper(save_path)
scraper.fetch_images(query, num_images)
scraper.close()