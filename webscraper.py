# start webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Game:
  def __init__(self):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(options=chrome_options)

    self.driver.get("https://play.aidungeon.io/main/newGame") # navigate to the main page

    element_present = EC.presence_of_element_located((By.XPATH, '//*[text()="Prompts"]'))
    WebDriverWait(self.driver, 15).until(element_present)

    prompts_button = self.driver.find_element_by_xpath("//*[text()='Prompts']")
    prompts_button.click() # click the prompts button
  
  def get_starting_options(self):
    options = []

    element_present = EC.presence_of_element_located((By.XPATH, "//*[text()='Pick a setting...']/../*[position()>2]/div[1]/div"))
    WebDriverWait(self.driver, 15).until(element_present)

    numbers = self.driver.find_elements_by_xpath("//*[text()='Pick a setting...']/../*[position()>2]/div[1]/div")
    
    element_present = EC.presence_of_element_located((By.XPATH, "//*[text()='Pick a setting...']/../*[position()>2]/div[2]"))
    WebDriverWait(self.driver, 15).until(element_present)

    option_texts = self.driver.find_elements_by_xpath("//*[text()='Pick a setting...']/../*[position()>2]/div[2]")

    for i in range(0, len(numbers)):
      options.append({
        'number': numbers[i].text,
        'text': option_texts[i].text
      })
    
    return options
  
  def end_game(self):
    self.driver.close()
    return True