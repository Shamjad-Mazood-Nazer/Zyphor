import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    # Configure Chrome options to download files automatically
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": "Downloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
        },
    )

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_payment_module(driver):
    # Perform login and navigate to the payment page
    driver.get("http://localhost:8000/login")
    # Perform login actions using Selenium (fill in email and password fields, submit the form)
    # Find the email and password fields and enter the login credentials
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("vishnusadas@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Vishnu@123")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Redirect to the payment page
    driver.get("http://localhost:8000/payment")

    download_button = driver.find_element(By.CLASS_NAME, "btn-success")
    download_button.click()
    time.sleep(2)
    # Wait for the file to be downloaded (add appropriate wait logic)

    # Verify that the file is downloaded successfully
    downloaded_file_path = "Downloads/"
    assert verify_file_downloaded(downloaded_file_path)

import os


def verify_file_downloaded(downloaded_file_path):
    if os.path.isfile(downloaded_file_path) and os.path.getsize(downloaded_file_path) > 0:
        return True
    else:
        return False
