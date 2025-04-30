from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    try:
        driver.get("https://quotes.toscrape.com/")
        # Wszystkie elementy z klasą 'quote'
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for i, q in enumerate(quotes, start=1):
            text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text
            print(f"{i}. {text} — {author}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
