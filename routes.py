from app import app, db
from flask import  render_template, redirect, url_for
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', subtitulo = "Grupo 11")

@app.route('/sobrenosotros', methods=['GET', 'POST'])
def sobrenosotros():

    formulario = formularios.FormAgregarTareas()

    if formulario.validate_on_submit():
        nueva_tarea = Tarea(titulo=formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
        return redirect('/sobrenosotros')

    tareas = Tarea.query.all()  # esto sirve para obtener todas las tareas y moustrarlas em sobrenosotros.html

    return render_template(
        'sobrenosotros.html',
        form=formulario,
        tareas=tareas
    )
@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '

# Ruta para editar una tarea existente
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarea = Tarea.query.get_or_404(id)
    formulario = formularios.FormAgregarTareas()

    if formulario.validate_on_submit():
        tarea.titulo = formulario.titulo.data
        db.session.commit()
        return redirect('/sobrenosotros')

    # Precargar el formulario con el dato existente
    formulario.titulo.data = tarea.titulo

    return render_template(
        'editar.html',
        form=formulario,
        tarea=tarea
    )
@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    try:
        db.session.delete(tarea)
        db.session.commit()
        print(f"Tarea{id} eliminada")
    except Exception as e:
            print(f"Error al eliminar: {e}")
            db.session.rollback()
    return redirect (url_for('sobrenosotros'))
        
        