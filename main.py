from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    username = "mobile number or email id"
    password = "password"
    driver = webdriver.Firefox(executable_path=r'C:\Users\ELCOT\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
    driver.get('https://www.facebook.com/')
    print("Opened facebook")

    user = driver.find_element_by_id("email")
    user.clear()
    user.send_keys(username)
    print("username entered")

    passw = driver.find_element_by_id("pass")
    passw.clear()
    passw.send_keys(password)
    print("password entered")

    try:
        #driver.find_element_by_name("login").click()
        element = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.NAME, "login")))
        element.click()
    except NoSuchElementException:
        print("NoSuchElementException")
    except InvalidArgumentException:
        print("InvalidArgumentException")
    print("Done")
    input('Press anything to quit \n')
    driver.quit()
    print("Finished")
