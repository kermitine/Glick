
version = '0.2.0'
import time
import decrypter
def mode_select_user_input():
    return input('Enter e for encryption. Enter d for decryption.' + '\n')

def get_mode():
    mode_selected = None
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


def glick_main():
    if get_mode() == 'dec':
        decrypter.decrypt_main()

if __name__ == '__main__':
    glick_main()