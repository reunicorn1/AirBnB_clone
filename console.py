#!/usr/bin/env python3
'''Entry point of the command interpreter'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''class HBNBCommand'''
    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '

    def do_quit(self, _):
        '''Quit command to exit the program
        '''

        return True

    def do_EOF(self, _):
        '''End-of-file
        '''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
