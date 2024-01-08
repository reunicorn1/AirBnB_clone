#!/usr/bin/env python3
'''This Module defines file storage class'''


class FileStorage:
    ''' FileStorage class.

    Attrs:
        __file_path(str): path to the JSON file
        __objects(dictionary): empty but will store all objects
            by <class name>.id
    '''

    __file_path = ''
    __objects = {}

    def all(self):
        '''Returns the dictionary'''
        pass

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''
        pass

    def save(self):
        '''Serializes __objects to the JSON file'''
        pass

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        pass
