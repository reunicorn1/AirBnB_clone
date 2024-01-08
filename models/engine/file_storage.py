#!/usr/bin/env python3
'''This Module defines file storage class'''

from json import loads, dumps

class FileStorage:
    ''' FileStorage class.

    Attrs:
        __file_path(str): path to the JSON file
        __objects(dictionary): empty but will store all objects
            by <class name>.id
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary `__objects`'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''
        if not obj:
            return
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        '''Serializes __objects to the JSON file'''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(dumps(FileStorage.__objects, indent=4))

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                _dict = loads(file.read())
                FileStorage.__objects = _dict
#                for _, v in _dict.items():
#                    print(imp.load_source('base_model', 'models/base_model.py').BaseModel())
        except:
            pass
