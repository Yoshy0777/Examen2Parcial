# Importamos la libreria canvas del paquete reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import random
import qrcode
from datetime import date
from datetime import datetime
ruta = "C:/Users/FRANKILIJOSHY/Desktop/Examen2Parcial/"
c = canvas.Canvas(ruta+'Reporte2Parcial.pdf')

#Aqui inicia el codigo del super mercado

nombre = input("Ingresa tu nombre: ")
correo = input("Ingresa tu correo electrónico: ")

despensa = ["Papitas", "Celulares", "Alita de pollo", "Coca cola", "envase de jugo"]
costo = [25,3500,10.5,20.99,9.5]
list = ["1.-","2.-","3.-","4.-","5.-"]
cantidades = [0,0,0,0,0]
carrito = [0,0,0,0,0]
opcion=1
contadorElementos = 0;
print(" ")
print("Bienvenido a Walmart")
print("   |Costo|     |Nombre del producto|")
for i,i2,i3 in zip (despensa, costo, list):
    print(i3,"$",i2,"       ",i)


while opcion == 1:
    opcion2 = int(input("Selecciona alguno de los siguientes productos: "))
    if (opcion2==1):
        piezas = int(input("¿Cuantas bolsas de papa vas a comprar? "))
        cantidades[0] = cantidades[0]+piezas
        carrito[0] = (cantidades[0]*costo[0])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1.Si 2.No "))
    elif(opcion2==2):
        piezas = int(input("¿Cuantos celulares vas a comprar? "))
        cantidades[1] = cantidades[1]+piezas
        carrito[1] = (cantidades[1]*costo[1])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==3):
        piezas = int(input("¿Cuantas alitas de pollo vas a comprar? "))
        cantidades[2] = cantidades[2]+piezas
        carrito[2] = (cantidades[2]*costo[2])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==4):
        piezas = int(input("¿Cuantos envases de Coca Cola vas a comprar? "))
        cantidades[3] = cantidades[3]+piezas
        carrito[3] = (cantidades[3]*costo[3])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==5):
        piezas = int(input("¿Cuantos envase de jugo vas a comprar? "))
        cantidades[4] = cantidades[4]+piezas
        carrito[4] = (cantidades[4]*costo[4])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    else:
        print("Producto no disponible, porfavor seleccione uno disponible ")

print("Carrito de compras: ")
print(" ")
print("|Cantidad|   |Precio del producto|   |TotalProducto|   |Nombre del producto|")

for i,i2,i3,i4 in zip(cantidades, costo, carrito, despensa):
    print(" ",i,"           ","$",i2,"                  ","$",i3,"               ",i4)

TotalPagar = sum(carrito)

print("El total a pagar es de: $",TotalPagar)
Pago = input("¿Con cuanto va a pagar?")
UsuarioPago = float(Pago)
Cambio = UsuarioPago-TotalPagar
print("El usuario pago un total de: $",UsuarioPago)
if (UsuarioPago<TotalPagar):
   print("Lo siento, pero te falta dinero para pagar el total")
else:
    print("Tu cambio es de: $"+"{:.2f}".format(Cambio))

print("Articulos vendidos: ",contadorElementos)
#Aqui termina el codigo del super mercado

#Inicia el codigo para imprimir el ticket en pdf

now = datetime.now().replace(microsecond=0)
imagen = ruta + "Walmart.png"
c.drawImage(imagen,220,780,150,80,mask="auto")
c.setFont('Helvetica', 15)
c.drawString(35,789,"---------------------------------------------------------------------------------------------------------")
c.setFont('Helvetica', 12)
c.drawString(200,780,f"Nombre del cliente: {nombre}")
c.drawString(175,765,f"Correo electrónico: {correo}")
c.setFont('Helvetica-Bold',16)
c.drawString(20,740,"==========")
c.drawString(480,740,"==========")
c.drawString(210,740,"Productos comprados")
c.setFont('Helvetica-Bold', 16)
c.drawString(55,720,"Nombre del producto:")
c.drawString(250,720,"Cantidad: ")
c.drawString(370,720,"Precio del producto: ")
c.setFont('Helvetica', 16)

PosY = 690

for a,a2,a3 in zip(despensa,cantidades,carrito):
    c.drawString(95,PosY,f"{a}")
    c.drawString(260,PosY,f"{a2}")
    c.drawString(400,PosY,f"{a3}")
    #PosX = PosX-10
    PosY = PosY-20



c.drawString(300,560,"EL TOTAL: $"+str("{:.2f}".format(TotalPagar)))
c.drawString(300,540,"Efectivo/transferencia: $"+str(UsuarioPago))
if(UsuarioPago<TotalPagar):
    c.drawString(300,520,"Lo siento, pero te falta dinero para pagar el total")
else:
    c.drawString(300,520,"CAMBIO: $"+str("{:.2f}".format(Cambio)))
def Random():
    return str(random.randint(100000,999999))    
c.drawString(200,480,f"TC#       {Random()}")
c.drawString(180,440,"ARTICULOS VENDIDOS:          "+str(contadorElementos))
c.setFont('Helvetica-Bold',20)
c.drawString(30, 400,("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"))

informacion = f"C.R. {Random()} Productos comprados en total: {contadorElementos} Total: ${TotalPagar}Fecha de la compra: {now.strftime('%Y:%M:%D')}"
img = qrcode.make(informacion)
nombreImagen = ruta + "miQR.png"
f = open(nombreImagen, "wb")
img.save(f)
f.close()

c.drawImage(nombreImagen,220,200,150,150)
c.setFont('Helvetica',18)
c.drawString(225,170,now.strftime("%Y %D %M"))




#Termina el codigo para imprimir el ticket en pdf

c.save()