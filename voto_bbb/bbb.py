from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':

    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9014")
    driver = webdriver.Chrome(options=options)

    nome = 'Karol Conká'
    titulo = "iframe[title='widget containing checkbox for hCaptcha security challenge']"
    texto_retornar = "Votar Novamente"

    quantidade = 0
    while True:
        quantidade += 1
        time.sleep(3)
        wait = WebDriverWait(driver, 10, poll_frequency=1)

        karois = driver.find_elements_by_xpath(f"//div[text()='{nome}']")

        for karol_conka in karois:
            try:
                karol_conka.click()
            except ElementNotInteractableException:
                pass

        time.sleep(2)

        captcha = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, titulo)))
        captcha.click()

        time.sleep(3)

        retornos = driver.find_elements_by_xpath(f"//button[text()='{texto_retornar}']")
        for retorno in retornos:
            try:
                retorno.click()
            except:
                pass
        print(quantidade)