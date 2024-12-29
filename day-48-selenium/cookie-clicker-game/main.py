# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure Chrome options and initialize WebDriver
driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_experimental_option("detach", True))
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find key elements on the page
cookie = driver.find_element(by="id", value="cookie")
money_element = driver.find_element(by="id", value="money")

# List of upgrades in order from most to least expensive
UPGRADES = [
    "buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", 
    "buyMine", "buyFactory", "buyGrandma", "buyCursor"
]

def click_cookie(duration=5):
    """Click the cookie continuously for specified duration"""
    end_time = time.time() + duration
    while time.time() < end_time:
        cookie.click()

def get_cookie_count():
    """Get current number of cookies (removes commas from text)"""
    return int(money_element.text.replace(",", ""))

def try_buy_upgrade(upgrade_id):
    """Attempt to buy an upgrade if we have enough cookies"""
    # Find upgrade element and extract its cost
    upgrade = driver.find_element(by="id", value=upgrade_id)
    cost = int(upgrade.find_element("css selector", "b").text.split(" - ")[1].replace(",", ""))
    
    if cost <= get_cookie_count():
        upgrade.click()
        time.sleep(0.03)  # Small delay to let purchase register
        return True
    return False

def game_loop():
    """Main game loop - runs for 5 minutes"""
    end_time = time.time() + 300  # 5 minutes = 300 seconds
    while time.time() < end_time:
        # Click cookie for 5 seconds before checking upgrades
        click_cookie(10)
        
        # Try to buy upgrades in order of most expensive to least
        for upgrade_id in UPGRADES:
            while try_buy_upgrade(upgrade_id):
                pass

# Start the game loop
game_loop()
driver.close()  # Close browser when done