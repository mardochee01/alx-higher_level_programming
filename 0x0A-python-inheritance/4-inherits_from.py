#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks is instance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
