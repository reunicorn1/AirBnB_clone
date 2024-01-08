#!/usr/bin/env python3
'''Module defines BaseModel class'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''BaseModel class'''
    def __init__(self) -> None:
        '''Instantiate an instance'''
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        '''updates the public instance attribute updated_at'''
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__

        Return:
            __dict__ plus __class__ represents class name
        '''
        return {**self.__dict__, '__class__': self.__class__.__name__}

    def __str__(self):
        '''Instance representaion'''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)
