# start_chat() function definition.
def start_chat(name, age, rating, status):
    # current status message is initialized to None.
    current_status_message = None

    # validating users details.
    error_message = None # variable for storing error messages.

    if not (age > 12 and age < 50) :
        # invalid age.
        error_message = "Invalid age. Provide correct details."
        print error_message
    else:
        welcome_message = "Authentication complete. Welcome\n Name : " + name + "\nAge: " + str(age) + "\nRating: " + str(rating) + "\nProud to have you onboard"
        print welcome_message

        # displaying menu for user.
        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            result = int(raw_input(menu_choices))

            # validating users input
            if (result == 1):
                # action 1
                pass
            elif (result == 2):
                show_menu = False
            else:
                print "wrong choice try again."