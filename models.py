from extension import db

class Tarea(db.Model):
    __tablename__ = 'tareas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'<Tarea {self.titulo!r}>'