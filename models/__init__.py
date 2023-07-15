#!/usr/bin/python3
"""
This module creates an instance of class FileStorage and calls reload on it
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
