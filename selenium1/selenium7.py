from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://the-internet.herokuapp.com/login")

    # Wyczyść pola, wpisz dane i kliknij Login
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.clear()
    password.clear()
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    print("Login button enabled:", login_button.is_enabled())
    login_button.click()

    # Pobierz i wyświetl treść flash-wiadomości oraz jej klasę
    flash = driver.find_element(By.ID, "flash")
    print("Flash message text:", flash.text.strip())
    print("Flash message class:", flash.get_attribute("class"))

    driver.quit()

if __name__ == "__main__":
    main()
