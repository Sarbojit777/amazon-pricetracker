

# import smtplib
# import ast
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from notifypy import Notify
# import os
# from bs4 import BeautifulSoup
# from datetime import datetime
# from pymongo import MongoClient


# client = MongoClient("mongodb://localhost:27017/")
# db = client["amazon"]
# collection = db["prices"]

# def notify():
#     notification = Notify()
#     notification.title = "Extraction of data"
#     notification.message = "Extracting data from amazon.com"
#     notification.send()

# def get_data():
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode
#     user_agent = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
#     options.add_argument(f"user-agent={user_agent}")

#     with open('products.txt') as f:
#         products = f.readlines()

#     driver = webdriver.Chrome(options=options)

#     for product in products:
#         product = product.strip()  # Remove any leading/trailing whitespace
#         file_path = f'data/{product}.html'
        
#         # If the file already exists, skip creating it (don't fetch the page)
#         if os.path.exists(file_path):
#             print(f"File for product {product} already exists. Skipping extraction...")
#             continue  # Skip this product and move to the next one

#         # Fetch the product page
#         driver.get(f"https://www.amazon.in/dp/{product}")
        
#         try:
#             # Wait until the page is loaded and the title is present (a good indicator that page is loaded)
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'productTitle')))
#             page_source = driver.page_source
            
#             # Check if the page source is empty
#             if not page_source.strip():
#                 print(f"Page source for product {product} is empty. Skipping...")
#                 continue

#             # Save the HTML page source
#             with open(file_path, 'w', encoding="utf-8") as f:
#                 f.write(page_source)
#             print(f"Saved HTML for product {product}")

#         except Exception as e:
#             print(f"Error loading page for product {product}: {str(e)}")
#             continue

# def extract_data():
#     files = os.listdir("data")
#     for file in files:
#         if not file.endswith(".html"):
#             continue  # Skip non-HTML files

#         print(f"Processing file: {file}")
#         with open(f"data/{file}", encoding="utf-8") as f:
#             content = f.read()

#         if not content.strip():
#             print(f"File {file} is empty, skipping...")
#             continue  # Skip empty files

#         soup = BeautifulSoup(content, 'html.parser')
#         title = soup.title.getText().split(":")[0] if soup.title else "No title"
#         time = datetime.now()

#         # Try to find the price
#         price = soup.find(class_="a-offscreen")
#         priceInt = None

#         if price:
#             priceInt = price.getText().replace(".00", "").replace(",", "").replace("₹", "")
#         else:
#             print(f"Price not found for product: {title}")
#             priceInt = "Price not available"

#         # Extract ASIN (Amazon Standard Identification Number)
#         asin = None
#         asin_meta = soup.find("input", {"name": "ASIN"})
#         if asin_meta:
#             asin = asin_meta.get("value")
#         else:
#             asin = "ASIN not found"
        

#         with open("user_input.txt", "r") as f:
#         # Strip newlines and convert each line (which is a string of a list) to an actual list
#             nested_list = [ast.literal_eval(line.strip()) for line in f]

#         # Print the nested list
#         print(nested_list)
#         ul=0
#         ll=0

#         for l in nested_list :
#             if asin == l[0]:
#                 ul=int(l[1])
#                 ll=int(l[2])
#         print(ul,ll)
#         print(priceInt)
#         priceInt = int(priceInt)
#         print("")
#         if priceInt in range(ll,ul+1):
            

#             email = "amazonpricetracking01@gmail.com"
#             receiver_email = "sarbojitdas70@gmail.com"  #user email

#             subject = "Test"
#             message = "Item is in your price range"

#             text = f"subject: {subject} message \n\n{message}"

#             server = smtplib.SMTP("smtp.gmail.com",587)
#             server.starttls()

#             server.login(email,"passw") # will update later
#             server.sendmail(email,receiver_email,text)
#             print("email has beeen sent successfully")
           

#         else:
#             print("working")

        

#         # Print and insert into MongoDB
#         print(priceInt, title, asin, time)
#         collection.insert_one({"priceInt": priceInt, "asin": asin, "title": title, "time": time})

# if __name__ == "__main__":

#     # Uncomment this if you want to get a notification before starting
#     # notify()

#     get_data()
#     extract_data()



































# import smtplib
# import ast
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from notifypy import Notify
# import os
# from bs4 import BeautifulSoup
# from datetime import datetime
# from pymongo import MongoClient
# from input import input_user, delete_info  # Import functions from input.py

# client = MongoClient("mongodb://localhost:27017/")
# db = client["amazon"]
# collection = db["prices"]

# def notify():
#     notification = Notify()
#     notification.title = "Extraction of data"
#     notification.message = "Extracting data from amazon.com"
#     notification.send()

# def check_and_prompt_user():
#     """Checks if products.txt and user_input.txt are empty. If they are, call input_user."""
#     if not os.path.exists("products.txt") or not os.path.getsize("products.txt"):
#         print("products.txt is empty. Please register products.")
#         input_user()
#     elif not os.path.exists("user_input.txt") or not os.path.getsize("user_input.txt"):
#         print("user_input.txt is empty. Please register user inputs.")
#         input_user()

# def get_data():
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode
#     user_agent = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
#     options.add_argument(f"user-agent={user_agent}")

#     with open('products.txt') as f:
#         products = f.readlines()

#     driver = webdriver.Chrome(options=options)

#     for product in products:
#         product = product.strip()  # Remove any leading/trailing whitespace
#         file_path = f'data/{product}.html'
        
#         # If the file already exists, skip creating it (don't fetch the page)
#         if os.path.exists(file_path):
#             print(f"File for product {product} already exists. Skipping extraction...")
#             continue  # Skip this product and move to the next one

#         # Fetch the product page
#         driver.get(f"https://www.amazon.in/dp/{product}")
        
#         try:
#             # Wait until the page is loaded and the title is present (a good indicator that page is loaded)
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'productTitle')))
#             page_source = driver.page_source
            
#             # Check if the page source is empty
#             if not page_source.strip():
#                 print(f"Page source for product {product} is empty. Skipping...")
#                 continue

#             # Save the HTML page source
#             with open(file_path, 'w', encoding="utf-8") as f:
#                 f.write(page_source)
#             print(f"Saved HTML for product {product}")

#         except Exception as e:
#             print(f"Error loading page for product {product}: {str(e)}")
#             continue

# def extract_data():
#     files = os.listdir("data")
#     for file in files:
#         if not file.endswith(".html"):
#             continue  # Skip non-HTML files

#         print(f"Processing file: {file}")
#         with open(f"data/{file}", encoding="utf-8") as f:
#             content = f.read()

#         if not content.strip():
#             print(f"File {file} is empty, skipping...")
#             continue  # Skip empty files

#         soup = BeautifulSoup(content, 'html.parser')
#         title = soup.title.getText().split(":")[0] if soup.title else "No title"
#         time = datetime.now()

#         # Try to find the price
#         price = soup.find(class_="a-offscreen")
#         priceInt = None

#         if price:
#             priceInt = int(price.getText().replace(".00", "").replace(",", "").replace("₹", ""))
#         else:
#             print(f"Price not found for product: {title}")
#             priceInt = None

#         # Extract ASIN (Amazon Standard Identification Number)
#         asin = None
#         asin_meta = soup.find("input", {"name": "ASIN"})
#         if asin_meta:
#             asin = asin_meta.get("value")
#         else:
#             asin = "ASIN not found"

#         # Read user input data
#         with open("user_input.txt", "r") as f:
#             nested_list = [ast.literal_eval(line.strip()) for line in f]

#         ul = 0
#         ll = 0
#         user_email = None

#         for l in nested_list:
#             if asin == l[1]:  # Match ASIN
#                 ul = int(l[2])
#                 ll = int(l[3])
#                 user_email = l[0]
#                 break

#         if priceInt and ll <= priceInt <= ul:
#             print(f"Price is in range for product {title} ({asin}). Sending email...")

#             email = "amazonpricetracking01@gmail.com"
#             receiver_email = user_email

#             subject = "Price Alert!"
#             message = f"The price of {title} ({asin}) is within your range! Current price: ₹{priceInt}."

#             text = f"Subject: {subject}\n\n{message}"

#             try:
#                 server = smtplib.SMTP("smtp.gmail.com", 587)
#                 server.starttls()
#                 server.login(email, "passw")  # Update with the actual password
#                 server.sendmail(email, receiver_email, text)
#                 print("Email has been sent successfully!")

#                 # Call delete_info for the user's email and the ASIN
#                 delete_info(user_email)
#                 print(f"Deleted data for user {user_email} and ASIN {asin}")

#             except Exception as e:
#                 print(f"Failed to send email: {str(e)}")
#             finally:
#                 server.quit()

#         else:
#             print(f"Price for {title} ({asin}) is out of range. Current price: ₹{priceInt}")

#         # Print and insert into MongoDB
#         print(priceInt, title, asin, time)
#         collection.insert_one({"priceInt": priceInt, "asin": asin, "title": title, "time": time})

# if __name__ == "__main__":
#     check_and_prompt_user()  # Ensure data files are populated
#     get_data()
#     extract_data()































# import smtplib
# import ast
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from notifypy import Notify
# import os
# from bs4 import BeautifulSoup
# from datetime import datetime
# from input import input_user, delete_info  # Importing functions from input.py

# def notify():
#     notification = Notify()
#     notification.title = "Extraction of data"
#     notification.message = "Extracting data from amazon.com"
#     notification.send()

# def check_and_input_user():
#     # Check if files are empty
#     if (not os.path.exists("products.txt") or os.stat("products.txt").st_size == 0) and \
#        (not os.path.exists("user_input.txt") or os.stat("user_input.txt").st_size == 0):
#         print("No data found in products.txt or user_input.txt. Running input_user...")
#         input_user()

# def get_data():
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode
#     user_agent = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
#     options.add_argument(f"user-agent={user_agent}")

#     with open('products.txt') as f:
#         products = f.readlines()

#     driver = webdriver.Chrome(options=options)

#     for product in products:
#         product = product.strip()  # Remove any leading/trailing whitespace
#         file_path = f'data/{product}.html'

#         # If the file already exists, skip creating it (don't fetch the page)
#         if os.path.exists(file_path):
#             print(f"File for product {product} already exists. Skipping extraction...")
#             continue  # Skip this product and move to the next one

#         # Fetch the product page
#         driver.get(f"https://www.amazon.in/dp/{product}")

#         try:
#             # Wait until the page is loaded and the title is present (a good indicator that page is loaded)
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'productTitle')))
#             page_source = driver.page_source

#             # Check if the page source is empty
#             if not page_source.strip():
#                 print(f"Page source for product {product} is empty. Skipping...")
#                 continue

#             # Save the HTML page source
#             with open(file_path, 'w', encoding="utf-8") as f:
#                 f.write(page_source)
#             print(f"Saved HTML for product {product}")

#         except Exception as e:
#             print(f"Error loading page for product {product}: {str(e)}")
#             continue

# def extract_data():
#     files = os.listdir("data")
#     for file in files:
#         if not file.endswith(".html"):
#             continue  # Skip non-HTML files

#         print(f"Processing file: {file}")
#         with open(f"data/{file}", encoding="utf-8") as f:
#             content = f.read()

#         if not content.strip():
#             print(f"File {file} is empty, skipping...")
#             continue  # Skip empty files

#         soup = BeautifulSoup(content, 'html.parser')
#         title = soup.title.getText().split(":")[0] if soup.title else "No title"
#         time = datetime.now()

#         # Try to find the price
#         price = soup.find(class_="a-offscreen")
#         priceInt = None

#         if price:
#             priceInt = price.getText().replace(".00", "").replace(",", "").replace("₹", "")
#         else:
#             print(f"Price not found for product: {title}")
#             priceInt = "Price not available"

#         # Extract ASIN (Amazon Standard Identification Number)
#         asin = None
#         asin_meta = soup.find("input", {"name": "ASIN"})
#         if asin_meta:
#             asin = asin_meta.get("value")
#         else:
#             asin = "ASIN not found"

#         with open("user_input.txt", "r") as f:
#             # Strip newlines and convert each line (which is a string of a list) to an actual list
#             nested_list = [ast.literal_eval(line.strip()) for line in f]

#         ul = 0
#         ll = 0

#         for l in nested_list:
#             if asin == l[0]:
#                 ul = int(l[1])
#                 ll = int(l[2])
#         print(ul, ll)
#         print(priceInt)
#         priceInt = int(priceInt)
#         print("")

#         if priceInt in range(ll, ul + 1):
#             print("Price is in the desired range!")

#             # Send email
#             email = "amazonpricetracking01@gmail.com"
#             receiver_email = "sarbojitdas70@gmail.com"  # user email

#             subject = "Price Alert"
#             message = "Item is in your price range"

#             text = f"Subject: {subject}\n\n{message}"

#             server = smtplib.SMTP("smtp.gmail.com", 587)
#             server.starttls()

#             server.login(email, "hykh ccry jhjz mmxf")  # Replace with your actual password
#             server.sendmail(email, receiver_email, text)
#             print("Email has been sent successfully!")

#             # Call delete_info for the matching email and ASIN
#             print(f"Calling delete_info for mail 'sarbojitdas70@gmail.com' and ASIN {asin}")
#             delete_info("sarbojitdas70@gmail.com")

#         else:
#             print("Price is not in the desired range.")

# if __name__ == "__main__":
#     check_and_input_user()  # Check and input user data if necessary
#     get_data()
#     extract_data()
















import smtplib
import ast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from notifypy import Notify
import os
from bs4 import BeautifulSoup
from datetime import datetime
from input import input_user, delete_info  # Importing functions from input.py

def notify():
    notification = Notify()
    notification.title = "Extraction of data"
    notification.message = "Extracting data from amazon.com"
    notification.send()

def check_and_input_user():
    # Check if files are empty
    if (not os.path.exists("products.txt") or os.stat("products.txt").st_size == 0) and \
       (not os.path.exists("user_input.txt") or os.stat("user_input.txt").st_size == 0):
        print("No data found in products.txt or user_input.txt. Running input_user...")
        input_user()

def get_data():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    user_agent = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    with open('products.txt') as f:
        products = f.readlines()

    driver = webdriver.Chrome(options=options)

    for product in products:
        product = product.strip()  # Remove any leading/trailing whitespace
        file_path = f'data/{product}.html'

        # If the file already exists, skip creating it (don't fetch the page)
        if os.path.exists(file_path):
            print(f"File for product {product} already exists. Skipping extraction...")
            continue  # Skip this product and move to the next one

        # Fetch the product page
        driver.get(f"https://www.amazon.in/dp/{product}")

        try:
            # Wait until the page is loaded and the title is present (a good indicator that page is loaded)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'productTitle')))
            page_source = driver.page_source

            # Check if the page source is empty
            if not page_source.strip():
                print(f"Page source for product {product} is empty. Skipping...")
                continue

            # Save the HTML page source
            with open(file_path, 'w', encoding="utf-8") as f:
                f.write(page_source)
            print(f"Saved HTML for product {product}")

        except Exception as e:
            print(f"Error loading page for product {product}: {str(e)}")
            continue
from input import delete_html_file  # Import the function from input.py

def extract_data():
    files = os.listdir("data")
    for file in files:
        if not file.endswith(".html"):
            continue  # Skip non-HTML files

        print(f"Processing file: {file}")
        with open(f"data/{file}", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            print(f"File {file} is empty, skipping...")
            continue  # Skip empty files

        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.getText().split(":")[0] if soup.title else "No title"
        time = datetime.now()

        # Try to find the price
        price = soup.find(class_="a-offscreen")
        priceInt = None

        if price:
            priceInt = price.getText().replace(".00", "").replace(",", "").replace("₹", "")
        else:
            print(f"Price not found for product: {title}")
            priceInt = "Price not available"

        # Extract ASIN (Amazon Standard Identification Number)
        asin = None
        asin_meta = soup.find("input", {"name": "ASIN"})
        if asin_meta:
            asin = asin_meta.get("value")
        else:
            asin = "ASIN not found"

        # Read user_input.txt to find price range and email for the current ASIN
        with open("user_input.txt", "r") as f:
            user_data = [ast.literal_eval(line.strip()) for line in f]

        ul = ll = None
        user_email = None

        # Locate the relevant data for the current ASIN
        for entry in user_data:
            if asin == entry[1]:  # Match ASIN
                user_email = entry[0]  # Extract email
                ul = entry[2]  # Upper limit
                ll = entry[3]  # Lower limit
                break

        if user_email is None:
            print(f"No matching entry found in user_input.txt for ASIN: {asin}")
            continue

        # Ensure priceInt is an integer before proceeding
        try:
            priceInt = int(priceInt)
        except ValueError:
            print(f"Invalid price found for ASIN: {asin}, skipping...")
            continue

        print(f"ASIN: {asin}, Price: {priceInt}, Range: {ll}-{ul}, Email: {user_email}")

        if priceInt in range(ll, ul + 1):
            # Send notification
            email = "amazonpricetracking01@gmail.com"
            receiver_email = user_email  # User's email from user_input.txt

            subject = "Price Alert!"
            # Send email with UTF-8 encoding
            message = f"The item '{title}' is now in your price range.\nhttps://www.amazon.in/dp/{asin}"

            # Convert the message to bytes using UTF-8 encoding
            text = f"Subject: {subject}\n\n{message}"

            # Ensure the text is properly encoded
            text = text.encode('utf-8')

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                print("Running")
                server.login(email, "imhu fihh zzek jain")  # Replace with your password
                server.sendmail(email, receiver_email, text)
                print("Email sent successfully!")

                # Call delete_info to remove the specific ASIN and email data
                delete_info(user_email, asin)

                # Delete the HTML file after sending the email
                delete_html_file(asin)  # Call delete_html_file from input.py


            except Exception as e:
                print(f"Error sending email: {str(e)}")
                delete_info(user_email, asin)

            finally:
                server.quit()

        else:
            print(f"Price for ASIN {asin} is out of range. Current price: {priceInt}")


# if __name__ == "__main__":
#     check_and_input_user()  # Check and input user data if necessary
#     get_data()
#     extract_data()

def run():
    check_and_input_user()  # Check and input user data if necessary
    get_data()
    extract_data()

# run()   #if u want run this file directly just uncomment this run 