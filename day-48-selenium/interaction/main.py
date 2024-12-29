# Import the Selenium WebDriver
from selenium import webdriver

# Configure Chrome options to keep the browser open after script completion
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the target website
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Locate the first name input field and enter the first name
first_name_input_box = driver.find_element(by="name", value="fName")
first_name_input_box.send_keys("Danny")

# Locate the last name input field and enter the last name
last_name_input_box = driver.find_element(by="name", value="lName")
last_name_input_box.send_keys("Chan")

# Locate the email input field and enter the email address
email_input_box = driver.find_element(by="name", value="email")
email_input_box.send_keys("dannychan@test.com")

# Locate the submit button and click it to submit the form
submit_button = driver.find_element(by="css selector", value="button.btn.btn-lg.btn-primary.btn-block[type='submit']")
submit_button.click()

# Retrieve the success message displayed after form submission
success_text = driver.find_element(by="class name", value="display-3").text
print(success_text)

# Close the browser window
driver.close()
