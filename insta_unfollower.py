from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
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
        field_username = self.find_element(by.CSS_SELECTOR, "input[name='username']")
        field_password = self.find_element(by.CSS_SELECTOR, "input[name='password']")
        field_username.clear()
        field_username.send_keys(self.username)
        field_password.clear()
        field_password.send_keys(self.password)
        self.find_element(by.CSS_SELECTOR, "button[type = 'submit']", True)

    def get_my_user_account(self):
        # Removes the not now pop ups that show when login into instagram
        self.find_element(by.XPATH, "//button[contains(text(), 'Not Now')]", True)
        self.find_element(by.XPATH, "//button[contains(text(), 'Not Now')]", True)
        self.find_element(by.XPATH, f"//a[@href = '/{self.username}/']", True)

    def get_people_who_follow_me(self):
        followers_link_x_path = (
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]"
        )
        self.find_element(by.XPATH, followers_link_x_path, True)
        # Get list of all the people who are followers
        self.driver.execute_script("window.scrollTo(0,5000);")
        followers_list = self.find_element(by.CLASS_NAME, "PZuss", False, 60)
        # self.driver.find_element_by_class_name(
        #     "PZuss",
        # )
        print(followers_list)

    def find_element(self, method, path, button=False, wait_time=16):
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
        # FOLLOWERS = "followers"
        # FOLLOWING = "following"
        driver.get("https://www.instagram.com/")
        self.login()
        self.get_my_user_account()
        self.get_people_who_follow_me()


# def get_followers_and_following_links(self, x_path, followers_flag):
#     buttons = self.find_element(by.XPATH, x_path)
#     return [
#         button
#         for button in buttons
#         if followers_flag in button.get_attribute("href")
#     ]

# def perform_action(self, link_to_page):
#     action = ActionChains(self.driver)
#     return action.click(link_to_page).perform()
