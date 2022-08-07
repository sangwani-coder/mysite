#!/usr/bin/env python3
""" mysites console"""

import cmd, sys

class ZyamboShell(cmd.Cmd):
    """Administrative Shell for mysite"""
    intro = "Welcome to Zyambo's Shell.     Type help or ? to list commands.\n"
    prompt = "(sangwani) "
    file = None

    def do_project(self, arg):
        """ Adds a new project to website"""
        pass

    def do_bio(self, arg):
        'Adds bio to home page'
        pass

    def do_about(self, arg):
        'Adds about to page'
        from storage.db import DB
        DB = DB()
        if arg == '':
            try:
                about = DB.read_about()
                print(about)
            except Exception as e:
                print(e)
                return False
        else:
            DB.write_about(arg)

    def do_exit(self, arg):
        'Exits the console'
        self.close()

    def close(self):
        'Exits the console'
        print('Closing shell')
        exit(1)


if __name__ == "__main__":
    ZyamboShell().cmdloop()
