response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Notifications'),URL('default','notifications')==URL(),URL('default','notifications'),[]),
(T('Requests'),URL('default','requests')==URL(),URL('default','requests'),[]),
(T('Catalogue'),URL('default','catalogue')==URL(),URL('default','catalogue'),[]),
(T('Inventory'),URL('default','inventory')==URL(),URL('default','inventory'),[]),
(T('Sb'),URL('default','sb')==URL(),URL('default','sb'),[]),
]