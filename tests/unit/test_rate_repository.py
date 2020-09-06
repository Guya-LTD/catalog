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

from catalog.repository.rate import Rate

class TestRateRepository:

    def setup_class(self):
        # init faker object
        self.faker = Faker()
        # rate repo
        self.rate = Rate(
            user_id = self.faker.name(),
            rating = self.faker.random_int(min=0, max=5)
        )

    def test_rate_object_creation(self):
        isinstance(self.rate, Rate)