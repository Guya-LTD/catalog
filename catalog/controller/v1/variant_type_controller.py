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


"""REST namespace Controller

Responses List :
    1xx -> :            Informational response - The request was received, continuing process
        * 100           Continue
        * 101           Switching Protocols
        * 102           Processing
        * 103           Early Hints (RFC 8297)

    2xx -> :            Successful - The request was successfully received, understood, and accepted
        * 200           Ok
        * 201           Created
        * 202           Accepted
        * 203           Non-Authoritative Information
        * 204           No Content
        * 205           Reset Content
        * 206           Partial Content
        * 207           Multi-Status
        * 208           Already Reported
        * 226           IM Used

    3xx -> :            Redirection - Further action needs to be taken in order to complete the request
        * 300           Multiple Choices
        * 301           Moved Permanently
        * 302           Found (Previously "Moved temporarily")
        * 303           See Other
        * 304           Not Modified
        * 305           Use Proxy
        * 306           Switch Proxy
        * 307           Temporary Redirect
        * 308           Permanent Redirect

    4xx -> :            Client Error - The request contains bad syntax or cannot be fulfilled
        * 400           Bad  Request
        * 401           Unauthorized
        * 402           Payment Required
        * 403           Forbidden
        * 404           Not Found
        * 405           Method Not Allowed
        * 406           Not Acceptable
        * 407           Proxy Authentication Required
        * 408           Request Timeout
        * 409           Conflict
        * 410           Gone
        * 411           Length Required
        * 412           Precondition Failed
        * 413           Payload Too Large
        * 414           URI Too Long
        * 415           Unsupported Media Type
        * 416           Range Not Satisfiable
        * 417           Expection Failed
        * 418           I'm a teapot
        * 421           Misdirected Request
        * 422           Unprocessable Entity
        * 423           Locked
        * 424           Failed Dependency
        * 425           Too Early
        * 426           Upgrade Required
        * 428           Precondition Required
        * 429           Too Many Requests
        * 431           Request Header Fields Too Large
        * 451           Unavailable For Legal Reasons

    5xx -> :            Server Error - The server failed to fulfil an apparently valid request
        * 500           Internal Server Error
        * 501           Not Implemented
        * 502           Bad Gateway
        * 503           Service Unavaliable
        * 504           Gateway Timeout
        * 505           HTTP Version Not Supported
        * 506           Variant Also Negotiates
        * 507           Insufficent Storage
        * 508           Loop Detected
        * 510           Not Extended
        * 511           Network Authentication Required


Functions:
    * get - returns list of datas
    * post - returns creation status with the newly created resource link
    * put - return update status with the the newly updated resource link
    * patch - returns the semi updated status with the newly semi updated resource link
    * delete - return delation status

"""

import ast
from bson import ObjectId
from flask import request, jsonify, make_response
from flask_restplus import Resource

from catalog.dto.variant_type_dto import VariantTypeDto
from catalog.blueprint.v1.variant_type import namespace
from catalog.repository.variant_type import VariantType
from catalog.repository.embed import Names, Assets, Images
from catalog.exception import ValueEmpty, InvalidObjectId, DocumentDoesNotExist


@namespace.route('')
@namespace.response(100, 'Continue')
@namespace.response(101, 'Switching Protocols')
@namespace.response(102, 'Processing')
@namespace.response(103, 'Early Hints (RFC 8297)')
@namespace.response(200, 'Ok')
@namespace.response(201, 'Created')
@namespace.response(202, 'Accepted')
@namespace.response(203, 'Non-Authoritative Information')
@namespace.response(204, 'No Content')
@namespace.response(205, 'Reset Content')
@namespace.response(206, 'Partial Content')
@namespace.response(207, 'Multi-Status')
@namespace.response(208, 'Already Reported')
@namespace.response(226, 'IM Used')
@namespace.response(300, 'Multiple Choices')
@namespace.response(301, 'Moved Permanently')
@namespace.response(302, 'Found (Previously "Moved temporarily")')
@namespace.response(303, 'See Other')
@namespace.response(304, 'Not Modified')
@namespace.response(305, 'Use Proxy')
@namespace.response(306, 'Switch Proxy')
@namespace.response(307, 'Temporary Redirect')
@namespace.response(308, 'Permanent Redirect')
@namespace.response(400, 'Bad  Request')
@namespace.response(401, 'Unauthorized')
@namespace.response(402, 'Payment Required')
@namespace.response(403, 'Forbidden')
@namespace.response(404, 'Not Found')
@namespace.response(405, 'Method Not Allowed')
@namespace.response(406, 'Not Acceptable')
@namespace.response(407, 'Proxy Authentication Required')
@namespace.response(408, 'Request Timeout')
@namespace.response(409, 'Conflict')
@namespace.response(410, 'Gone')
@namespace.response(411, 'Length Required')
@namespace.response(412, 'Precondition Failed')
@namespace.response(413, 'Payload Too Large')
@namespace.response(414, 'URI Too Long')
@namespace.response(415, 'Unsupported Media Type')
@namespace.response(416, 'Range Not Satisfiable')
@namespace.response(417, 'Expection Failed')
@namespace.response(418, 'I\'m a teapot')
@namespace.response(421, 'Misdirected Request')
@namespace.response(422, 'Unprocessable Entity ')
@namespace.response(423, 'Locked')
@namespace.response(424, 'Failed Dependency')
@namespace.response(425, 'Too Early')
@namespace.response(426, 'Upgrade Required')
@namespace.response(428, 'Precondition Required')
@namespace.response(429, 'Too Many Requests')
@namespace.response(431, 'Request Header Fields Too Large')
@namespace.response(451, 'Unavailable For Legal Reasons')
@namespace.response(500, 'Internal Server Error')
@namespace.response(501, 'Not Implemented')
@namespace.response(502, 'Bad Gateway')
@namespace.response(503, 'Service Unavaliable')
@namespace.response(504, 'Gateway Timeout')
@namespace.response(505, 'HTTP Version Not Supported')
@namespace.response(506, 'Variant Also Negotiates')
@namespace.response(507, 'Insufficent Storage')
@namespace.response(508, 'Loop Detected')
@namespace.response(510, 'Not Extended')
@namespace.response(511, 'Network Authentication Required')
class VariantTypesResource(Resource):
    """Foobar Related Operation

    ...

    `asc'  +
    `desc` -


    Attributes
    ----------
    LIMIT : Integer
        Max allowed rows

    Methods
    -------
    get() :
        Get All/Semi datas from database

    post() :
        Save data/datas to database

    """

    _LIMIT = 10

    def get(self):
        """Get All/Semi datas from database

        ...

        Query Examples:
            * Filtering :
                - name.en=eq:abc&name.am=neq:abc

        Returns
        -------
            Json Dictionaries

        """

        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', self._LIMIT))
        filters = {}
        order_by = request.args.get('order_by')

        for key in request.args:
            if key not in ['page', 'limit', 'sort_by', 'order_by']:
                splited = request.args.get(key).split(':')
                value = splited[1]
                try: 
                    value = ast.literal_eval(value)
                except ValueError:
                    pass 

                filters[key] = {'$%s' % splited[0] :  value}

        variant_types = VariantType.objects(__raw__ = filters).order_by(order_by).paginate( page = page, per_page = limit).items

        # Return must always include the global fileds :
        # Field           Datatype        Default         Description             Examples
        # -----           --------        -------         -----------             --------
        # code            int             201             1xx, 2xx, 3xx, 5xx
        # description     string          Created         http code description
        # messages        array           Null            any type of messages
        # errors          array           Null            occured errors
        # warnings        array           Null            can be url format
        # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
        return make_response(jsonify({
            'code': 200,
            'description': 'Ok',
            'message': '',
            'errors': [],
            'warnings': [],
            'datas': variant_types,
            'page': page,
            'limit': limit,
            'total': VariantType.objects.count()
        }), 200)

    @namespace.expect(VariantTypeDto.request, validate = True)
    def post(self):
        """Save data/datas to database

        ...

        Returns
        -------
            Json Dictionaries

        """

        # start by validating request fields for extra security
        # step 1 validation: strip payloads for empty string        
        if not namespace.payload['names']['en'].strip():
            raise ValueEmpty({'payload': payload})

        names = Names(
            en = namespace.payload['names']['en'],
            am = namespace.payload.get('names').get('am')
        )

        variant_type = VariantType(
            names = names,
            unit = namespace.payload['unit']
        )

        variant_type.save()

        if not variant_type.id:
            namespace.abort(500)
        else:
            # Return must always include the global fileds :
            # Field           Datatype        Default         Description             Examples
            # -----           --------        -------         -----------             --------
            # code            int             201             1xx, 2xx, 3xx, 5xx
            # description     string          Created         http code description
            # messages        array           Null            any type of messages
            # errors          array           Null            occured errors
            # warnings        array           Null            can be url format
            # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
            return make_response(jsonify({
                'code': 201,
                'description': 'Created',
                'message': '',
                'errors': [],
                'warnings': [],
                'datas': variant_type
            }), 201)

    
@namespace.route('/<string:id>')
@namespace.response(100, 'Continue')
@namespace.response(101, 'Switching Protocols')
@namespace.response(102, 'Processing')
@namespace.response(103, 'Early Hints (RFC 8297)')
@namespace.response(200, 'Ok')
@namespace.response(201, 'Created')
@namespace.response(202, 'Accepted')
@namespace.response(203, 'Non-Authoritative Information')
@namespace.response(204, 'No Content')
@namespace.response(205, 'Reset Content')
@namespace.response(206, 'Partial Content')
@namespace.response(207, 'Multi-Status')
@namespace.response(208, 'Already Reported')
@namespace.response(226, 'IM Used')
@namespace.response(300, 'Multiple Choices')
@namespace.response(301, 'Moved Permanently')
@namespace.response(302, 'Found (Previously "Moved temporarily")')
@namespace.response(303, 'See Other')
@namespace.response(304, 'Not Modified')
@namespace.response(305, 'Use Proxy')
@namespace.response(306, 'Switch Proxy')
@namespace.response(307, 'Temporary Redirect')
@namespace.response(308, 'Permanent Redirect')
@namespace.response(400, 'Bad  Request')
@namespace.response(401, 'Unauthorized')
@namespace.response(402, 'Payment Required')
@namespace.response(403, 'Forbidden')
@namespace.response(404, 'Not Found')
@namespace.response(405, 'Method Not Allowed')
@namespace.response(406, 'Not Acceptable')
@namespace.response(407, 'Proxy Authentication Required')
@namespace.response(408, 'Request Timeout')
@namespace.response(409, 'Conflict')
@namespace.response(410, 'Gone')
@namespace.response(411, 'Length Required')
@namespace.response(412, 'Precondition Failed')
@namespace.response(413, 'Payload Too Large')
@namespace.response(414, 'URI Too Long')
@namespace.response(415, 'Unsupported Media Type')
@namespace.response(416, 'Range Not Satisfiable')
@namespace.response(417, 'Expection Failed')
@namespace.response(418, 'I\'m a teapot')
@namespace.response(421, 'Misdirected Request')
@namespace.response(422, 'Unprocessable Entity ')
@namespace.response(423, 'Locked')
@namespace.response(424, 'Failed Dependency')
@namespace.response(425, 'Too Early')
@namespace.response(426, 'Upgrade Required')
@namespace.response(428, 'Precondition Required')
@namespace.response(429, 'Too Many Requests')
@namespace.response(431, 'Request Header Fields Too Large')
@namespace.response(451, 'Unavailable For Legal Reasons')
@namespace.response(500, 'Internal Server Error')
@namespace.response(501, 'Not Implemented')
@namespace.response(502, 'Bad Gateway')
@namespace.response(503, 'Service Unavaliable')
@namespace.response(504, 'Gateway Timeout')
@namespace.response(505, 'HTTP Version Not Supported')
@namespace.response(506, 'Variant Also Negotiates')
@namespace.response(507, 'Insufficent Storage')
@namespace.response(508, 'Loop Detected')
@namespace.response(510, 'Not Extended')
@namespace.response(511, 'Network Authentication Required')
class VariantTypeResource(Resource):
    """"Single Foobar Related Operation

    ...

    Methods
    -------
    get(id:String) :
        Get a data from database

    put(id:String) :
        Update a data from database

    delete(id:String) :
        Delete a data from database

    """

    def get(self, id):
        """Get All/Semi datas from database

        ...

        Parameters
        ----------
        id : integer
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """

        # start by validating request fields for extra security
        # step 1 validation: valid if id is 12-hex
        if not ObjectId.is_valid(id):
            raise InvalidObjectId({'payloads': [{'id': id}]})

        # the query may be filtered by calling the QuerySet object 
        # with field lookup keyword arguments. The keys in the keyword 
        # arguments correspond to fields on the Document you are querying
        variant_type = VariantType.objects(id = id)

        # Return must always include the global fileds :
        # Field           Datatype        Default         Description             Examples
        # -----           --------        -------         -----------             --------
        # code            int             201             1xx, 2xx, 3xx, 5xx
        # description     string          Created         http code description
        # messages        array           Null            any type of messages
        # errors          array           Null            occured errors
        # warnings        array           Null            can be url format
        # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
        code = 200
        description = 'OK'

        if not variant_type:
            code = 204
            description = 'No Content'

        return make_response(jsonify({
            'code': code,
            'description': description,
            'message': '',
            'errors': [],
            'warnings': [],
            'datas': variant_type
        }), code)


    @namespace.expect(VariantTypeDto.request, validate = True)
    def put(self, id):
        """Update a data from database

        ...

        Parameters
        ----------
        id : String
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """

        # start by validating request fields for extra security
        # step 1 validation: valid if id is 12-hex
        if not ObjectId.is_valid(id):
            raise InvalidObjectId({'payloads': [{'id': id}]})

        # step 2 validation: check if document exists in collection
        if not VariantType.objects(id = id):
            raise DocumentDoesNotExist({'payloads': [{'id': id}]})

        # start by validating request fields for extra security
        # step 3 validation: strip payloads for empty string        
        if not namespace.payload['names']['en'].strip():
            raise ValueEmpty({'payload': payload})

        names = Names(
            en = namespace.payload['names']['en'],
            am = namespace.payload.get('names').get('am')
        )

        vt = VariantType.objects(id = id).update(
            names = names,
            unit = namespace.payload['unit']
        )

        if vt:
            variant_type = VariantType.objects(id = id)
            #variant_type.reload()
            # Return must always include the global fileds :
            # Field           Datatype        Default         Description             Examples
            # -----           --------        -------         -----------             --------
            # code            int             201             1xx, 2xx, 3xx, 5xx
            # description     string          Created         http code description
            # messages        array           Null            any type of messages
            # errors          array           Null            occured errors
            # warnings        array           Null            can be url format
            # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
            return make_response(jsonify({
                'code': 200,
                'description': 'OK',
                'message': 'Updated',
                'errors': [],
                'warnings': [],
                'datas': variant_type
            }), 200)


    def delete(self, id):
        """Update a data from database

        ...

        Parameters
        ----------
        id : String
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """
        # method not allowed
        namespace.abort(405)