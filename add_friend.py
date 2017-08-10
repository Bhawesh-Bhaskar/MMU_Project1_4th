# import statements.
from globals import friends_name, friends_age, friends_rating, friends_is_online

# add new friends.
def add_friend():
    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    # concatination.
    new_name = new_name + " " + new_salutation

    new_age = int(raw_input("Age? "))

    new_rating = float(raw_input("Spy rating? "))

    # users input validations
    if len(new_name) > 0 and new_age > 12 and new_age < 50:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    # returning total no of friends.
    return len(friends_name)