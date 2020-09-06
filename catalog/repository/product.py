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
from catalog.model.product import Product as ProductEntity
from .embed import Names, Descriptions, Assets


class Product(db.Document, ProductEntity):
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

    descriptions : Dictionary
        Language Translation References, called with their short name
        Example :
            - names.en
            - names.am

    store : String 
        Unique Store identifier

    category : Object->Category

    assets : Dictionary
        Stores Images or Videos 

    rate : Integer 
        Rating 

    rate_count : Integer 
        Total count of rating 

    rate_average : Interger 
        Average Rating 1 - 5

    """

    names = db.EmbeddedDocumentField(Names)
    
    descriptions = db.EmbeddedDocumentField(Descriptions)

    sku = db.StringField()

    shipping = db.EmbeddedDocumentField(Shipping)

    variants = db.EmbeddedDocumentListField(Variants)
    
    store_id = db.StringField()
    
    category = db.ReferenceField(Category)

    assets = db.EmbeddedDocumentField(Assets)

    pricing = db.EmbeddedDocumentField(Price)

    rates = db.ListField(db.ReferenceField(Rate))

    rate_count = db.IntField(default = 0)

    rate_average = db.IntField(default = 0)
