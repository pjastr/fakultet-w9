# example1_formy.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("http://formy-project.herokuapp.com/form")

    # 1) FIRST NAME – is_displayed(), clear(), send_keys()
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    print("First name visible:", first_name.is_displayed())
    first_name.clear()
    first_name.send_keys("John")

    # 2) LAST NAME – is_enabled(), clear(), send_keys()
    last_name = driver.find_element(By.ID, "last-name")
    print("Last name enabled:", last_name.is_enabled())
    last_name.clear()
    last_name.send_keys("Doe")

    # 3) JOB TITLE – clear(), send_keys()
    job_title = driver.find_element(By.ID, "job-title")
    job_title.clear()
    job_title.send_keys("QA Engineer")

    # 4) RADIO BUTTON (“College”) – is_selected(), click()
    radio_college = driver.find_element(By.ID, "radio-button-2")
    print("Radio ‘College’ selected before:", radio_college.is_selected())
    radio_college.click()
    print("Radio ‘College’ selected after:", radio_college.is_selected())

    # 5) CHECKBOX (“Male”) – is_selected(), click()
    checkbox_male = driver.find_element(By.ID, "checkbox-1")
    print("Checkbox ‘Male’ selected before:", checkbox_male.is_selected())
    checkbox_male.click()
    print("Checkbox ‘Male’ selected after:", checkbox_male.is_selected())

    # 6) DATE PICKER – send_keys(), get_attribute()
    date_field = driver.find_element(By.ID, "datepicker")
    date_field.clear()
    date_field.send_keys("05/28/2025")
    print("Date value attribute:", date_field.get_attribute("value"))

    # 7) SUBMIT – click()
    submit_btn = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary")
    print("Submit button enabled:", submit_btn.is_enabled())
    submit_btn.click()

    # 8) PO SUBMISJI – pobranie nagłówka i .text
    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    print("Post-submit heading text:", heading.text)

    driver.quit()

if __name__ == "__main__":
    main()
