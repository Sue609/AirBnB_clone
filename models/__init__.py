#!/usr/bin/python3
""" Package initialization """
from models import storage


storage = FileStorage()
storage.reload()
