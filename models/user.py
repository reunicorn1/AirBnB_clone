#!/usr/bin/env python3
'''Module defines `User` class'''

from models.base_model import BaseModel


class User(BaseModel):
    '''User class.

    Atrrs:
        email: string
        password: string
        first_name: string
        last_name: string
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        '''Initiliaztion'''
        super().__init__(*args, **kwargs)
