#!/usr/bin/env python3
'''Module creates a unique FileStorage instance for the application

Attrs:
    storage: an instance of FileStorage
'''

from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
