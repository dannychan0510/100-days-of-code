# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

# Load environment variables
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Go up one level
env_path = os.path.join(parent_dir, '.venv', '.env')  # Look in .venv directory
load_dotenv(env_path)  # Explicitly specify the path

# Configure Chrome options to keep the browser open after script completion
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Configure Chrome options and initialize WebDriver
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Locate sign in button
# Find username input field
username_input = driver.find_element(by="id", value="username")
password_input = driver.find_element(by="id", value="password")

# Enter credentials
username_input.send_keys(os.getenv('LINKEDIN_EMAIL'))
password_input.send_keys(os.getenv('LINKEDIN_PASSWORD'))

# Locate the sign in button
sign_in_button = driver.find_element(by="css selector", value="button.btn__primary--large.from__button--floating")
sign_in_button.click()
time.sleep(2)

# Navigate to the job search page
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(2)

# Locate and click the minimize chat button
minimize_chat_button = driver.find_element(by="id", value="ember113")
minimize_chat_button.click()
time.sleep(1)

# Save job
save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
save_button.click()
print("Job saved successfully.")
time.sleep(2)

# Follow company that posted the listing
follow_button = driver.find_element(By.CSS_SELECTOR, 'button.follow.artdeco-button.artdeco-button--secondary.ml5')
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(follow_button)\
       .pause(2)\
       .move_by_offset(0, -150)\
       .perform()
time.sleep(2)

# Close the message overlay first
message_overlay = driver.find_element(By.CLASS_NAME, "msg-overlay-bubble-header__details")
message_overlay.click()  # This should minimize the chat window

# Wait a moment and then try clicking the follow button
time.sleep(1)
follow_button.click()

print("Company followed successfully.")
time.sleep(2)