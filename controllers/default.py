# -*- coding: utf-8 -*-
### required - do no delete
from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'cybertechsolts@gmail.com'
mail.settings.login = 'cybertechsolts@gmail.com:perreoperreo'

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    return dict()

@auth.requires_login()
def notifications():
    return dict()

@auth.requires_login()
def requests():
    return dict()

@auth.requires_login()
def catalogue():
    personal = db().select(db.empleado.ALL, orderby=db.empleado.nombre)
    edificio = db().select(db.edificio.ALL, orderby=db.edificio.nombre)
    inventario = db().select(db.inventario.ALL, orderby=db.inventario.material)
    area = db().select(db.area.ALL, orderby=db.area.nombre)
    supervisor = db().select(db.supervisor.ALL, orderby=db.supervisor.nombre)
    unidad = db().select(db.unidad.ALL, orderby=db.unidad.nombre)
    estatus_solicitud = db().select(db.estatus_solicitud.ALL, orderby=db.estatus_solicitud.nombre_estatus)
    prioridad = db().select(db.prioridad.ALL, orderby=db.prioridad.nombre_prioridad)
    espacio = db().select(db.espacio.ALL, orderby=db.espacio.nombre_espacio)
    lugar = db().select(db.lugar.ALL, orderby=db.lugar.edificio)
    form_personal = SQLFORM(db.empleado)
    if form_personal.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_edificio = SQLFORM(db.edificio)
    if form_edificio.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_inventario = SQLFORM(db.inventario)
    if form_inventario.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_area = SQLFORM(db.area)
    if form_area.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_supervisor = SQLFORM(db.supervisor)
    if form_supervisor.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_unidad = SQLFORM(db.unidad)
    if form_unidad.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_estatus = SQLFORM(db.estatus_solicitud)
    if form_estatus.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_prioridad = SQLFORM(db.prioridad)
    if form_prioridad.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_espacio = SQLFORM(db.espacio)
    if form_espacio.accepts(request.vars, session):
       response.flash = 'your comment is posted'
    form_lugar = SQLFORM(db.lugar)
    if form_lugar.accepts(request.vars, session):
       response.flash = 'your comment is posted'

    return dict(personal=personal,edificio=edificio,form_personal=form_personal,inventario=inventario,area=area,supervisor=supervisor,unidad=unidad,estatus_solicitud=estatus_solicitud,prioridad=prioridad,espacio=espacio,form_edificio = form_edificio,form_inventario = form_inventario, form_area = form_area,form_supervisor = form_supervisor,form_unidad = form_unidad,form_estatus = form_estatus,form_prioridad = form_prioridad,form_espacio = form_espacio,lugar = lugar,form_lugar=form_lugar)

# Falta Arreglarle Algunos Detalles
def eliminar():
    db(db.empleado.identificador==request.args(0)).delete()
    db(db.lugar.espacio==request.args(0)).delete()
    db(db.edificio.nomenclatura==request.args(0)).delete()
    db(db.area.nomenclatura==request.args(0)).delete()
    db(db.supervisor.identificador==request.args(0)).delete()
    db(db.prioridad.nombre_prioridad==request.args(0)).delete()
    db(db.espacio.nombre_espacio==request.args(0)).delete()
    db(db.unidad.id==request.args(0)).delete()
    db(db.estatus_solicitud.id==request.args(0)).delete()
    db(db.inventario.id==request.args(0)).delete()
    redirect(URL('catalogue'))
    return dict()

@auth.requires_login()
def inventory():
    return dict()

@auth.requires_login()
def notifications():
    return dict()

def show_send_email():

    form = SQLFORM.factory(
        Field('Correo', requires =[ IS_NOT_EMPTY(error_message='Campo Requerido'), IS_EMAIL(error_message='Correo inválido') ]),
        Field('Asunto', requires=IS_NOT_EMPTY(error_message='Campo Requerido')),
        Field('Mensaje', requires=IS_NOT_EMPTY(error_message='Campo Requerido'), type='text'),submit_button='Enviar'
    )

    strings = form.elements(_class='string')
    form.add_button('Regresar', URL('default','notifications'))

    btn = form.elements(_class='btn btn-primary')
    for b in btn:
        b['_class'] = 'btn form_submit'

    btnc = form.elements(_class='w2p-form-button')
    for b in btnc:
        b['_class'] = 'btn form_cancel'

    if form.process().accepted:
        session.name = form.vars.name
        session.email = form.vars.Correo
        session.subject = form.vars.Asunto
        session.message = form.vars.Mensaje
        if mail:
            if mail.send(to=form.vars.Correo,
                subject=form.vars.Asunto,
                message=form.vars.Mensaje):
                response.flash = 'email sent sucessfully.'
            else:
                response.flash = 'fail to send email sorry!'
        else:
            response.flash = 'Unable to send the email : email parameters not defined'
    elif form.errors:
            response.flash='form has errors.'

    response.flash='you clicked on civilized'

    return dict(form=form)

@auth.requires_login()
def sb():
    return dict()
def error():
    return dict()

'''<!--       <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav navbar-right">
            {{='auth' in globals() and auth.navbar('Welcome',mode='dropdown') or ''}}
          </ul>
       </div> -->'''
