#Considere las siguientes reglas de cocina en su programa:

#1 cda = 3 cdtas
#1 tza = 16 cda
#El 10% del volmen se evapora en el proceso de cocción

#Definimos que una taza son 250 cc en base a información de repostería obtenida en internet, en base a eso sacamos las demás relaciones

print('''Bienvenido usuario a la calculadora de arepas. 
      Ingrese los siguientes ingredientes siguiendo la misma proporción: 
        1 taza agua 
        1 taza harina PAN
        1 cucharadita sal
        1 cucharada aceite''')

agua = int(input("¿Cuántas tazas de agua va a colocar? "))

harina = int(input("¿Cuántas tazas de harina PAN va a colocar? "))

sal = int(input("¿Cuántas cucharaditas de sal va a colocar? "))

aceite = int(input("¿Cuántas cucharadas de aceite va a colocar? "))

print(input('''Estos son los pasos para la preparación:

        En un bol, se vierte el agua, la harina y la sal
        Se mezcla hasta que quede uniforme
        Se le da a la mezcla forma de disco
        Se coloca con el aceite en un budare hasta dorar
        Se voltea y repite
        Se sirve en un plato
        Presione cualquier tecla para continuar: '''))

taza = 250
cucharada = float((1/16)*taza) 
cucharadita = float((1/3)*cucharada)

volumen_tot = float((agua*taza) + (harina*taza) + (sal*cucharadita) + (aceite*cucharada))
volumen_neto = float(round(volumen_tot - ((volumen_tot*10)/100)))

print("El volumen total de su arepa es: ", volumen_neto, 'cc')




