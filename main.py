import random
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#FOR USING INSTABOT YOU SHOULD DOWNLOAD CHROMEDRIVER AND WRITE PATH TO IT
CHROME_DRIVER_PATH = "/Users/anelsagindykova/PycharmProjects/chromedriver"
SOMEONES_ACCOUNT = ""
#WRITE YOUR USERNAME OR PHONE NUMBER HERE. Example: USERNAME = "myaccount"
USERNAME = ""
#WRITE YOUR PASSWORD HERE. Example: PASSWORD = "MYPASSWORD1234"
PASSWORD = ""
HASHTAGS = ["plants", "cats", "cat", "catlover", "catlife"]
COMMENT = "beautiful"


class InstagramBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        accept_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[1]')
        accept_button.click()
        time.sleep(5)
        username_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_button.send_keys(USERNAME)
        password_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_button.send_keys(PASSWORD)
        time.sleep(5)
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        time.sleep(5)

    def follow_followers(self):
        self.login()
        someones_account = input("Which account do you choose? ")
        self.driver.get(f"https://www.instagram.com/{someones_account}")
        followers_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        time.sleep(3)
        modal = self.driver.find_element(by=By.XPATH, value="//div[@Class='isgrP']")
        for n in range(10):
            all_follow_button = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
            for n in all_follow_button:
                if n.text != "Follow":
                    pass
                else:
                    n.click()
                    time.sleep(3)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def like_hashtags(self):
        self.login()
        for a in range(len(HASHTAGS)):
            self.driver.get(f"https://www.instagram.com/explore/tags/{HASHTAGS[a]}/")
            time.sleep(2)
            first_hashtag_photo_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
            first_hashtag_photo_button.click()
            time.sleep(2)
            for i in range(random.randint(10, 20)):
                try:
                    unlike_button = self.driver.find_element(by=By.XPATH, value="//button/div/*[*[local-name()='svg']/@aria-label='Unlike']/*")
                except Exception:
                    like_button = self.driver.find_element(by=By.XPATH, value="//button/div/*[*[local-name()='svg']/@aria-label='Like']/*")
                    like_button.click()
                    time.sleep(2)

                next_hashtag_photo = self.driver.find_element(by=By.XPATH, value="//button/div/*[*[local-name()='svg']/@aria-label='Next']/*")
                next_hashtag_photo.click()
                time.sleep(2)

    def write_comments(self):
        self.login()
        for a in range(len(HASHTAGS)):
            self.driver.get(f"https://www.instagram.com/explore/tags/{HASHTAGS[a]}/")
            time.sleep(2)
            first_hashtag_photo_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
            first_hashtag_photo_button.click()
            time.sleep(2)
            for i in range(random.randint(10, 20)):
                write_comment = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
                write_comment.click()
                time.sleep(2)
                write_comment.send_keys(COMMENT)
                time.sleep(2)
                post_comment = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button/div')
                post_comment.click()
                next_hashtag_photo = self.driver.find_element(by=By.XPATH, value="//button/div/*[*[local-name()='svg']/@aria-label='Next']/*")
                next_hashtag_photo.click()
                time.sleep(2)

    def unfollow_following(self):
        self.login()
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{USERNAME}")
        time.sleep(2)
        following_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div').click()
        time.sleep(2)
        all_follow_button = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for n in all_follow_button:
            n.click()
            time.sleep(2)
            unfollow_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div/div/div[3]/button[1]")
            unfollow_button.click()
            time.sleep(3)


bot = InstagramBot(CHROME_DRIVER_PATH)

# bot.unfollow_following()
# bot.write_comments()
# bot.like_hashtags()
# bot.follow_followers()
