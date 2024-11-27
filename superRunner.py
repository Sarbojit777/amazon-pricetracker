
import time
import os
import threading
from input import input_user
from new import run

def are_files_empty():
    return (not os.path.exists("products.txt") or os.stat("products.txt").st_size == 0) and \
           (not os.path.exists("user_input.txt") or os.stat("user_input.txt").st_size == 0)

# Function to run Check prices periodically every 2 hours
def run_periodically():
    while True:
        # Wait for 2 hours before checking prices again
        time.sleep(2 * 60 * 60)  # 2 hours in seconds
        
        
        # time.sleep(10)  # 10 secs
        
        # Check if both files are empty, then stop the process
        if are_files_empty():
            print("Both 'products.txt' and 'user_input.txt' are empty. Exiting the periodic check...")
            print("Please enter application and add asin")
            break
        
        print("Running 'Check prices'...")
        run()  


def main():

    threading.Thread(target=run_periodically, daemon=True).start()

    while True:
        print("Choose an option:")
        print("1) Enter application")
        print("2) Check prices (runs every 2 hours)")
        print("3) Exit application")
        
        try:
            choicea = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choicea == 1:
            print("Hello, welcome to our app!")
            print("Choices\n1) Enter ASIN\n2) Check prices\n3) Exit\n")

            while True:
                try:
                    choice = int(input())
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                
                if choice == 1:  # allow user to enter asin manually
                    input_user()  
                    run()  
                    break

                elif choice == 2:
                    print("Check prices option is running every 2 hours automatically.")
                    
                    run()  # Here to run() manually if user wants to check prices 
                elif choice == 3:
                    print("Exiting app...")
                    return  
                else:
                    print("Invalid choice. Please try again.")
            
        elif choicea == 2:
            print("You chose to check prices, but it's being handled automatically every 2 hours.")
        elif choicea == 3:
            print("Exiting application...")
            break 
        else:
            print("Invalid choice. Please try again.")
        

        if are_files_empty():
            print("Both 'products.txt' and 'user_input.txt' are empty. Exiting the application...")
            break  

if __name__ == "__main__":
    main()

    