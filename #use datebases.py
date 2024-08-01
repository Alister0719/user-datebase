#use datebases
import os
import time

# Funcion que crea los archivos
def make_file(file_name):
   match file_name:
      case "clientes.txt":
         try:
            lines=[]
            lines.append("112540139,Esteban,Monge,mongejimenezcr@gmail.com\n")
            lines.append("112540140,Francisco,Monge,sempaispace@gmail.com\n")
            file=open(file_name,"w")
            file.writelines(lines)
            file.close()
            print("Archivo: "+file_name+" creado")
         except PermissionError:
            print("Por favor revise los permisos del directorio")
         except:
            print("Error desconocido, por favor contacte al administrador")
      case "productos.txt":
         try:
            lines=[]
            lines.append("1,Ron Flor de Caña,7500,975,8475\n")
            lines.append("2,Ron Centenario,7000,910,7910\n")
            file=open(file_name,"w")
            file.writelines(lines)
            file.close()
            print("Archivo: "+file_name+" creado")
         except PermissionError:
            print("Por favor revise los permisos del directorio")
         except:
            print("Error desconocido, por favor contacte al administrador")
      case "sucursales.txt":
         try:
            lines=[]
            lines.append("1,Desamparados,Frente a la municipalidad,86609111\n")
            lines.append("2,Aserri,Frente a la municipalidad,22300555\n")
            file=open(file_name,"w")
            file.writelines(lines)
            file.close()
            print("Archivo: "+file_name+" creado")
         except PermissionError:
            print("Por favor revise los permisos del directorio")
         except:
            print("Error desconocido, por favor contacte al administrador")
      case _:
         print("Archivo inválido")

# Funcion que muestra el menu cada vez que el usuario lo desa
def menu():
   print("Bienvenido a el supermercado")
   print("1. Mostrar todas los clientes")
   print("2. Mostrar todos los productos")
   print("3. Mostrar todas las sucursales")
   print("4. Vender")
   print("x. Salir")

# Funcion que limpia la pantalla
def clear_screen():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')

# Funcion que parmite leer todo el contenido de un archivo
def read_file(file_name):
   with open(file_name,"r") as file:
      for line in file:
        print(line.replace("\n",""))

# Funcion para crear respaldos
def make_backup(file_name):
   datetime = time.strftime("%Y%m%d-%H%M%S")
   if os.name == 'nt':
      os.system('copy '+file_name+' '+file_name+datetime+'.BAK')
   else:
      os.system('cp '+file_name+' '+file_name+datetime+'.BAK')

# Funcion que busca una sucursal 
def read_branch(file_name,id_branch):
   with open(file_name,"r") as file:
      branch_found=""
      for line in file:
         line_list=line.split(",")
         if line_list[0] == str(id_branch):
            branch_found = line
            break
      if branch_found != "":
         return branch_found.replace("\n","")
      else:
         return False

# Funcion que busca un producto 
def read_product(file_name,id_product):
   with open(file_name,"r") as file:
      product_found=""
      for line in file:
         line_list=line.split(",")
         if line_list[0] == str(id_product):
            product_found = line
            break
      if product_found != "":
         return product_found.replace("\n","")
      else:
         return False

# Funcion que busca un producto
def read_client(file_name,id_client):
   with open(file_name,"r") as file:
      client_found=""
      for line in file:
         line_list=line.split(",")
         if line_list[0] == str(id_client):
            client_found = line
            break
      if client_found != "":
         return client_found.replace("\n","")
      else:
         return False

def print_invoice(branch,product,client):
   branch_list=branch.split(",")
   product_list=product.split(",")
   if client:
      client_list=client.split(",")
   print("==== Super mercado ====")
   print("Sucursal: "+branch_list[1])
   print("Direccion: "+branch_list[2])
   print("WhatsApp: "+branch_list[3])
   if client:
      print("ID: "+client_list[0])
      print("Nombre: "+client_list[1],client_list[2])
      print("Correo: "+client_list[3])
   print("==== Lineas de venta ====")
   print("Producto: "+product_list[1])
   print("Precio bruto: "+product_list[2])
   print("Impuestos: "+product_list[3])
   print("Precio neto: "+product_list[4])
   print("==== Gracias por su compra ====")

# Funcion principal
for file_name in 'clientes.txt','productos.txt','sucursales.txt':
   if os.path.isfile(file_name):
      print("Archivo existe")
      make_backup(file_name)
   else:
      print("Archivo no existe")
      make_file(file_name)

opcion=""
while opcion != "x":
   menu()
   opcion=input("Digite una opción: ")
   match opcion:
      case "1":
         read_file('clientes.txt')
         input("Presione una tecla para continuar...")
         clear_screen()
      case "2":
         read_file('productos.txt')
         input("Presione una tecla para continuar...")
         clear_screen()
      case "3":
         read_file('sucursales.txt')
         input("Presione una tecla para continuar...")
         clear_screen()
      case "4":
         read_file('sucursales.txt')
#         try:
         id_branch=int(input("Digite el numero de sucursal: "))
         sucursal=read_branch('sucursales.txt',id_branch)
         if sucursal:
            read_file('productos.txt')
            id_product=int(input("Digite el id de producto: "))
            producto=read_product('productos.txt',id_product)
            if producto:
               factura=input("Desea factura S/N: ").upper()
               if factura == "S":
                  read_file('clientes.txt')
                  id_client=int(input("Digite el id de producto: "))
                  cliente=read_client('clientes.txt',id_client)
                  if not cliente:
                     print("Cliente inválido... se factura sin cliente")
                     input("Presione una tecla para continuar...")
                     clear_screen()
               else:
                  cliente=False
               print_invoice(sucursal,producto,cliente) 
            else:
               print("Producto inválido...")
               input("Presione una tecla para continuar...")
               clear_screen()
         else:
            print("Sucursal inválida...")
            input("Presione una tecla para continuar...")
            clear_screen()

#         except:
#            print("Sucursal debe ser un número...")
#            input("Presione una tecla para continuar...")
#            clear_screen()
      case "x":
         print("Gracias vuelve pronto... se va por la sombra")
      case _:
         print("Opcion inválida")

