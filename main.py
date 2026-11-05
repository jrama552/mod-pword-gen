from main_functions import *
from preset_vault import preset_vault
import time
import os
import traceback
import sys

'''def show_error_location(exc_type, exc_value, exc_tb):
    sys.__excepthook__(exc_type, exc_value, exc_tb)   # prints the normal traceback first
    summary = traceback.extract_tb(exc_tb)
    last = summary[-1]
    print(f'File "{last.filename}", line {last.lineno}, in {last.name}  2', file=sys.stderr) #last.name gives the module name

sys.excepthook = show_error_location'''                               # assign the function (no parentheses)

start = time.perf_counter()


# if file already exists, do nothing
if __name__ == '__main__':
    for file, init in init_list:
        if not os.path.exists(file):
            init()
vault = []
preset_vault(vault)
run = True
while run:
    # need to mount list/files
    print(f'vault: {vault}')
    run = direct_user(user_action(), vault)


end = time.perf_counter()
print(f'\n{end - start:.5f} seconds')



# current: view ---> making 'view' function (in user functions vs in aux_functions)
# 4. save account/password pairs (password notepad) to file and retrieve
# 5. ask user for input (what do you want to generate w/ (i.e. the
# actual customization and modular part of the pword generation --> pword resets)
# 6. similar idea, but presents of generation

# not sure if addressed: # 3. need to fix profile.lowered() function, tags splitter, and
