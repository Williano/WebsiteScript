# Script: WebsiteScript.py
# Description: This Script ask a user for a website's domain name and
#              opens the Web Browser and navigate to the website.
# Programmer: William Kpabitey Kwabla.
# Date: 31.07.17


# Imports the webbrowser module to open the webbrowser and navigate
# to the website.
import webbrowser

def open_webpage(domain):
    '''
    Accepts the domain name from the user and
    open's the website.
    '''
    
    # Declares a variable to store the www
    world_wide_web = "www."

    # Prepends the www with user's domain input.
    url = world_wide_web + domain

    # Creats an object for the webbrowser method.
    website_url = webbrowser.open(url)

    # Opens website.
    print("Opening {} .....".format(url))
    print(website_url)
    

def main():
    '''
     Starts the program.
    '''

    # A variable to control the loop.
    check_again = 'Y' or 'y'
    

    # Checks to see if users wants to open another website.
    while check_again == 'Y' or check_again == 'y':
        # Asks user for number of websites.
        number_of_websites = eval(input("How many websites do you want to open ? : "))

        # Loops through the number of websites.
        for num_of_times in range(number_of_websites):
            # Asks the user for the website's domain name.
            domain_name = input("Enter the domain name of the website(eg: google.com): ")

            # Passes users input to the website function.
            open_webpage(domain_name)

            print() # Displays an empty line.

            # Ask user if he/she wants to open another website.
        check_again = input("Do you want to open another website ? ( Y or y = Yes, N or n = No): ")


#Checks to see if script is runned as main program or is being imported.
if __name__ == "__main__":
    # Calls the main function if the script is runned as main program and
    # not imported.
    main()




    


