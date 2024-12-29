# Import the Selenium WebDriver
from selenium import webdriver

# Configure Chrome options to keep the browser open after script completion
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Python.org website
driver.get("https://www.python.org")

# Locate event time elements on the page
event_times = driver.find_elements(by="css selector", value=".event-widget time")

# Locate event name elements on the page
event_names = driver.find_elements(by="css selector", value=".event-widget li a")

# Create a dictionary to store event information
events = {}

# Iterate over the events and populate the dictionary
for index in range(len(event_times)):
    events[index] = {
        "time": event_times[index].get_attribute("datetime").split("T")[0],  # Extract the date part
        "name": event_names[index].text
    }

# Print the collected events
print(events)

# Close the browser window
driver.close()
