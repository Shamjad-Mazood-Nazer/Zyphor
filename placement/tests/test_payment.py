import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login_and_payment(driver):
    # Login
    driver.get("http://localhost:8000/login")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("vishnusadas@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Vishnu@123")

    password_field.send_keys(Keys.RETURN)

    assert driver.current_url == "http://localhost:8000/studentDash"

    # Payment
    driver.get("http://localhost:8000/payment")

    # Click on the "Download receipt" button
    download_button = driver.find_element(By.CLASS_NAME, "btn-success")
    download_button.click()

    # Wait for the file to download
    time.sleep(2)  # Increase the sleep duration to 2 seconds

    # Check if the receipt file exists on the Desktop
    receipt_file_path = os.path.expanduser("~/Downloads/payment_receipt (1).pdf")
    assert os.path.isfile(receipt_file_path)
