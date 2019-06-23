# -*- coding: utf-8 -*-
"""Unittest for testing app configs"""

import unittest
from flask import current_app

from server.main.api import create_app_blueprint
from server.tests.base import BaseTestCase


class TestDevelopmentConfig(BaseTestCase):
    """Class to test dev app configs"""

    def create_app(self):
        """Overwrites this method is BaseTestCase
        :return: Flask app
        """
        app = create_app_blueprint('development')
        return app

    def test_dev_config(self):
        """Test the config for Development environment"""
        with self.context:
            message = "Development DEBUG config value should be true instead of " + str(current_app.config['DEBUG'])
            self.assertEqual(current_app.config['DEBUG'], True,
                             msg=message)
            message = "Development TESTING config value should be false instead of " + str(current_app.config['TESTING'])
            self.assertEqual(current_app.config['TESTING'], False,
                             msg=message)

class TestTestingConfig(BaseTestCase):
    """Class to test test app configs"""
    def create_app(self):
        """Overwrites this method is BaseTestCase

        :return: Flask app
        """
        app = create_app_blueprint('testing')
        return app

    def test_test_config(self):
        """Test the config for Testing environment"""
        with self.context:
            message = "Testing DEBUG config value should be false instead of " + str(current_app.config['DEBUG'])
            self.assertEqual(current_app.config['DEBUG'], False,
                             msg=message)
            message = "Testing TESTING config value should be true instead of " + str(current_app.config['TESTING'])
            self.assertEqual(current_app.config['TESTING'], True,
                             msg=message)

if __name__ == '__main__':
    unittest.main()
