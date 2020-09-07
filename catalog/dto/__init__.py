from flask_restplus import Namespace, fields

GNS = Namespace('General Name Space', description = '')

_Names = GNS.model('Language', {
 
    'en' : fields.String(required = False, description = ''),
 
    'am' : fields.String(required = False, description = '')

})


_Images = GNS.model('Images', {
 
    'height' : fields.Integer(),

    'width' : fields.Integer(),

    'priority' : fields.Integer(),

    'src' : fields.Url()

})


_Assets = GNS.model('Assets', {
 
   'images' : fields.List(fields.Nested(_Images))

})

_Response = GNS.model('Response', {
    'code': fields.Integer(),
    'description': fields.String(),
    'message' : fields.String(),
    'errors' : [],
    'warnings': [],
    'datas': []
})