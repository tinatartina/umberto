#Creazione variabili

x=13

y= "Martina"

print(x)

print(y)

 

#Riassegnazione variabili

x=3     # x è una varibile int

x="cane"  # x è diventata un str

print(x)    

 

#Cambiamento tipo variabili

x=str(3)   #x è una variabile str e sarà "3"

y=int(3)   #y è una variabile int e sarà 3

z=float(3) #z è una variabile float e sarà 3.0

 

#Stampa tipo variabili

x=7

y="gatto"

print(type(x))

print(type(y))

 

#"" e '' sono la stessa cosa

x = "John"

x = 'John'

 

#La stessa lettera maiuscola non sovrascriverà quella minuscola+

a=73

A="kai"

 

#Come posso nominare una variabile per renderla "legale":-Una variabile deve iniziare con una lettera o un _; -Può contenere solo caratter alfa-numerici e _ (A-z, 0-9, _); Le varibaili scritte con la stessa parola cambiano in base ai caratteri (Age,age,AGE)sono variabili diverse

myvar = "John"

my_var = "John"

_my_var = "John"

myVar = "John"

MYVAR = "John"

myvar2 = "John"

 

#Assegnazione variabili su una linea

x, y, z= "papà", "mamma", "ciao"

print(x)

print(y)

print(z)

 

#Come estrarre dei valori e trasformarli in variabili -->(mi stamperà i contenuti della "LISTA")

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)

print(y)

print(z)

 

#funzione print

x = "Python is awesome"

print(x)

 

#print che stampa più variabili

x = "Python"

y = "is"

z = "awesome"

print(x, y, z)

 

#print con il +

x = "Python "

y = "is "

z = "awesome"

print(x + y + z)

 

#+ con operazioni matematiche

x = 5

y = 11

print(x + y)

 

#+ non si può fare con "type" diversi

x = 5

y = "John"

print(x + y)

 

# "," stampa tutti i "type"

x = 5

y = "John"

print(x, y)



#variabile fuori dalla funzione ma che si riesce ad utilizzare nella funzione
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#variabile nella funzione viene stampata e la variabile fuori dalla funzione viene stampata dopo che è stata chiusa la funzione 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#global ti fa utilizzare una variabile che crei all'interno della funzione anche fuori dalla funzione 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#global essendo dentro alla funzione va a cambiare la variabile x e ti stampa solo la x all'interno della funzione 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


