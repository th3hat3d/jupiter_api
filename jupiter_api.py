from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests

def list_classes(user,passw,school_year="current"):
    driver = webdriver.Chrome()

    driver.get("https://login.jupitered.com/login/index.php?89967")
    driver.implicitly_wait(0.5)
    student_name = driver.find_element(value="text_studid1")
    student_name.send_keys(user)
    password = driver.find_element(value="text_password1")
    password.send_keys(passw)
    login_button = driver.find_element(value="loginbtn")
    login_button.click()
    time.sleep(2)
    if school_year != "current":
        driver.execute_script(f'changeschoolyear("89967,{school_year}")')
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    classes = soup.find_all(class_="classnav")
    class_list = ""
    for i in classes:
        class_list += str(BeautifulSoup(str(i), 'html.parser').get_text() + "\n")
    driver.quit()
    return class_list

def get_picture(user,passw):
    driver = webdriver.Chrome()

    driver.get("https://login.jupitered.com/login/index.php?89967")
    driver.implicitly_wait(0.5)
    student_name = driver.find_element(value="text_studid1")
    student_name.send_keys(user)
    password = driver.find_element(value="text_password1")
    password.send_keys(passw)
    login_button = driver.find_element(value="loginbtn")
    login_button.click()
    time.sleep(2)
    driver.execute_script('go("settings")')
    time.sleep(1)
    pic_link = driver.find_element(By.CLASS_NAME, "rad12").get_attribute("src")
    driver.quit()
    return requests.get(pic_link).content

def list_grades(user,passw,school_year="current"):
    driver = webdriver.Chrome()

    driver.get("https://login.jupitered.com/login/index.php?89967")
    driver.implicitly_wait(0.5)
    student_name = driver.find_element(value="text_studid1")
    student_name.send_keys(user)
    password = driver.find_element(value="text_password1")
    password.send_keys(passw)
    login_button = driver.find_element(value="loginbtn")
    login_button.click()
    time.sleep(2)
    if school_year != "current":
        driver.execute_script(f'changeschoolyear("89967,{school_year}")')
    driver.execute_script('go("todo")')
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    l = ""
    for i in soup.find_all(style="padding:8px 20px 9px 20px"):
        if i.get_text().strip().partition(" \xa0")[0] == "":
            l += "N/A\n"
        else:
            l += (i.get_text().strip().partition(" \xa0")[0] + "\n")
    return l
