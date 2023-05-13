import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login_and_download_job_description(driver):
    driver.get("http://localhost:8000/login")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("shamjad.nazar.20@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Admin@123")

    password_field.send_keys(Keys.RETURN)

    assert driver.current_url == "http://localhost:8000/studentDash"

    driver.get("http://localhost:8000/viewDrive")

    # Find the "Download" link for the job description
    download_link = driver.find_element(By.XPATH, "//table//a[contains(@href, '.pdf')]")

    # Get the URL of the job description file
    job_description_url = download_link.get_attribute("href")

    # Get the file name from the URL
    file_name = os.path.basename(job_description_url)

    # Click the "Download" link
    download_link.click()

    # Wait for the file to be downloaded
    time.sleep(2)

    # Specify the path where the file should be saved
    download_path = os.path.expanduser("~/Downloads")  # Update the directory path

    # Construct the full file path
    file_path = os.path.join(download_path, file_name)

    # Assert that the file exists in the specified path
    assert os.path.isfile(file_path), f"File '{file_name}' was not downloaded successfully"

    # Assert that the file size is greater than 0
    assert os.path.getsize(file_path) > 0, f"File '{file_name}' is empty or not downloaded correctly"
