
# def input_user():
#     email=input("Enter Your Email Id: ")
#     list1=[]
#     while True :
#         asin_no=input("Enter product ASIN which u want to track: ")


#         with open ("products.txt","a") as f:
#             f.write(f"{asin_no}\n")


#         print("Enter price range at which u want to get notified: ")
#         upper_price=int(input("Enter the upper price limit: "))
#         lower_price=int(input("Enter the lower price limit: "))
#         list2=[asin_no,upper_price,lower_price]
#         with open ("user_input.txt","a") as f:
#             f.write(f"{list2}\n")
#         cont=input("Do you want to register another product ?(y/n): ")
#         if cont in ["N","n"]:
#             break
        



import ast

import os



def delete_html_file(asin):  #this function deletes the html file of the product when email is sent for that particular product
    """
    Delete the HTML file corresponding to the given ASIN from the 'data' directory.
    
    :param asin: The Amazon Standard Identification Number (ASIN) of the product.
    """
    file_path = f"data/{asin}.html"
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted HTML file for product {asin}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {str(e)}")
    else:
        print(f"File for product {asin} does not exist.")

def input_user():   #takes input from the user 
    email = input("Enter Your Email Id: ")
    while True:
        asin_no = input("Enter product ASIN which you want to track: ")

        # Save ASIN to products.txt
        with open("products.txt", "a") as f:
            f.write(f"{asin_no}\n")

        # Get price range
        print("Enter price range at which you want to get notified: ")
        upper_price = int(input("Enter the upper price limit: "))
        lower_price = int(input("Enter the lower price limit: "))

        # Format the data
        list2 = [email, asin_no, upper_price, lower_price]

        # Save to user_input.txt
        with open("user_input.txt", "a") as f:
            f.write(f"{list2}\n")

        # Ensure input is either 'y' or 'n'
        while True:
            try:
                cont = input("Do you want to register another product? (y/n): ").lower()
                if cont not in ['y', 'n']:
                    raise ValueError("Input must be 'y' or 'n'.")
                elif cont == 'n':
                    break  # Exit the loop if user chooses 'n'
                else:
                    break  # Continue loop if user chooses 'y'
            except ValueError as e:
                print(e)
        
        if cont == 'n':
            break

def delete_info(user_email, asin_to_delete):            #deletes data in userinput and product.txt file when email is sent 
    # Read user_input.txt and filter out the specific ASIN to delete
    with open("user_input.txt", "r") as f:
        user_data = [ast.literal_eval(line.strip()) for line in f]

    # Filter out the entry that matches both the user email and the ASIN
    updated_user_data = [entry for entry in user_data if not (entry[0] == user_email and entry[1] == asin_to_delete)]

    # Write the updated data back to the file
    with open("user_input.txt", "w") as f:
        for entry in updated_user_data:
            f.write(str(entry) + "\n")

    # Read products.txt and filter out the ASIN to delete
    with open("products.txt", "r") as f:
        products = [line.strip() for line in f]

    updated_products = [product for product in products if product != asin_to_delete]

    # Write the updated products back to the file
    with open("products.txt", "w") as f:
        for product in updated_products:
            f.write(product + "\n")
# input_user()