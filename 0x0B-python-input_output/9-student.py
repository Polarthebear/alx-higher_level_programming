#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new student.


        Args:
            first_name: First name of the student
            last_name: Last name of the student
            age: age of the new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """find a dictionary representation of the student."""
        return self.__dict__
