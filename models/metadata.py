from dataclasses import dataclass

@dataclass
class Metadata:
    id: int
    fileName: str
    format: str
    size: int
    url: str

    def mostrar(self) -> dict:
        return {
            "id": self.id,
            "fileName": self.fileName,
            "format": self.format,
            "size": self.size,
            "url": self.url
        }

    def registrar(self, fileName: str, format: str, size: int, url: str):
        self.fileName = fileName
        self.format = format
        self.size = size
        self.url = url

    def actualizar(self, id: int, fileName: str, format: str, size: int, url: str):
        self.id = id
        self.fileName = fileName
        self.format = format
        self.size = size
        self.url = url

    def eliminar(self, id: int):
        if self.id == id:
            self.id = None
            self.fileName = None
            self.format = None
            self.size = None
            self.url = None