# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

# Load environment variables
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_path = os.path.join(parent_dir, '.venv', '.env')
load_dotenv(env_path)

# Configure Chrome options and initialize WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def login_to_linkedin():
    """Handle LinkedIn login process"""
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    
    username_input = driver.find_element(by="id", value="username")
    password_input = driver.find_element(by="id", value="password")
    
    username_input.send_keys(os.getenv('LINKEDIN_EMAIL'))
    password_input.send_keys(os.getenv('LINKEDIN_PASSWORD'))
    
    sign_in_button = driver.find_element(by="css selector", value="button.btn__primary--large.from__button--floating")
    sign_in_button.click()
    time.sleep(2)

def navigate_to_job_search():
    """Navigate to job search page and minimize chat"""
    driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
    time.sleep(2)
    
    message_overlay = driver.find_element(By.CLASS_NAME, "msg-overlay-bubble-header__details")
    message_overlay.click()
    time.sleep(1)

def save_job():
    """Save the current job listing if not already saved"""
    save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
    save_button_text = save_button.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text.strip()
    
    if save_button_text == "Saved":
        print("Job already saved, skipping...")
    else:
        save_button.click()
        print("Job saved successfully.")
    time.sleep(2)

def follow_company():
    """Follow the company if not already following"""
    follow_button = driver.find_element(By.CSS_SELECTOR, 'button.follow.artdeco-button.artdeco-button--secondary.ml5')
    follow_button_text = follow_button.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text.strip()
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", follow_button)
    time.sleep(2)
    
    if follow_button_text == "Following":
        print("Already following company, skipping...")
    else:
        follow_button.click()
        print("Company followed successfully.")
    time.sleep(2)

# Execute the automation sequence
login_to_linkedin()
navigate_to_job_search()
save_job()
follow_company()