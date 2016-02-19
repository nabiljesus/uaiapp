response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Índice'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Solicitudes'),URL('default','requests')==URL(),URL('default','requests'),[]),
(T('Catálogo'),URL('default','catalogue')==URL(),URL('default','catalogue'),[]),
(T('Inventario'),URL('default','inventory')==URL(),URL('default','inventory'),[]),
(T('Notificaciones'),URL('default','show_send_email')==URL(),URL('default','show_send_email'),[]),
]
