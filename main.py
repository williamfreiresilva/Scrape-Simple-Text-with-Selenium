# import webdriver
from selenium import webdriver

# if running in Windows IDE
#service = Service('C\\Users\username\\Downloads\\chromedriver.exe')

# create function for webdriver options
def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  # create webdriver object
  driver = webdriver.Chrome(options=options)

  # if running in Windows IDE instead
  # driver = webdriver.Chrome(service=service, option=option)
  
  # get automated.pythonanywhere.com
  driver.get("http://automated.pythonanywhere.com")
  return driver

def main():
  driver = get_driver()
  # get element
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())