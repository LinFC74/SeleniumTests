from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import unittest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def test_login(self):
        #Extraer el nombre de los items del form
        username = self.driver.find_element(By.NAME, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.NAME, "login-button")

        #Ingresar datos
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login-button"))
        ).click()

        #Validacion
        #dashboard = self.driver.find_element(By.CSS_SELECTOR, ".app_logo")
        #self.assertEqual(dashboard.text, "Swag Labs")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
        )



    def tearDown(self):
        self.driver.quit()
        print ("Test finalizado")

if __name__ == "__main__":
    unittest.main()