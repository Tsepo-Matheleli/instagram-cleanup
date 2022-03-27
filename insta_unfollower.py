from selenium import webdriver
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.wait import WebDriverWait as wait


class instagram_unfollow:
    def __init__(self, username, password):
        self._followers = []
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"drivers/geckodriver")

    def login(self):
        field_username = self.execute_element(by.CSS_SELECTOR, "input[name='username']")
        field_password = self.execute_element(by.CSS_SELECTOR, "input[name='password']")
        field_username.clear()
        field_username.send_keys(self.username)
        field_password.clear()
        field_password.send_keys(self.password)
        self.execute_element(by.CSS_SELECTOR, "button[type = 'submit']", True)

    def get_main_account(self):
        # Removes the not now pop ups that show when login into instagram
        self.execute_element(by.XPATH, "//button[contains(text(), 'Not Now')]", True)
        self.execute_element(by.XPATH, "//button[contains(text(), 'Not Now')]", True)
        self.execute_element(by.XPATH, f"//a[@href = '/{self.username}/']", True)

    def get_main_account_followers(self):
        followers_link_x_path = (
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]"
        )
        self.execute_element(by.XPATH, followers_link_x_path, True)
        # Get list of all the people who are followers
        self.driver.execute_script("window.scrollTo(0,5000);")
        followers_list = self.execute_element(by.CLASS_NAME, "PZuss", False, 60)
        print(followers_list)

    def execute_element(self, method, path, button=False, wait_time=15):
        if button == False:
            return wait(self.driver, wait_time).until(
                condition.element_to_be_clickable((method, path))
            )
        return (
            wait(self.driver, wait_time)
            .until(condition.element_to_be_clickable((method, path)))
            .click()
        )

    def execute_cleanup(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        self.login()
        self.get_main_account()
        self.get_main_account_followers()



