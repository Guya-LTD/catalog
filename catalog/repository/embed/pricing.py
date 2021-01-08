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
        - Cart service for Guya microservices
    * Description
        - Cart mangement service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style
    flask-mongoengine v0.7

Language Short Name References List:
-----------------------------------
    * en - For English
    * am - For Amharich

flask-mongoengine based ODM flask-mongoengine built up on pymongo engine.
"""

from catalog.model.pricing import Pricing as PricingEntity
from catalog.database import db
from .dimensions import Dimensions


class Pricing(db.EmbeddedDocument, PricingEntity):
    """Pricing, Default Embedded Document 

    A Meta Class 

    ...

    Attributes
    ----------
    list : Decimal

    retail : Decimal

    savings : Decimal

    pct_savings : Decimal
    """

    price = db.DecimalField()

    retail = db.DecimalField(default = 0)

    savings = db.DecimalField(default = 0)

    pct_savings = db.DecimalField(default = 0)