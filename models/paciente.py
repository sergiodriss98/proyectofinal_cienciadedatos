from dataclasses import dataclass
from typing import Optional
from models.metadata import Metadata

@dataclass
class Paciente:
    id: int
    nombre: str
    edad: int
    metadata: Optional[Metadata] = None

    def mostrar(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "metadata": self.metadata.mostrar() if self.metadata else None
        }

    def registrar(self, nombre: str, edad: int, metadata: Metadata):
        self.nombre = nombre
        self.edad = edad
        self.metadata = metadata

    def actualizar(self, id: int, nombre: str, edad: int, metadata: Metadata):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.metadata = metadata

    def eliminar(self, id: int):
        if self.id == id:
            self.id = None
            self.nombre = None
            self.edad = None
            self.metadata = None