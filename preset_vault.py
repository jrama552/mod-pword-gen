from account_class import *


def load_test_profiles(vault):  # Appends hard-coded test Profiles (Github, Spotify) to the given vault list in place; returns None
    p1 = Profile('Github', 'jrama552', '', ['Programming'])
    p2 = Profile('Spotify', 'jiror', '', ['Entertainment'])
    p_N = [p1, p2]
    for x in p_N:
        vault.append(x)