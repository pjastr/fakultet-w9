from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.python.org/")
        # czekamy aż link "About" będzie klikalny i klikamy
        wait = WebDriverWait(driver, 10)
        about = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "About")))
        about.click()

        # czekamy aż na nowej stronie pojawi się dowolny <h1>
        heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Nagłówek sekcji About:", heading.text)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
