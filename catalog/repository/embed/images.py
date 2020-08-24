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

from catalog.database import db


class Images(db.EmbeddedDocument):
    """Images, Default Embedded Document 

    A Meta Class 

    ...

    Attributes
    ----------
    height : Integer 

    width : Integer 

    priority : Integer 
        Which one two display first, the lower the no the first

    src : String 
        Mostly contain images url path 

    """
    
    height = db.IntField(default = 1900)
    
    width = db.IntField(default = 1900)
    
    priority = db.IntField(default = 0)
    
    src = db.StringField()