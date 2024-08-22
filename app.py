from flask import Flask, render_template, request, url_for
#
from flask_sqlalchemy import SQLAlchemy
#
from flask_migrate import Migrate
#
from models import Persona
#
from database import db
#
from forms import PersonaForm
#
from werkzeug.utils import redirect


app = Flask(__name__)
#
#Configurarcion DB
USER_DB = '#' #usuario de la base de datos
PASS_DB = '#' #contraseña de la base de datos
URL_DB = 'localhost'
NAME_DB = '#' #nombre de la base de datos
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializo el objecto db de slqalchemy
db.init_app(app)

#configuracion de flask migrate
migrate = Migrate()
migrate.init_app(app, db)

#configuracion de flask-wtf
app.config['SECRET_KEY'] = '#' #llave secreta


@app.route('/')
def inicio():
    listado_personas = Persona.query.all()
    cantidad_personas = Persona.query.count()
    return render_template('inicio.html', listado=listado_personas, cantidad=cantidad_personas)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar_persona():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
        else:
            print(persona.errors)
    
    return render_template('agregar_persona.html', form=personaForm)


@app.route('/buscar_persona/<int:id>/')
def buscar(id):
    dato=id
    persona_buscada = Persona.query.get_or_404(dato)
    
    return render_template('buscar_persona.html', persona=persona_buscada)


@app.route('/buscar/')
def buscar_persona():

    dato = request.args.get('id')
    
    if dato:
        buscado = Persona.query.filter_by(id=int(dato))
    else:
        buscado = Persona.query.all()

    return render_template('buscar.html', buscado=buscado)


@app.route('/modificar/<int:id>/', methods=['POST', 'GET'])
def modificar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method=='POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
        else:
            print(persona.errors)
    
    return render_template('actualizar.html', form=personaForm)


@app.route('/eliminar/<int:id>/')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()

    return redirect(url_for('inicio'))