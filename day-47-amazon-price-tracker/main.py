# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, body):
    # Validate input parameters
    if not subject or not body:
        print("Error: Subject and body must not be empty")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        return
        
    # Load environment variables
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)  # Go up one level
    env_path = os.path.join(parent_dir, '.venv', '.env')  # Look in .venv directory
    load_dotenv(env_path)  # Explicitly specify the path

    # Email credentials and settings from environment variables
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    # Validate environment variables
    if not all([sender_email, sender_password, receiver_email]):
        print("Error: Missing email configuration. Check your .env file.")
        print(f"sender_email: {sender_email}")
        print(f"receiver_email: {receiver_email}")
        return

    # Prepare email content
    if isinstance(body, (int, float)):
        body = str(body)
    if isinstance(subject, (int, float)):
        subject = str(subject)
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    # Send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Identify yourself to the server
        server.starttls()  # Start TLS encryption
        server.ehlo()  # Re-identify yourself over TLS connection
        server.login(sender_email, sender_password)  # Login to the server
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to get Amazon price
def get_amazon_price(url):
    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0',
        'Accept-Language': 'en-US'
    }
    
    try:
        # Send GET request to the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Create BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for price element within a-box-inner div
        price_whole_element = soup.find('div', class_='a-box-inner').find('span', class_='a-price-whole')
        price_cent_element = soup.find('div', class_='a-box-inner').find('span', class_='a-price-fraction')
        
        if price_whole_element and price_cent_element:
            # Extract price and clean it
            price = price_whole_element.text.strip() + price_cent_element.text.strip()
            # Remove currency symbol and commas, keep only numbers
            price = re.sub(r'[^\d.]', '', price)
            return float(price)
        else:
            return "Price not found"
            
    except Exception as e:
        return f"Error: {str(e)}"

def get_amazon_title(url):
    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0',
        'Accept-Language': 'en-US'
    }
    
    try:
        # Send GET request to the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Create BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for product title element
        title_element = soup.find(id="productTitle")
        
        if title_element:
            # Extract title and clean it
            title = title_element.get_text().strip()
            return title
        else:
            return "Title not found"
            
    except Exception as e:
        return f"Error: {str(e)}"

# Main program
# URL of the Amazon product
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
target_price = 100.00  # Set your desired price threshold

# Get the title and price
title = get_amazon_title(url)
price = get_amazon_price(url)
print(f"""
Product title: {title}

Product price: {price}
""")

# Check if price is below threshold and send email if it is
if isinstance(price, float) and price <= target_price:
    subject = "Amazon Price Alert!"
    body = f"The product you're watching has dropped to ${price}!\n\nCheck it out here: {url}"
    send_email(subject, body)