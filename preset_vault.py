from account_class import *


def preset_vault(vault):
    p1 = Profile('Github', 'jrama552', '', ['Programming', 'School'])
    p2 = Profile('Spotify', 'jiror', '', ['Entertainment'])
    p3 = Profile('MyUCLA', 'Joe', '', ['School', 'Career'])
    plist = [p1, p2, p3]
    for x in plist:
        vault.append(x)

