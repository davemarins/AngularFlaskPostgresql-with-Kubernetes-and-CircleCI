# -*- coding: utf-8 -*-
"""

UserService class - This class holds the method related to User manipulations.

"""

from ..main.models.user import User
from ..main.services import SQLAlchemyService


class UserService(SQLAlchemyService):
    __model__ = User

    def __init__(self):
        # Creating a parent class ref to access parent class methods.
        self.parentClassRef = super(UserService, self)

