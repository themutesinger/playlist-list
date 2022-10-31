from ytplaylistparse import YtPlaylist
def main():
    
    url = input("URL: ")
    driver_path = 'drivers/geckodriver'
    playlist = YtPlaylist(url, driver_path)
    titles = playlist.get_list()
    for i in titles: print(i)


if __name__ == "__main__":
    main()