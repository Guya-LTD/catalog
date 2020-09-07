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