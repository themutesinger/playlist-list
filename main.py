import os

from ytparser import ParserYoutube
            

def main():
    
    url = input("URL: ")
    driver_path = os.path.abspath('drivers/geckodriver')
    playlist = ParserYoutube(url, driver_path)
    titles = playlist.get_list()
    for i in titles: print(i)


if __name__ == "__main__":
    main()