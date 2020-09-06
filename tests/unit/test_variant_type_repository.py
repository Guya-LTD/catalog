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

from catalog.repository.embed import Names
from catalog.repository.variant_type import VariantType


class TestVariantTypeRepository():

    AM_WORD_LIST = (
        'አልማዝን', 'አየኋት', 'ከፈትኩላት', 'በሩን', 'ዘጋሁባት',
        'አየሩ', 'ተኝቷል', 'ኢትዮጵያ', 'ውስጥ', 'ናት', 'ከተማ'
    )

    def setup_class(self):
        # init faker object
        self.faker = Faker()
        # init names of category
        self.names = Names(
            en = self.faker.sentence(),
            am = self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
        )
        # init variant type
        self.variant_type = VariantType(names = self.names)

    def test_variant_type_object_creation(self):
        isinstance(self.variant_type, VariantType)

    def test_variant_type_object_creation_value_for_names(self):
        assert self.variant_type.names == self.names