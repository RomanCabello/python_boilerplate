"""Main module."""


def comision_anual(objetivo_annual):
    return objetivo_annual / 12


def activos_totales(objetivo_mensual, comision_compartida):
    return objetivo_mensual / (comision_compartida / 12)


def invitados_totales(activos_totales, saldo_promedio_invitados):
    return activos_totales / saldo_promedio_invitados




class Basics:
    def __init__(self):
        self.__comision_sowos = 0.00625
        self.__comision_compartida = self.__comision_sowos * .3

    def execute(self):
        objetivo_annual = int(input("¿Cuál es tu objetivo annual?:\n"))
        saldo_promedio_invitados = int(input("¿Cuál es el saldo promedio de tus invitados?"))

        objetivo_mensual = objetivo_annual / 12
        activos_totales = objetivo_mensual / (self.__comision_compartida / 12)

        invitados_totales = activos_totales / saldo_promedio_invitados

        print(invitados_totales)


if __name__ == '__main__':
    Basics().execute()
