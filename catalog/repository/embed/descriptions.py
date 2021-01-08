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
        - Catalog service for Guya microservices
    * Description
        - Catalog mangement service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style
    flask-mongoengine v0.7


flask-mongoengine based ODM flask-mongoengine built up on pymongo engine.
"""

from catalog.model.descriptions import Descriptions as DescriptionsEntity
from catalog.database import db


class Descriptions(db.EmbeddedDocument, DescriptionsEntity):
    """Embedded document.
    
    Attributes
    ----------
    en: String
        English language field

    am: String
        Amharic language field
    """

    en = db.StringField(required = True)

    am = db.StringField()