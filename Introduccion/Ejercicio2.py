#Ejercicio 2:
#Aplicar formato a las variables mediante el método string.format(). Escriba un programa
#para usar el método string.format() para formatear las siguientes tres variables según la salida esperada.

#Dado:🏹

#totalMoney = 1000
#quantity = 3
#price = 450

#Resultado: Tengo 1000 euros para comprar 3 tarjetas gráficas por 450,00 dólares.

totalMoney = 1000
quantity = 3
price = 450

print(f"Tengo {totalMoney} euros para comprar {quantity} tarjetas gráficas por {price:.2f} dólares.")
