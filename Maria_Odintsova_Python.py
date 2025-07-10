def main():

 productos = {'8475HD': ['HP', '15.6', '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '2175HD': ['Acer', '14', '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', '14', '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti']
}

 stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1]}

 print()
 print("!!MENU PRICIPAL!!:")
 print()

 print("1. Stock marca")
 print("2. Busqueda por precio")
 print("3. Listado de productos")
 print("4. salir")
 print()

 option = int(input("Seleccione una opción:"))
 
 if option == 1:
  marca = input("ingrese marca:")
  total = 0
  for modelo in productos:
   if productos[modelo][0].lower() == marca.lower():
    if modelo in stock:
     total += stock[modelo][1]
     print(f"Modelo: {modelo} disponible")
     print(f"stock total de {marca}: {total}")

 if option == 2:
  precio_min = int(input("ingrese precio mainimo:"))
  precio_max = int(input("ingrese precio maximo:"))
  print("Marca del modelo:")
  found = False
  for modelo in productos:
   if modelo in stock:
    precio = stock[modelo][0]
    if precio_min <= precio <= precio_max:
     marca = productos[modelo][0]
     print(f"{marca}-{modelo}")
     found = True
     if not found:
      print("no hay laptops dentro del rango entregado")

 elif option == 3:
  print("marca - modelo - ram - disco")
  print("GB o T)")
  for modelo in productos:
   marca = productos[modelo][0]
   ram = productos[modelo][2]
   tipo_disco = productos[modelo][3]
   capacidad_disco = productos[modelo][4]
   print(f"{marca},{modelo},{ram},{tipo_disco},{capacidad_disco}")
   modelo_buscar = input("ingrese modelo:")
   if modelo_buscar not in productos: print("no hay notebooks disponibles para mostrar")
  else:
   info = productos[modelo_buscar]
   print(f"marca: {info[0]}")
   print(f"pantalla: {info[1]}")
   print(f"ram: {info[2]}")
   print(f"tipo disco: {info[3]}")
   print(f"capacidad: {info[4]}")
   print(f"procesador: {info[5]}")
   print(f"video: {info[6]}")
   if modelo_buscar in stock:
    print(f"precio: ${stock[modelo_buscar][0]}")
    print(f"{stock[modelo_buscar][1]} unidades")

 elif option == 4:
  print("Programa Finalizado")

if_name_= "_main_"
main()
