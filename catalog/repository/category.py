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


Entity.
"""

from catalog.database import db
from catalog.model.category import category as CategoryEntity
from .mixins.timestamp_mixin import TimestampMixin
from .embed import Names, Assets


class Category(db.Document, CategoryEntity, TimestampMixin):
    """Categories ODM 
    
    ...

    Attributes
    ----------
    _id : String 
        Auto inherated attribute, 12-byte, 24 char hexadicmal
    
    names : Dictionary
        Language Translation References, called with their short name
        Example :
            - names.en
            - names.am

    count : Integer 
        The Number of products found in the current category

    parent : String 
        Parent Object Id, i.e 12-byte, 24 char hexadicmal

    assets : Dictionary
        Stores Images or Videos
    """

    ames = db.EmbeddedDocumentField(Names)
    
    count = db.IntField(default = 0)
    
    parent = db.StringField
    
    facets = db.ListField(db.StringField())

    assets = db.EmbeddedDocumentField(Assets)