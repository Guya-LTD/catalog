# -*- coding: utf-8 -*-

"""Copyright Header Details

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)
 
Project
-------
    * Name: 
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - Catalog Service
    * Description
        - Catlog Catalog Service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style
"""

import pytest
from faker import Faker

from catalog import create_app
from catalog.repository.category import Category


class TestCategoryApi:

    AM_WORD_LIST = (
        'አልማዝን', 'አየኋት', 'ከፈትኩላት', 'በሩን', 'ዘጋሁባት',
        'አየሩ', 'ተኝቷል', 'ኢትዮጵያ', 'ውስጥ', 'ናት', 'ከተማ'
    )

    def setup_class(self):
        # init faker object
        self.faker = Faker()
        # creating a FlaskClient instance to interact with the app
        self.app = create_app().test_client()

    def test_categories_get_api(self):
        url = '/api/v1/categories'
        # calling api endpoint
        categories = self.app.get(url)
        # asserting status code
        assert categories.status_code == 200

    def test_categories_post_api(self):
        url = '/api/v1/categories'
        data = {
            'names': {
                'en': self.faker.sentence(),
                'am': self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
            },
            'image': {
                'src': self.faker.url(),
                'priority': 1,
                'height': self.faker.random_int(min=100, max=1900),
                'width': self.faker.random_int(min=100, max=1900)
            }
        }
        # calling api endpoint
        categories = self.app.post(url, json = data)
        # asserting status code
        assert categories.status_code == 201

    def test_categories_post_without_image(self):
        url = '/api/v1/categories'
        data = {
            'names': {
                'en': self.faker.sentence(),
                'am': self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
            }
        }
        # calling api endpoint
        categories = self.app.post(url, json = data)
        # asserting status code
        assert categories.status_code == 201

    def test_category_get_api(self):
        pass

    def test_category_get_api_with_invalid_id(self):
        id = self.faker.sentence()
        url = '/api/v1/categories/%s' % id
        # calling apis endpoint
        category = self.app.get(url)
        # asserting status code
        assert category.status_code == 400

    def test_category_get_api_with_empty_id(self):
        id = self.faker.sentence()
        url = '/api/v1/categories/%s' % id
        # calling apis endpoint
        category = self.app.get(url)
        # asserting status code
        assert category.status_code == 400

    def test_category_put_api(self):
        pass

    def test_category_put_api_with_invalid_id(self):
        id = self.faker.sentence()
        url = '/api/v1/categories/%s' % id
        # calling apis endpoint
        category = self.app.put(url)
        # asserting status code
        assert category.status_code == 400

    def test_category_put_api_with_empty_id(self):
        id = self.faker.sentence()
        url = '/api/v1/categories/%s' % id
        # calling apis endpoint
        category = self.app.put(url)
        # asserting status code
        assert category.status_code == 400

    def test_category_delete_api(self):
        id = self.faker.sentence()
        url = '/api/v1/categories/%s' % id
        # calling apis endpoint
        category = self.app.delete(url)
        # asserting status code
        assert category.status_code == 405
