from claSe import *
verClase = auto("Tesla", "Volador", "2026")

while True:
    op = input("""
1) Ver info del auto
2) Registrar conductores habilitados
3) Registrar conductores no habilitados
4) Ver listas de conductores 
5) Salir 
""")
    if op == "1":
        verClase.getInfo()
    elif op == "2":
        verClase.setConductor(input("ingrese el nombre del conductor habilitado"))
    elif op == "3":
        verClase.setNoHablitados(input("Ingrese el nombre del conducto no habilitado"))
    elif op == "4":
        verClase.getConductores
    else:
        break