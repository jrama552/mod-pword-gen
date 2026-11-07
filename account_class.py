class Profile:
    def __init__(self, account, username, password, tags):
        self.acc = account
        self.user = username
        self.password = password
        self.tags = tags

    def printo(self):
        if self.password == '':
            print(f'{self.acc}\nUsername: {self.user}\nPassword: None\nTags: ', end='')
            for x in self.tags:
                print(x, end='; ')
            print('\n')
        else:
            print(f'{self.acc}\nUsername: {self.user}\nPassword: {self.password}\nTags: ', end='')
            for x in self.tags:
                print(x, end='; ')
            print('\n')

    def lowered(self, field):
        lower_tags = []
        for x in self.tags:
            lower_tags.append(x.lower())
        values = {
            'a': self.acc.lower(),
            'u': self.user.lower(),
            'p': self.password.lower(),
            't': lower_tags
        }
        return values[field]


