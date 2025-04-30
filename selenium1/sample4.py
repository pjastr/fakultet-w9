from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # (opcjonalnie) otwieramy okno maksymalizowane,
    # żeby nic nie przykrywało elementów
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://en.wikipedia.org/")

        wait = WebDriverWait(driver, 10)
        # czekamy, aż pole wyszukiwania będzie widoczne
        search = wait.until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        # wpisujemy zapytanie i naciskamy ENTER
        search.send_keys("Selenium (software)", Keys.RETURN)

        # czekamy, aż nagłówek strony (h1#firstHeading) się pojawi
        heading = wait.until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        print("Strona:", heading.text)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
