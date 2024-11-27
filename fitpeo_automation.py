from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Task 1: Navigate to the FitPeo Homepage
    driver.get("https://fitpeo.com")
    time.sleep(2)
    print("Navigated to the FitPeo homepage successfully.")

    # Task 2: Navigate to the Revenue Calculator Page
    revenue_calculator_link = driver.find_element(By.CSS_SELECTOR, "a[href*='revenue-calculator'] > div.satoshi")
    revenue_calculator_link.click()
    time.sleep(2)
    print("Navigated to the Revenue Calculator Page successfully.")

    # Task 3: Scroll Down to the Slider section
    slider_div = driver.find_element(By.CSS_SELECTOR, ".MuiSlider-rail")
    driver.execute_script("arguments[0].scrollIntoView();", slider_div)
    time.sleep(2)
    print("Slider is now in view.")

    # Task 4: Adjust the Slider to 820
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    current_value = int(slider.get_attribute("value"))
    target_value = 820

    if current_value < target_value:
        steps = target_value - current_value
        for _ in range(steps):
            slider.send_keys(Keys.ARROW_RIGHT)
    elif current_value > target_value:
        steps = current_value - target_value
        for _ in range(steps):
            slider.send_keys(Keys.ARROW_LEFT)

    time.sleep(2)
    updated_value = slider.get_attribute("value")
    if updated_value == "820":
        print("Slider value set to 820 successfully!")
    else:
        print(f"Failed to set slider value. Current value is {updated_value}.")

    # Task 5: Update the Text Field to 560
    text_field = driver.find_element(By.XPATH, '//*[@id=":R57alklff9da:"]')  # Update XPath if needed
    text_field.click()
    time.sleep(1)
    text_field.clear()
    text_field.send_keys("560")
    text_field.send_keys(Keys.ENTER)
    time.sleep(2)
    slider_value = slider.get_attribute("value")
    if slider_value == "560":
        print("Slider value updated to 560 successfully!")
    else:
        print(f"Failed to sync slider value. Current value is {slider_value}.")

    # Task 7: Select CPT checkboxes
    checkboxes = [
        ('//label[span[text()="CPT-99091"]]/span[1]/input'),
        ('//label[span[text()="CPT-99453"]]/span[1]/input'),
        ('//label[span[text()="CPT-99454"]]/span[1]/input'),
        ('//label[span[text()="CPT-99474"]]/span[1]/input'),
    ]
    for checkbox_xpath in checkboxes:
        checkbox = driver.find_element(By.XPATH, checkbox_xpath)
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        checkbox.click()
        time.sleep(1)
    print("All required CPT checkboxes selected successfully.")

    # Task 8: Validate Total Recurring Reimbursement
    total_reimbursement = driver.find_element(By.CSS_SELECTOR, ".total-reimbursement-class")  # Replace with the actual CSS selector
    if total_reimbursement.text == "$110700":
        print("Total Recurring Reimbursement validated successfully.")
    else:
        print(f"Validation failed. Found value: {total_reimbursement.text}")

    # Task 9: Verify Total Recurring Reimbursement Header
    header_text = driver.find_element(By.CSS_SELECTOR, ".reimbursement-header-class")  # Replace with the actual CSS selector
    if header_text.text == "Total Recurring Reimbursement for all Patients Per Month: $110700":
        print("Header validation successful.")
    else:
        print(f"Header validation failed. Found: {header_text.text}")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
