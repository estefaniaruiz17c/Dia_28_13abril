# Librería Matplotlib - diccionarios
print("Librería Matplotlib - diccionarios")

# Importemos las librerias que vamos a utilizar
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Primer ejericio: En un salón de 48 personas, se les preguntó sobre su color fdavorito. Se recopilarán todos los datos en una gráfica

# Para acceder al archivo de texto de 'arch1.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
color = open('Colores.txt','r')
texto1lis = color.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
color.close()

print(texto1lis)

# Creación del diccionario: las claves corresponden a los colores y los valores a la cantidad de votos por ese color

clave1 = (texto1lis[0].rstrip('\n'))
valor1 = (texto1lis[1].rstrip('\n'))
clave2 = (texto1lis[2].rstrip('\n'))
valor2 = (texto1lis[3].rstrip('\n'))
clave3 = (texto1lis[4].rstrip('\n'))
valor3 = (texto1lis[5].rstrip('\n'))
clave4 = (texto1lis[6].rstrip('\n'))
valor4 = (texto1lis[7].rstrip('\n'))
clave5 = (texto1lis[8].rstrip('\n'))
valor5 = (texto1lis[9].rstrip('\n'))

votos1 = {clave1:int(valor1), clave2:int(valor2), clave3:int(valor3), clave4:int(valor4), clave5:int(valor5)}

print()
print("Diccionario: ",votos1)
print()

colores1 =["turquoise","limegreen","hotpink","yellow","blueviolet"]

# Creación de la gráfica y estilo de la misma
plt.bar(votos1.keys(),  votos1.values() , color=colores1)

# Establecer nombres de los ejes
plt.xlabel ('Colores')
plt.ylabel('Cantidad de votos')

# Establecer título de la gráfica
plt.title('Encuesta: Colores favoritos')

# Guardar en formato PNG
plt.savefig("Colores fav.png")

# Cerrar la ejecución de la gráfica
plt.close()

print("---------"*7)

# Segundo ejericio: Se hace el análisis comparativo del promedio en las calificaciones de 4 grupos del grado 10 de un colegio.

# Para acceder al archivo de texto de 'Calificaciones.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
calif = open('Calificaciones.txt','r')
texto2lis = calif.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
color.close()

print(texto2lis)

# Creación del diccionario: las claves corresponden a los colores y los valores a la cantidad de votos por ese color

key1 = (texto2lis[0].rstrip('\n'))
value1 = (texto2lis[1].rstrip('\n'))
key2 = (texto2lis[2].rstrip('\n'))
value2 = (texto2lis[3].rstrip('\n'))
key3 = (texto2lis[4].rstrip('\n'))
value3 = (texto2lis[5].rstrip('\n'))
key4 = (texto2lis[6].rstrip('\n'))
value4 = (texto2lis[7].rstrip('\n'))

promedios2 = {key1:float(value1), key2:float(value2), key3:float(value3), key4:float(value4)}

print()
print("Diccionario 2: ",promedios2)
print()

colores_cal =["lightskyblue","salmon","palegreen","plum"]

# Creación de la gráfica y estilo de la misma
plt.pie(promedios2.values() , labels = promedios2.keys(), colors=colores_cal, autopct =("%0.2f%%") )

# Establecer título de la gráfica
plt.title('Calificaciones grado 10')

# Guardar en formato PNG
plt.savefig("Promedio calificaciones.png")

# Cerrar la ejecución de la gráfica
plt.close()