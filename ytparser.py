import time

from bs4 import BeautifulSoup
from selenium import webdriver


class ParserYoutube:

    def __init__(self, url, driver_path):
        self.url = url
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.__get()


    def __get(self):
        try:
            self.driver.get(url=self.url)
            self.driver.maximize_window()
            self.__scroll_page()
            time.sleep(5)
            self.alltitles = self.__get_playlist()

        except Exception as error:
            print(f"ошибка нахуй: {error}")
        finally:
            self.driver.close()
            self.driver.quit()

    def __get_playlist(self):
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        alltitle_tag = soup.findAll(id="video-title")
        alltitles = [i.text.strip() for i in alltitle_tag]
        return alltitles

    def __scroll_page(self):

        while True:

            document_height_before = self.driver.execute_script(
                "return document.documentElement.scrollHeight")
            self.driver.execute_script(
                "window.scrollBy(0,document.documentElement.scrollHeight)")
            time.sleep(1.5)
            document_height_after = self.driver.execute_script(
                "return document.documentElement.scrollHeight")
            if document_height_after == document_height_before:
                break
    
    def get_list(self):
        titles = self.alltitles
        return titles

    def save(result_file_path):

        with open(result_file_path, "w") as txtfile:

            for item in self.alltitle:
                txtfile.write(item.get("title")+'\n')