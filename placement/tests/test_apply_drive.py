import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login_and_apply_drive(driver):
    driver.get("http://localhost:8000/login")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("shamjad.nazar.20@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Admin@123")

    password_field.send_keys(Keys.RETURN)

    assert driver.current_url == "http://localhost:8000/studentDash"

    driver.get("http://localhost:8000/viewDrive")

    # Click the "btn-primary" button
    btn_primary = driver.find_element(By.CLASS_NAME, "btn-primary")
    btn_primary.click()

    # Wait for the alert to be displayed
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())

    # Get the text of the alert
    alert_message = alert.text

    # Accept the alert
    alert.accept()

    # Perform assertions based on the alert message
    if "Already applied" in alert_message:
        # Extract the applied date from the alert message
        applied_on = alert_message.split("Already applied on ")[1].split("!..")[0]

        # Perform assertions on the applied date or further actions
        # ...

    elif "Successfully Applied" in alert_message:
        # Extract the drive name from the alert message
        drive_name = alert_message.split("Successfully Applied to ")[1].split(" !..")[0]

        # Perform assertions on the drive name or further actions
        # ...

    # Example: Check if the page redirects to a specific page after applying to the drive
    assert driver.current_url == "http://localhost:8000/viewDrive"
