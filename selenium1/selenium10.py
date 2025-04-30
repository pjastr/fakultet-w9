from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("http://the-internet.herokuapp.com/dynamic_controls")

    # 1) Remove/Add checkbox
    remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_btn.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!"))
    add_btn = driver.find_element(By.XPATH, "//button[text()='Add']")
    print("Add button displayed:", add_btn.is_displayed())
    add_btn.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's back!"))

    # 2) Enable/Disable pola tekstowego
    enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
    text_input = driver.find_element(By.CSS_SELECTOR, "#input-example input")
    print("Input initially enabled:", text_input.is_enabled())
    enable_btn.click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))
    text_input.send_keys("Test")
    text_input.clear()
    text_input.send_keys("Done")
    print("Input value after:", text_input.get_attribute("value"))

    driver.quit()

if __name__ == "__main__":
    main()
