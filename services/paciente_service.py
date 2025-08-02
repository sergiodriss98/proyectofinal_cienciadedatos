from typing import List, Optional
import random
import string
from models.paciente import Paciente
from models.metadata import Metadata

class PacienteService:
    def __init__(self):
        self._next_id: int = 1
        self.pacientes: List[Paciente] = []

    def listar(self, n: Optional[int] = None) -> List[Paciente]:
        return self.pacientes[:n] if n is not None else list(self.pacientes)

    def registrar(self, paciente: Paciente) -> Paciente:
        paciente.id = self._next_id
        self._next_id += 1
        self.pacientes.append(paciente)
        return paciente

    def actualizar(self, paciente: Paciente) -> bool:
        existente = self.buscar(paciente.id)
        if not existente:
            return False
        existente.actualizar(
            paciente.id,
            paciente.nombre,
            paciente.edad,
            paciente.metadata
        )
        return True

    def eliminar(self, id: int) -> bool:
        if not self.buscar(id):
            return False
        self.pacientes = [p for p in self.pacientes if p.id != id]
        return True

    def buscar(self, id: int) -> Optional[Paciente]:
        return next((p for p in self.pacientes if p.id == id), None)

    # Métodos auxiliares
    def _generar_metadata_aleatoria(self, id: int) -> Metadata:
        fileName = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".jpg"
        fmt = random.choice(["JPEG", "PNG", "GIF"])
        size = random.randint(100, 5000)
        url = f"https://example.com/files/{fileName}"
        return Metadata(id, fileName, fmt, size, url)

    def crear_paciente_random(self) -> Paciente:
        pid = self._next_id
        paciente = Paciente(pid, nombre="", edad=0)

        nombre = random.choice(["Luis", "Ana", "Carlos", "Marta"])
        edad = random.randint(18, 90)
        metadata = self._generar_metadata_aleatoria(pid)
        paciente.registrar(nombre, edad, metadata)
        return self.registrar(paciente)