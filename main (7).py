Exercises=int(input("Introduzca el número del ejercicio que desee ejecutar: "))

if Exercises==17:
  #Número Positivio o negativo
  number = int(input("Por favor ingrese el número: "))
  if (number > 0): 
    print("  El número " + str(number) + " Es positivo")
  else:
    print("El número " + str(number) + " Es negativo")

elif Exercises==18:
  #El Número mayor y el número menor 
  number1 = float(input("Por favor ingrese el número: "))
  number2 = float(input("Por favor ingrese otro número: "))
  if (number1>number2):
    print("El número ", number1, "Es el mayor: ")
  elif (number2>number1):
    print("El número", number1, "Es el menor:")

elif Exercises==19:
  #El número mayor y el número menor entre tres números
  number1 = float(input("Por favor ingrese un número: "))
  number2 = float(input("Por favor ingrese otro número: "))
  number3 = float(input("Por favor ingrese otro número: "))
  if (number1 > number2 > number3):
    print("El número", number1, "Es el mayor y el número ", number3, "Es el menor")
  elif (number1 > number3 > number2):
    print("El número", number1, "Es el mayor y el número ", number2, "Es el menor ")
  elif (number2 > number1 > number3):
    print("El número", number2, "Es el mayor y el número", number3, "Es el menor ")
  elif (number3 > number1 > number2):
    print("El número", number3, "Es el mayor y el número ", number2, "Es el menor ")
  elif (number2 > number3 > number1):
    print("El número", number2, "Es el mayor y el número ", number1, "Es el menor ")
  else:
    print("El número", number3, "Es el mayor y el número ", number1, "Es el menor ")

elif Exercises==20:
  #Salario del empleado
  name = input("Por favor ingrese su nombre: ")
  hours = float(input("Por favor ingrese las horas que normalmente trabaja: "))
  additional = float(input("Por favor ingrese el número de horas extras trabajadas: "))
  if (additional==0):
    print(name, "Su salario es de", hours*4)
  elif (additional >0):
    print(name, "Su salario es de",(hours*4)+(additional*8))

elif Exercises==21:
  #Suma o resta de dos números
  number1 = float(input("Por favor ingrese un número: "))
  number2 = float(input("Por favor ingrese otro número: "))
  if (number1 > number2):
    print("La resta de los dos número es: ", number1-number2)
  elif (number2 > number1):
    print("La suma de los dos números es: ", number1+number2)

elif Exercises==22:
  #El cociente de dos números
  number1 = float(input("Por favor ingrese un número: "))
  number2 = float(input("Por favor ingrese otro número: "))
  if (number2 > 0):
    division=number1/number2
    print("El cociente de estos dos números es:", division)
  elif (number2 == 0):
    print("La división no es válida ya que en matemáticas, la división entre cero es una división en la que el divisor es igual a cero, y que no tiene un resultado bien definido")
elif Exercises ==23:
  #Días de la semana
  numberDay = int(input("Ingrese el número del día de la semana (1-7): "))
  if numberDay == 1:
    print("lunes")
  elif numberDay == 2:
    print("Martes")
  elif numberDay == 3:
    print("Miercoles")
  elif numberDay == 4:
    print("Jueves")
  elif numberDay == 5:
    print("Viernes")
  elif numberDay == 6:
    print("Sabado")
  elif numberDay == 7:
    print("Domingo")
  
elif Exercises==24:
  #indentificar un triangulo equilatero
  number1 = float(input("Por favor ingrese la medida de la primera longitud: "))
  number2 = float(input("Por favor ingrese la medida de la segunda longitud: "))
  number3 = float(input("Por favor ingrese la medida de la tercera longitud: "))
  if number1 == number2 and number1 == number3:
    print("El triangulo es equilatero ")
  elif (number1 != number2 or number1 != number3 or number2 != number3):
    print("El triangulo no es equilatero ")

elif Exercises==25:
  #Suma o multiplicación de dos números 
  number1 = float(input("Por favor ingrese un número: "))
  number2 = float(input("Por favor ingrese otro número: "))
  if (number1 <0 or number2 <0):
    addition = number1 + number2
    print ("La suma de los dos números es: ",addition)
  elif (number1 >0 or number2 >0):
    multiplication= number1 * number2
    print ("La multiplicación de los dos números es: ",multiplication)

elif Exercises==26:
  #Signos zodiacales
  day = int(input("Por favor ingrese el día de su nacimiento: "))
  month = int(input("Por favor ingrese el número del mes de su nacimiento: "))
  if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Usted es Acuario")
  elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Usted es Piscis")
  elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Usted es Aries")
  elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Usted es Tauro")
  elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Usted es Geminis")
  elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Usted es Cancer")
  elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Usted es Leo")
  elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Usted es Virgo")
  elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Usted es Libra")
  elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Usted es Escorpio")
  elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Usted es Sagitario")
  elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Usted es Capricornio")

elif Exercises==27:
  #Area y perimetro de un cuadrilatero
  base = float(input("Por favor ingrese la base del cuadrilatero: "))
  height = float(input("Por favor ingrese la altura del cuadrilatero "))
  #Cuadrado
  if (base == height):
    perimeter1 = base*4
    area1 = base*height
    print("La figura es un cuadrado, su perimetro es ",perimeter1, "y su area es ",area1)
  #Rectangulo
  elif (base != height):
    perimeter2 = (base*2)+(height*2)
    area2 = (base*height)
    print("La figura es un rectangulo, su perimetro es ",perimeter2, "y su area es ",area2)
    
elif Exercises==28:
  #Descuentos
    sale = float(input("Por favor ingrese el valor de la venta: "))
  
    if (sale < 100.0):
      discount1 = sale*5/100
      price1 = sale - discount1
      print("Su descuento es del 5% lo que equivale a ",discount1, "y su compra queda en ",price1)
    
    elif (sale>100 or sale==100) and (sale<200):
      discount2  = sale*10/100
      price2 = sale - discount2
      print("Su descuento es del 10% lo que equivale a ",discount2, "y su compra queda en ",price2)
      
    elif (sale > 200 or sale == 200):
      discount3 = sale*15/100
      price3 = sale - discount3
      print("Su descuento es del 15% lo que equivale a ",discount3, "y su copra queda en ",price3)

elif Exercises == 29:
  #Año bisiesto
  year = int(input("Por favor ingrese el año: "))
  if not year % 4 and (year % 100 or not year % 400):
    print("El año es bisiesto")
  else:
    print("El año no es bisiesto")