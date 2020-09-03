# Alejandro Restrepo Giraldo CC: 1001389709

from funciones import Factorial
from funciones import Binomial
from funciones import Pascal

print("Prueba de que la función de factorial calcula correctamente. Los i! con i = 1,2,3,4,5 deben dar respectivamente 1,2,6,24,120.")

for i in range(1,6):
   print("Factorial(%d) = %d" %(i,Factorial(i)))



print("\n Prueba de que la función de coeficiente binomial calcula correctamente. Con i = 2,3,4,5 y j = 2,3 deben dar respectivamente los coeficentes binomiales (2,2) = 1, (3,2) = 3, (3,3) = 1, (4,2) = 6, (4,3) = 4, (5,2) = 10, (5,3) = 10")

for i in range(2,6):
   for j in range(2,4):
      if (i==2 and j==3):
         continue
      print("Binomial(%d,%d) = %d" %(i,j,Binomial(i,j)))

print("\nPrueba de que la función de triángulo de pascal calcula correctamente. Para n = 9 se retorna:")
Pascal(9)
print("\nSe puede comprobar su correcta escritura en el archivo Pascal_n.txt")



