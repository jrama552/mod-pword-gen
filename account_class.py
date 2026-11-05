class Profile:
    def __init__(self, account, username, password, tags):  # THE CLASS: stores the profile's account, username, password, and tags
        self.acc = account
        self.user = username
        self.password = password
        self.tags = tags

    def print_profile(self):  # prints the profile's fields (password shows "None" if empty); returns None
        if self.password == '':
            print(f'{self.acc}\nUsername: {self.user}\nPassword: None\nTags: ', end='')
            for x in self.tags:
                print(x, end='')
            print('\n')
        else:
            print(f'{self.acc}\nUsername: {self.user}\nPassword: {self.password}\nTags: ', end='')
            for x in self.tags:
                print(x, end='')
            print('\n')