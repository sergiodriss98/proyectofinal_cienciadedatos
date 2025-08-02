# Proyecto Gestión de Pacientes Covid-19

## Descripción

Proyecto para gestionar pacientes y metadatos asociados a imágenes médicas.  
Permite registrar, actualizar, eliminar y listar pacientes y sus metadatos mediante una interfaz de terminal.

## Estructura del Proyecto

proyecto_imagenes/
├── main.py
├── models/
│ ├── metadata.py
│ └── paciente.py
├── services/
│ └── paciente_service.py
├── venv/ # Entorno virtual (no subir al repositorio)
└── README.md

## Requisitos

- Python 3.8 o superior
- pip actualizado

---

## Instalación

1. Clonar el repositorio.

2. Crear y activar un entorno virtual (Opcional):

```bash
  python -m venv venv
  # Windows
  venv\Scripts\activate
  # Linux/Mac
  source venv/bin/activate
```

3. Actualizar pip:

```bash
 python -m pip install --upgrade pip
```

4. Uso

- Ejecutar el script principal con:

```bash
  python main.py
```

5. Salir de Venv

```bash
  deactivate
```

Good Luck Guys! 
