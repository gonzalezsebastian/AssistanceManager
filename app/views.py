from flask_appbuilder.api import expose
from flask_appbuilder.baseviews import BaseView
from flask_appbuilder.security.decorators import has_access
from .models import Asignatura, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask import g
from flask_appbuilder.security.sqla.models import User

from . import appbuilder, db
import app

# TODO: Probar related views
# related_views = [EmployeeView]

class ClassesView(BaseView):
    
    default_view = 'listaClases'
    @has_access
    @expose('/listaClases')
    def listaClases(self):
        
        return render_template('ListaClases.html', user=g.user)
    
    @has_access
    @expose('/clase/<id>')
    def Clase(self, id):
        
        return render_template('Clase.html', user=g.user)

class DepartamentoView(ModelView):
    datamodel = SQLAInterface(Departamento)
    add_columns=['id','nombre']
    list_columns=['id','nombre']
    show_columns=['id','nombre']

class ProgramaAcademicoView(ModelView):
    datamodel = SQLAInterface(ProgramaAcademico)
    add_columns=['id','nombre','departamento']
    list_columns=['id','nombre','departamento']
    show_columns=['id','nombre','departamento']
    
class AsignaturaView(ModelView):
    datamodel = SQLAInterface(Asignatura)
    add_columns=['id','nombre','departamento']
    list_columns=['id','nombre','departamento']
    show_columns=['id','nombre','departamento']
    
class PlanEstudioView(ModelView):
    datamodel = SQLAInterface(PlanEstudio)
    add_columns=['id','nombre','programa']
    list_columns=['id','nombre','programa']
    show_columns=['id','nombre','programa']

class PlanAsignaturaView(ModelView):
    datamodel = SQLAInterface(PlanAsignatura)
    add_columns=['id','asignatura','plan']
    list_columns=['id','asignatura','plan']
    show_columns=['id','asignatura','plan']
    
    
class PeriodoView(ModelView):
    datamodel = SQLAInterface(Periodo)
    add_columns=['id','nombre']
    list_columns=['id','nombre']
    show_columns=['id','nombre']
    
class SalonView(ModelView):
    datamodel = SQLAInterface(Salon)
    add_columns=['id']
    list_columns=['id']
    show_columns=['id']
    
class DocenteView(ModelView):
    datamodel = SQLAInterface(Docente)
    add_columns=['id','nombre', 'direccion', 'email','cedula', 'departamento']
    list_columns=['id','nombre', 'direccion', 'email', 'cedula', 'departamento']
    show_columns=['id','nombre', 'direccion', 'email', 'cedula', 'departamento']

class CursoView(ModelView):
    datamodel = SQLAInterface(Curso)
    add_columns=['id', 'docente', 'asignatura']
    list_columns=['id', 'docente', 'asignatura']
    show_columns=['id', 'docente', 'asignatura']
    
class ClaseView(ModelView):
    datamodel = SQLAInterface(Clase)
    add_columns=['id', 'curso', 'inicio', 'fin', 'salon']
    list_columns=['id', 'curso', 'inicio', 'fin', 'salon']
    show_columns=['id', 'curso', 'inicio', 'fin', 'salon']
    
class EstudianteMatriculaView(ModelView):
    datamodel = SQLAInterface(EstudianteMatriculaCurso)
    add_columns=['curso', 'periodo', 'estudiante']
    list_columns=['curso', 'periodo', 'estudiante']
    show_columns=['curso', 'periodo', 'estudiante']

class EstudianteView(ModelView):
    datamodel = SQLAInterface(Estudiante)
    add_columns=['id','nombre', 'direccion', 'cedula', 'telefono', 'plan', 'periodo']
    list_columns=['id','nombre', 'direccion', 'cedula', 'telefono', 'plan', 'periodo']
    show_columns=['id','nombre', 'direccion', 'cedula', 'telefono', 'plan', 'periodo']

appbuilder.add_view(
    DepartamentoView, "Departamentos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    ProgramaAcademicoView, "Programas Academicos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    AsignaturaView, "Asignaturas", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    PlanEstudioView, "Planes de Estudio", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    PlanAsignaturaView, "Plan de Estudio - Asignatura", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    PeriodoView, "Periodos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    SalonView, "Salones", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    DocenteView, "Docentes", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    CursoView, "Cursos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    ClaseView, "Clases", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    EstudianteMatriculaView, "Estudiante-Matricula", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    EstudianteView, "Estudiantes", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    ClassesView, "Lista de clases", icon="fa-folder-open-o", category="Lista de clases"
)