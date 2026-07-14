#Sistema de gestion Style Shop

def mostrar_menu():
    print("===============MENU PRINCIPAL==============")
    print("1. Unidades por categoría ")
    print("2. Búsqueda de prendas por rango de precio ")
    print("3. Actualizar precio de prenda ")
    print("4. Agregar prenda ")
    print("5. Eliminar prenda")
    print("6. Salir ")

def leer_opcion():
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Debe ingresar una opcion valida del menu. ")
        except ValueError:
            print("Debe ingresar una opcion entre 1 y 6.")
    return opcion

def validar_texto(texto):
    if texto.strip() != "":
        return True
    else:
        return False

def validar_opcion_sn(opcion):
    if opcion.lower() == "s" or opcion.lower() == "n":
        return True
    else:
        return False
    
def validar_entero_mayor_cero(numero):
    if numero > 0:
        return True
    else:
        return False

def validar_entero_mayor_igual_cero(numero):
    if numero >= 0:
        return True
    else:
        return False
    
def buscar_codigo(codigo, prendas):
    if codigo.upper() in prendas:
        return True
    else:
        return False

def unidades_categoria(categoria, prendas, bodega):
    total = 0
    for codigo in prendas:
        if prendas[codigo][1].lower() == categoria.lower():
            total = total + bodega[codigo][1]
    print("Prendas en Stock:", total)

def busqueda_precio(p_min, p_max, bodega, prendas):
    disponibles = []
    for codigo in bodega:
        precio = bodega[codigo][0]
        unidades = bodega[codigo][1]
        if p_min <= precio <= p_max and unidades > 0:
            nombre = prendas[codigo][0]
            texto = nombre + "--" + codigo
            disponibles.append(texto)
    disponibles.sort()
    if len(disponibles) == 0:
        print("No hay prendas en ese rango de precios. ")
    else:
        for item in disponibles:
            print(item)

def Actualizar_precio(codigo, nuevo_precio, prendas, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, prendas):
        bodega[codigo][0] == nuevo_precio
        return True
    else:
        return False
    
def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, prendas, precio, unidades, bodega):
    codigo.upper()
    if buscar_codigo(codigo, prendas):
        return False
    else:
        prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
        bodega[codigo] = [precio, unidades]
        return True

def eliminar_prenda(codigo, prendas, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, prendas):
        del prendas[codigo]
        del bodega[codigo]
        return True
    else:
        return False

prendas = {
    "S001":["Polera Basica", "Polera", "M", "negro", "algodon", True],
    "S002":["Jeans Slim", "pantalon", "L", "azul", "denin", False],
    "S003":["Chaqueta Urban", "chaqueta", "M", "gris", "poliester", True],
    "S004":["Vestido Sol", "vestido", "S", "rojo", "lino", False],
    "S005":["Poleron Cozy", "poleron", "XL", "verde", "algodon", True],
    "S006":["Camisa Formal", "camisa", "M", "blanco", "algodon", False]
}

bodega = {
    "S001":[7990, 12],
    "S002":[19990, 0],
    "S003":[29990, 3],
    "S004":[24990, 6],
    "S005":[17990, 8],
    "S006":[14990, 2]
}
opcion = 0
while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        categoria = input("Ingrese categoria a consultar: ")
        unidades_categoria(categoria, prendas, bodega)
    elif opcion == 2:
        try:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
            if p_min > 0 and p_max > 0 and p_min <= p_max:
                busqueda_precio(p_min, p_max, bodega, prendas)
            else:
                print("No hay prendas en ese rango de precios. ")
        except ValueError:
            print("Debe ingresar valorte enteros")
    elif opcion == 3:
        continuar = "s"
        while continuar == "s":
            codigo = input("Ingrese codigo de la prenda: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if validar_entero_mayor_cero(nuevo_precio):
                    if Actualizar_precio(codigo, nuevo_precio, prendas, bodega):
                        print("Precio actualizado. ")
                    else:
                        print("El codigo no existe. ")
                else:
                    print("Precio invalido. ")
            except ValueError:
                print("Precio invalido. ")
            continuar = input("¿Desea actualizar otro precio (s/n)?: ")
    elif opcion == 4:
        codigo = input("Ingrese codigo de la prenda: ")
        nombre = input("Ingrese nombre: ")
        categoria = input("Ingrese categoria: ")
        talla = input("Ingrese talla: ")
        color = input("Ingrese color: ")
        material = input("Ingrese material: ")
        es_unisex = input("¿Es unisex?")
        try:
            precio = int(input("Ingrese precio: "))
        except ValueError:
            precio = -1
        try:
            unidades = int(input("Ingrese unidades: "))
        except ValueError:
            unidades = -1
        if (validar_texto(codigo), validar_texto(nombre), validar_texto(categoria), validar_texto(talla), validar_texto(color), validar_opcion_sn(es_unisex), validar_entero_mayor_cero(precio), validar_entero_mayor_igual_cero(unidades)):
            if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas, bodega):
                print("Prenda agregada. ")
            else:
                print("La prenda ya existe.")
        else:
            print("Datos invalidos")
    elif opcion == 5:
        codigo = input("Ingrese codigo de prenda a eliminar: ")
        if eliminar_prenda(codigo, prendas, bodega):
            print("Prenda eliminada")
        else:
            print("La prenda no existe")
    elif opcion == 6:
        print("Programa finalizado. ")