from dataclasses import dataclass
from typing import List, Optional
from models.paciente import Paciente

@dataclass
class Gestor:
    pacientes: List[Paciente]

    def listar(self) -> List[dict]:
        return [paciente.mostrar() for paciente in self.pacientes]

    def registrar(self, paciente: Paciente) -> None:
        self.pacientes.append(paciente)

    def actualizar(self, id: int, nuevo_paciente: Paciente) -> bool:
        for i, paciente in enumerate(self.pacientes):
            if paciente.id == id:
                self.pacientes[i] = nuevo_paciente
                return True
        return False

    def eliminar(self, id: int) -> bool:
        for i, paciente in enumerate(self.pacientes):
            if paciente.id == id:
                del self.pacientes[i]
                return True
        return False