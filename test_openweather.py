import time

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://openweathermap.org/"
WRONG_LOGIN = 'error@gmail.com'
WRONG_PASSWORD = 'error'
SING_IN_PAGE = 'https://home.openweathermap.org/users/sign_in'


def test_open_page(driver):
    driver.get(URL)
    driver.maximize_window()
    assert 'weather' in driver.current_url
    print(driver.current_url)

def test_page_title(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    assert driver.title == "Сurrent weather and forecast - OpenWeatherMap"
    print(driver.title)

def test_placeholder_search_city(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']").send_keys('New York')
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    driver.implicitly_wait(7)
    driver.find_element(By.XPATH, "//ul[@class='search-dropdown-menu']/li[1]/span[1]").click()
    expected_city = 'New York City, US'
    displayed_city = driver.find_element(By.XPATH, "//h2[text()='New York City, US']")
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert displayed_city_text == expected_city



# TC – 01 – 01 > Sing In > Unregistered User > wrong login and wrong password
def test_wrong_login_password(driver):
    driver.get(SING_IN_PAGE)
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_email']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element.send_keys(WRONG_LOGIN)
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_password']")
    text = element.get_attribute('placeholder')
    assert text == 'Password'
    element.send_keys(WRONG_PASSWORD)
    cssValue = driver.find_element(By.XPATH, "//input[@value='Submit']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    driver.find_element(By.XPATH, "//div[@class='panel-heading']"), 'NO ALERT'
    driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid Email or password.')]")


# TC – 01 – 02 > Sing In > Unregistered User > recover password
def test_recover_password(driver):
    driver.get(SING_IN_PAGE)
    cssValue = driver.find_element(By.XPATH, "//a[@href='#']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    driver.find_element(By.XPATH, "//a[@href='#']").click()
    element = driver.find_element(By.XPATH, "//input[@class='form-control string email optional']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    driver.find_element(By.XPATH, "//input[@class='form-control string email optional']").send_keys(WRONG_LOGIN)
    cssValue = driver.find_element(By.XPATH, "//input[@value='Send']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element_value(
        (By.XPATH, "//input[@value='Send']"), "Create user"))
    driver.find_element(By.XPATH, "//input[@value='Send']").click()
    assert "users/password" in driver.current_url
    driver.find_element(By.XPATH, "//div[@class='panel-heading']"), 'NO ERROR MESSAGE!'
    driver.find_element(By.XPATH, "// *[contains(text(), 'Email not found')]"), 'NO EMAIL NOT FOUND MESSAGE!'
    driver.find_element(By.XPATH, "//div[@class='sign-form']"), 'NO FORGOT YOUR PASSWORD FORM!'
    driver.find_element(By.XPATH, "//*[contains(text(),'Forgot your password?')]")
    element = driver.find_element(By.ID, "user_email")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element = driver.find_element(By.ID, "user_email")
    text = element.get_attribute('value')
    assert text == WRONG_LOGIN
    driver.find_element(By.XPATH, "//input[@value='Change password']"), 'NO CHANGE PASSWORD BUTTON!'

















