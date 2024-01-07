import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
 
class FindHelloWorld(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
 
    def test_hello_world(self):
         
        driver = self.driver
 
        driver.get("http://127.0.0.1:8000/blog")

        try:
            element = driver.find_element(By.XPATH, "//*[contains(text(), 'hello world')]")
            print("Text 'Hello World' found on page.")
        except NoSuchElementException:
            print("Text 'Hello World' not found on page.")
 
    # use cleanup after every test
    def tearDown(self):
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main()