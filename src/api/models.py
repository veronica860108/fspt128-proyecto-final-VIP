from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_bcrypt import check_password_hash, generate_password_hash
from typing import List


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
 
    calificaciones_realizadas: Mapped[List["Calificaciones"]] = relationship(back_populates="profesor")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
    def set_password(self,password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        return check_password_hash(self.password,password)


class Estudiantes(db.Model):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] =mapped_column(String(40),nullable=False)
    apellidos: Mapped[str] =mapped_column(String(40),nullable=False)
    email: Mapped[str] =mapped_column(String(40),nullable=False)
    password: Mapped[str] =mapped_column(String(40),nullable=False)

    salon_id: Mapped[int] = mapped_column(Integer, ForeignKey("salon.id"),nullable=False)
    calificaciones: Mapped[List["Calificaciones"]] = relationship(back_populates="estudiante")
    salon: Mapped["Salon"] = relationship(back_populates="alumnos")
    ####es N-n?
   
    def serialize(self):
        return{
            "estudiante_id":self.id,
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "email":self.email,
        }
    
    def set_password(self,password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        return check_password_hash(self.password,password)
    
class Salon(db.Model):
    __tablename__ = "salon"
    id: Mapped[int] = mapped_column(primary_key=True)
    asignatura: Mapped[str] = mapped_column(String(80),nullable=False)
    profesor_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    estudiante_id: Mapped[str]= mapped_column(String(80),nullable=False)

    alumnnos = Mapped[List["Estudiantes"]]= relationship( back_populates="salon")


    def serialize(self):
        return{
            "salon_id":self.id,
            "asignatura":self.asignatura,
            "estudiante_id": self.estudiantes_id
        }
    
class Calificaciones(db.Model):
    __tablename__ = "calificaciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    calificacion: Mapped[int] = mapped_column(nullable=True)
    
    estudiantes_id: Mapped[int] = mapped_column(Integer,ForeignKey="estudiantes.id")
    profesor_id:Mapped[int] = mapped_column(Integer,ForeignKey="user.id") 
    estudiante: Mapped["Estudiantes"] =relationship(back_populates="calificaiones")
    profesor: Mapped["User"] = relationship(back_populates="calificaiones_realizadas")

    


    def serialize(self):
        return {
            "calificacion_id": self.id,
            "calificacion": self.calificacion,
        }
    
class Asignatura(db.Model):
    __tablename__ = "asignatura"
    id: Mapped[int] = mapped_column(primary_key=True)
    asignatura: Mapped[str] = mapped_column(String(120), nullable=True)

    salones_asignados: Mapped[List["Salon"]] = relationship(back_populates="asignatura")
    def serialize(self):
        return {
            "nombre_asignatura": self.nombre_asignatura,
            "asignatura_id": self.asignatura_id,
        }