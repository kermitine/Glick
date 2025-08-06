# Copyright (C) 2025 Ayrik Nabirahni
# This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see https://www.gnu.org/licenses.


import time
import decrypter
import encrypter
import files.ascii as ascii
from files.vars import *



def mode_select_user_input():
    return input(str('Enter e for encryption. Enter d for decryption. Enter any number to exit.' + '\n'))
def get_mode():
    while True:
        mode_selected = mode_select_user_input()
        print('\n')
        if mode_selected in ['e', 'E']:
            return 'enc'
        elif mode_selected in ['d', 'D']:
            return 'dec'
        elif mode_selected in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Program Terminating...')
            time.sleep(1.5)
            return 'terminate'
        else:
            print('Unrecognized mode. Are you sure you typed the right character? Please try again.' + '\n')
            


def glick_main():
    print('Glickcrypt V' + version_gli + ' initialized')
    print('___________________________________')
    print('\n')
    mode = get_mode()
    if mode == 'dec':
        decrypter.decrypt_main()
    elif mode == 'enc':
        encrypter.encrypt_main()
    else:
        pass

    


if __name__ == '__main__':
    ascii.ascii_run()
    glick_main()