from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Define your ProxyEmpire rotating proxy URL
proxy_host = "rotating.proxyempire.io"
proxy_port = "5000"  # Replace with your ProxyEmpire port
proxy_user = "package-10001-country-us"  # Replace with ProxyEmpire username
proxy_pass = "Z69zPkXzsZf58IkP"  # Replace with ProxyEmpire password

# List of sample first and last names for randomization
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Emily", "Eve", "Grace", "Henry"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Hernandez"]

# Function to set up WebDriver with ProxyEmpire rotating proxy
def setup_driver_with_proxy():
    chrome_options = Options()
    
    # Run Chrome in headless mode (optional)
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up the proxy (commented out since you're not using proxy)
    # proxy = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
    # chrome_options.add_argument(f'--proxy-server={proxy}')

    # print(f"Using proxy: {proxy}")
    # Initialize the WebDriver using ChromeDriverManager (using Service to pass executable_path)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Generate random first name, last name, email, and phone number
def generate_random_contact_info():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}{random.randint(1000, 9999)}@gmail.com"
    phone_number = f"{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"
    return first_name, last_name, email, phone_number

# Automate account creation with form filling after navigating to the registration page
def create_account():
    driver = setup_driver_with_proxy()
    wait = WebDriverWait(driver, 20)  # Increased wait time

    try:
        # Step 1: Go to the login page
        driver.get("https://my.stubhub.com/secure/login")
        print("Navigated to the login page.")

        # Step 2: Wait for and click on the link to navigate to the register page
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create account')]")))
        submit_button.click()
        print("Clicked on 'Create account' link.")

        # Step 3: Wait for the registration form elements to load
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Ensure the phone number input is visible (no need to use Select for country code)
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phoneNumber.phoneNumber")))

        # Wait for password field
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Generate randomized contact info
        first_name, last_name, email, phone_number = generate_random_contact_info()

        # Print the randomized data
        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}, Phone Number: {phone_number}")

        # Fill in the form fields with random data
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        country_code_input = driver.find_element(By.ID, "react-select-2-input")
        country_code_input.send_keys("US")  # Type the country code
        # Directly fill in the phone number input field (no country code dropdown needed)
        phone_input.send_keys(phone_number)
        
          # Wait for country code input field to be visible and type "US"
      
        # Password field
        password_input.send_keys("SecurePassword123")

        # Click the submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create account')]")))
        submit_button.click()
        print("Account creation submitted.")

        # Optional: Random delay
        time.sleep(random.randint(1, 5))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the browser session
        driver.quit()
        print("Browser closed.")

# Loop to create multiple accounts
for _ in range(1):  # Adjust the range as needed
    create_account()
    time.sleep(random.randint(5, 15))  # Delay between account creations



