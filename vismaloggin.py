from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import passord
import datetime



def countdown(t):
    for i in range(t):
        sleep(1)
        print(i+1)


def loggin():


    global driver, url, password, username
    start = 0
    fa = 0
    tider, man, tir, ons, tor, fre = [0], [], [], [], [], []
    daynr = 0
    days = [man, tir, ons, tor, fre]
    if start == 0:
        username, password, url = passord.username, passord.password, "Visma url"
        driverpath = Service(r'C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(service=driverpath, options=options)

    driver.get(url)

    countdown(5)
    print("Initialising.")
    button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button.click()
    print("Cookies have been eaten")
    button = driver.find_element(By.ID, "login-with-feide-button")
    button.click()
    countdown(5)
    usernamebox = driver.find_element(By.ID, "username")
    passwordbox = driver.find_element(By.ID, "password")
    usernamebox.send_keys(username)
    passwordbox.send_keys(password)

    button = driver.find_element(By.XPATH, "/html/body/div/article/section[2]/div[1]/form/button")
    button.click()
    print("loggin complete")
    countdown(5)
    src = driver.page_source
    split = src.split("<")
    del src

    for setning in split:
        if "fa-clock" in setning:
            fa = True
        elif fa:
            fa = False
            klokkeslett = setning.split("- ")
            klokkeslett = klokkeslett[1]
            klokkeslett = klokkeslett.replace(":", "")
            if int(tider[-1]) >= int(klokkeslett):
                tider = tider[1:]
                days[daynr].append(tider)
                tider = [0, klokkeslett]
                daynr += 1
            else:
                tider.append(klokkeslett)
    days[daynr].append(tider)
    date = datetime.datetime.now()
    daynr = date.weekday()
    driver.quit()
    return days[daynr]
