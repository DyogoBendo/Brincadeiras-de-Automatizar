from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
if __name__ == '__main__':

    contacts = ["Nikoly", "Jimenez", "Sarah", "Alan", "Anthonny", "Karin"]
    text = "cara de batata"
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    print("Scan QR Code, And then Enter")
    input()
    print("Logged In")

    for contact in contacts:
        inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
        input_box_search.click()
        time.sleep(1)
        input_box_search.send_keys(contact)
        time.sleep(5)

        print(list(driver.find_elements_by_class_name("matched-text")))
        selected_contact = driver.find_elements_by_class_name("matched-text")[-1]
        selected_contact.click()

        time.sleep(2)

        inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(1)
        # input_box.send_keys(text + Keys.ENTER)
        time.sleep(1)
        driver.refresh()

    driver.close()

