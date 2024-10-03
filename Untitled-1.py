
version = '0.1.0'
mode_selected = None
import time
import decrypter
def mode_select_user_input():
    mode_input = input('Enter e for encryption. Enter d for decryption.' + '\n')
    return mode_input

def get_mode():
    global mode_selected
    mode_selected = mode_select_user_input()

    if mode_selected in ['e', 'E']:
        print('Encryption selected.')
        return 'enc'
    elif mode_selected in ['d', 'D']:
        print('Decryption selected.')
        return 'dec'
    else:
        print('Unrecognized mode. Are you sure you typed the right character? Please try again.' + '\n')
        get_mode() # resets program



if get_mode() == 'dec':
    # INSERT DECRYPTION HERE
    pass
