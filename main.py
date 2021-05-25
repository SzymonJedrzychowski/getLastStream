from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from os import system, name

def clear():
    """Clear the screen""" 
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear')



options = Options()
options.add_argument('--headless')

names = ["scarra", "lilypichu", "yvonnie", "natsumiii", "starsmitten", "kkatamina", "disguisedtoast"]
streams = {}

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
try:

    for j in names:
        driver.get("https://twitchtracker.com/"+j)
        sleep(0.5)
        element = driver.find_element_by_xpath('//*[@id="channel-streams"]/div[1]/a[1]').get_attribute('href')
        driver.get(element)
        sleep(0.5)
        titles = []
        i = 1
        while True:
            try:
                title = [driver.find_element_by_xpath('//*[@id="main-col"]/section[1]/ul/li[{}]/div/span[1]'.format(i)).text, driver.find_element_by_xpath('//*[@id="main-col"]/section[1]/ul/li[{}]/div/span[2]'.format(i)).text]
                i+=1
                titles.append(title)
            except Exception as e:
                break
        streams[j] = titles
    driver.close()

except Exception as e:
    driver.close()

clear()

for i in streams.keys():
    print("{} - https://twitch.tv/{}".format(i, i))
    for j in streams[i]:
        print("   {} - {}".format(j[0], j[1]))
    print()