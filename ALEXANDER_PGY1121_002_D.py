import os
os.system("cls")

menu = ("""\nmenu\n1.registrar producto\n2.buscar producto\n3.listar productos\n4.salir""")
producto = [0]
digproducto = [0]
categoria = ["tecnologia","alimento","limpieza","decoracion"]
valorprod =[000000]
while True:
    try:
        nombre = input("ingrese su nombre: ")
        apellido = input("ingrese su apellido: ")
        print(menu)
        o = int(input("opcion: "))
        print (o)
        if o == 1:
            print(f"categorias:{categoria}")
            #añadir producto
            prod = input("nombre de producto:  ")
            producto.append(prod)
            #codigo de producto
            dproducto = int(input("ingrese 6 digitos del producto:  ")) 
            digproducto.append(dproducto)       
            #insertar valor
            valor = int(input("insertar valor de producto"))
            valorprod.append(valor)
        elif o == 2:
            code = input("seleccione el codigo de producto")
            print(digproducto[code])
        elif o == 3:
            print("hola")
        elif o == 4:
            print(f"hasta luego {nombre} {apellido} esperamos verte muy pronto!\nCaracol Express version 1.05")
            
            break
        else: 
            print("seleccione un numero de la lista")
    except:
        print("ha ocurrido una excepcion")  
