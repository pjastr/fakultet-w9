from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
    for idx, cb in enumerate(checkboxes, start=1):
        print(f"Checkbox {idx} displayed:", cb.is_displayed())
        print(f"Checkbox {idx} selected before:", cb.is_selected())

        # Dla 1. zaznacz jeśli nie zaznaczony, dla 2. odznacz jeśli zaznaczony
        if idx == 1 and not cb.is_selected():
            cb.click()
        elif idx == 2 and cb.is_selected():
            cb.click()

        print(f"Checkbox {idx} selected after:", cb.is_selected())

    driver.quit()

if __name__ == "__main__":
    main()
