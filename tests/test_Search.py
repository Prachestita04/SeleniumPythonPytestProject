import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_search_for_a_valid_product():
    # options = Options()
    # options.add_experimental_option("detach", True) #used to remove chrome parent-child relationship behaviour

    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()  # create a child process of chrome when parent close, automatically child process close without mentioning quit()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.set_page_load_timeout(40)
    driver.implicitly_wait(20)
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("hp")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    time.sleep(10)
    driver.quit()
