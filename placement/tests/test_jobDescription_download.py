import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

    # Click the "Download" link
    download_link.click()

    # Verify that the file is downloaded
    # You can add assertions or further actions here to validate the downloaded file

    # Example: Check if the page redirects to a specific page after downloading the file
    assert driver.current_url == "http://localhost:8000/somepage"
