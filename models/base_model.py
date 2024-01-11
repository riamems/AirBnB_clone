#!/usr/bin/python3
"""Defines the BaseModel class."""


import uuid
from datetime import datetime


class BaseModel:
    """Base class for other classes to be used for the duration."""

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes.

        If no keyword arguments are provided, generates a new UUID for the `id`
        attribute and sets the `created_at` and `updated_at` attributes to the
        current datetime. Adds the new instance to the storage.

        If keyword arguments are provided, converts the `created_at` and
        `updated_at` attributes from string format to datetime format and sets
        the instance attributes accordingly.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    __repr__ = __str__

    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        }
