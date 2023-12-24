from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import re
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

def list_teachers(user,passw,school_year="current"):
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
    for i in soup.find_all(class_="hi"):
        driver.execute_script(i['click'])
        html_doc2 = driver.page_source
        soup2 = BeautifulSoup(html_doc2, 'html.parser')
        l += (soup2.find(style="padding:8px 20px 12px 20px").text.split("\n")[2] + "\n")
        driver.execute_script('go("todo")')
    return l

def calculate_gpa(user,passw,school_year="current",mp="current"):
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
    if mp != "current":
        mp = int(mp)
        if mp < 1:
            return "Invalid MP index. Try a number that is 1 or more."
        driver.execute_script("popmenu('datemenu1')")
        dropdown = driver.find_element(By.CLASS_NAME, "menulist")
        elements = dropdown.find_elements(By.XPATH, './/*')
        if mp > len(elements):
            return "MP not present."
        elements[mp-1].click()
    html_doc = driver.page_source
    running_gpa = []
    running_total = 0.0
    a = re.findall(r"gogrades\([0-9]+,[0-9]\)", html_doc)
    for i in a:
        driver.execute_script(i)
        grade_doc = driver.page_source
        soup = BeautifulSoup(grade_doc, 'html.parser')
        first_n = BeautifulSoup(str(soup.find(class_="right pad20")).replace("\xa0", "&nbsp;").replace('pad20"', 'pad20 "'), 'html.parser').get_text().replace("/\xa0", "")
        if first_n == 'None':
            driver.execute_script('go("todo")')
            continue
        numerator = float(first_n)
        index_d = grade_doc.find(str(soup.find(class_="right pad20")).replace("\xa0", "&nbsp;").replace('pad20"', 'pad20 "'))
        start_d_index = grade_doc.find('\n', index_d) + 1 if grade_doc.find('\n', index_d) != -1 else len(grade_doc)
        end_d_index = grade_doc.find('\n', start_d_index)
        d_line = grade_doc[start_d_index:end_d_index]
        denominator = float(BeautifulSoup(d_line, 'html.parser').get_text())
        running_gpa.append(numerator/denominator)
        driver.execute_script('go("todo")')
    for grade in running_gpa:
        running_total += grade
    return str(round((running_total/len(running_gpa))*4, 2))
