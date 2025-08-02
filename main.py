from services.paciente_service import PacienteService
from models.paciente import Paciente

if __name__ == "__main__":
    svc = PacienteService()

    print("1. Registro manual de un paciente (sin metadata)")
    p_manual = Paciente(id=0, nombre="María", edad=30)
    svc.registrar(p_manual)
    print(">> Paciente registrado manualmente:")
    print(p_manual.mostrar(), end="\n\n")

    print("2. Creo 3 pacientes con datos aleatorios")
    randoms = [svc.crear_paciente_random() for _ in range(3)]
    print(">> Pacientes aleatorios creados:")
    for p in randoms:
        print(p.mostrar())
    print()

    print(">> Listado completo de pacientes:")
    for p in svc.listar():
        print(f"  • {p}")
    print()

    busq = svc.buscar(2)
    print(">> Búsqueda de paciente con id=2:")
    print(busq.mostrar() if busq else "  — No encontrado")
    print()

    if busq:
        busq.nombre = "Pedro"
        busq.edad = 45
        svc.actualizar(busq)
        print(">> Paciente actualizado (id=2):")
        print(svc.buscar(2).mostrar())
        print()

    eliminado = svc.eliminar(1)
    print(f">> Eliminación de paciente con id=1: {'Éxito' if eliminado else 'No existía'}")
    print()

    print(">> Listado final de pacientes:")
    for p in svc.listar():
        print(f"  • {p}")