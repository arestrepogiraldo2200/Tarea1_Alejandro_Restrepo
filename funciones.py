# Alejandro Restrepo Giraldo CC: 1001389709

# Librerías
import sys

# Función de factorial
def Factorial(n):

   # Rutina para detectar sólo entradas de números enteros.
   # Afecta también a Binomial(n,k).
   if n-int(n) != 0:
      print("Solo se aceptan enteros como entradas.")
      sys.exit()

   prod = 1
   # Ciclo de la productoria
   for i in range(1,n+1):
      prod = prod*i
   return int(prod)


# Función de Coeficiente binomial
def Binomial(n,k):
   
   # Cálculo del coeficiente usando la función Factorial(n)
   coef = Factorial(n)/(Factorial(k)*Factorial(n-k))
   return int(coef)

# Función de triángulo de Pascal
# Se imprime por terminal y se guarda en archivo Pascal-n.txt

def Pascal(n):

   # Se crea archivo para guardar la figura
   file = open('Pascal-n.txt', 'w')

   for i in range(0,n+1):
      # Formato de saltos de columna de dos espacios
      print("n = %d" %i,end="")
      file.write("n = ")
      file.write(str(i))
      for k in range(0,n-i+2):
         print("  ", end="")
         file.write("  ")
      for j in range(0,i+1):
         # Término del triángulo
         b = Binomial(i,j)
         print(b, end="")
         file.write(str(b))
         # Formato
         if (b<10):
            print("   ", end="")
            file.write("   ")
         if (9 < b and b < 100):
            print("  ", end="")
            file.write("  ")
         if (99 < b and b< 1000):
            print(" ", end="")
            file.write(" ")
      print("")
      file.write("\n")
   file.close()
   print("\n Figura guardada en Pascal-n.txt")

















