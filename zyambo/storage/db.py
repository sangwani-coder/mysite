#!/usr/bin/env python3
""" DB class"""
import os


class DB():
    """ File storage"""

    def write_about(self, data: str)  -> str:
        """ write about msg to file"""
        path = os.path.dirname(__file__)
        f_path = os.path.join(path, 'about.txt')
        with open(f_path, 'w') as abt:
            abt.write(data)
            print('about written to:', f_path)

    def read_about(self) -> list:
        """read about text """
        path = os.path.dirname(__file__)
        f_path = os.path.join(path, 'about.txt')
        try:
            abt = open(f_path, 'r+')
            if not abt:
                abt.write("Empty")
                abt.close()
            return [abt.read()]
        except FileNotFoundError:
            print("File not found")
            return 
