#!/usr/bin/python3
""" Package initialization """
from models.engine import file_storage


storage = FileStorage()
storage.reload()
