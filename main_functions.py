from user_functions import *


# ------------------------------------------action center-------------------------------------------------


def user_action():
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


def direct_user(intent, vault):
    if intent == 'c':
        print(f'\x1B[3mFLAG:\x1B[0m intent: create profile/password')
        generate_password(vault)
        return True
    elif intent == 'v':
        print(f'\x1B[3mFLAG:\x1B[0m intent: {intent}')
        view_profile(vault) # create func
        # function
        return True
    elif intent == 'e':
        print(f'\x1B[3mFLAG:\x1B[0m intent: {intent}')
        # function
        return True
    else:
        return False


