from database import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    activo = db.Column(db.Boolean)
    fecha_nacimiento = db.Column(db.Date)
    email = db.Column(db.String(50))

    def __str__(self):
        return self.nombres + ' ' + self.apellidos