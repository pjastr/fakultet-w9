from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, "input")
    print("Input field displayed:", input_field.is_displayed())

    # Wyczyść i wpisz liczbę
    input_field.clear()
    input_field.send_keys("12345")
    print("Input value attribute:", input_field.get_attribute("value"))

    driver.quit()

if __name__ == "__main__":
    main()
