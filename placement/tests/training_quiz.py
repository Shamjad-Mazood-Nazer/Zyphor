import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_attend_quiz(driver):
    # Open the login page
    driver.get("http://localhost:8000/login")

    # Find the email and password fields and enter the login credentials
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("vishnusadas@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Vishnu@123")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Assuming successful login, navigate to the quiz page
    driver.get("http://localhost:8000/quiz")

    # Find all the quiz questions
    questions = driver.find_elements(By.CLASS_NAME, "quiz-question")

    for question in questions:
        # Find the options for the current question
        options = question.find_elements(By.CLASS_NAME, "form-check-input")
        if options:  # Check if options are found
            chosen_option = options[0]  # Select the first option
            chosen_option.click()

    # Submit the quiz form
    submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")  # Update the class name
    submit_button.click()

    # Verify the redirection to the quiz result page
    assert driver.current_url == "http://localhost:8000/quiz"
