#!/usr/bin/python3
"""test_User"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8


class test_User(test_basemodel):
    """test_User"""

    def test_user_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    # def test_first_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.first_name), str)

    # def test_last_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.last_name), str)

    # def test_email(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.email), str)

    # def test_password(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.password), str)
