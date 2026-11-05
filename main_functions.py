from user_functions import *


# ------------------------------------------action center-------------------------------------------------

# returns the input string (not lowercased)
def prompt_menu_choice():  # Asks what the user wants to do until the input is c/v/e/ex
    flag = False
    while not flag:
        actions = ['c', 'v', 'e', 'ex']
        intent = input('What do you want to do?\n[c]reate profile/password, '
                       '[v]iew saved passwords, [e]dit saved passwords, [ex]it\n')
        if not intent.lower() in actions:
            print("Answer must be 'c', 'v', 'e', or 'ex'.")
        else:
            print(f'\x1B[3mFLAG: \x1B[0m user intent: {intent}')
            flag = True
            return intent

# returns True to keep the main loop going, False to exit
def run_menu_action(intent, vault):  # runs the function matching the menu choice
    if intent == 'c':
        print(f'\x1B[3mFLAG:\x1B[0m intent: create profile/password')
        generate_and_assign_password(vault)
        return True
    elif intent == 'v':
        print(f'\x1B[3mFLAG:\x1B[0m intent: {intent}')
        # function
        return True
    elif intent == 'e':
        print(f'\x1B[3mFLAG:\x1B[0m intent: {intent}')
        # function
        return True
    else:
        return False