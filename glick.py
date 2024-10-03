
version = '1.0.0'
import time
import decrypter
import encrypter
from files_enc.ascii import *

def ascii():
    print(ascii_kermitine_portrait)
    print(ascii_kermitine)




def mode_select_user_input():
    return input(str('Enter e for encryption. Enter d for decryption. Enter any number to exit.' + '\n'))

def get_mode():
    mode_selected = None
    mode_selected = mode_select_user_input()

    if mode_selected in ['e', 'E']:
        print('\n')
        return 'enc'
    elif mode_selected in ['d', 'D']:
        print('\n')
        return 'dec'
    elif mode_selected in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Program Terminating...')
        time.sleep(1.5)
        return 'terminate'

    else:
        print('Unrecognized mode. Are you sure you typed the right character? Please try again.' + '\n')
        get_mode() # resets program


def glick_main():
    print('Glickcrypt V' + version + ' initialized' + '\n')
    mode = get_mode()
    if mode == 'dec':
        decrypter.decrypt_main()
    elif mode == 'enc':
        encrypter.encrypt_main()
    else:
        pass

    


if __name__ == '__main__':
    ascii()
    glick_main()
    