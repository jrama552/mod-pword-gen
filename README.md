# modular_password_generator
Description: **see name**

NOTE: **WORK IN PROGRESS**

GOAL: make a password generator
objectives: (update; not current)
- format two hexacosademical characters, a 7-9 letter word (in English OR Japanese, or any custom word list), then 3 numbers or symbols (e.g. 5ehorned8! a3building2 9cGintama#2)
- make it (somewhat) modular (you can add addition word lists, but must go through formatting and length checks -- see init_jp)
- make a simple GUI that shows used passwords

Miscellaneous:
jp_dict.csv is the raw file from which i pulled the japanese words for


Notes for code:
jp_file is the raw imported file
jp_dict is the cleaned file 
jp_wordlist is the list of useable jp words
