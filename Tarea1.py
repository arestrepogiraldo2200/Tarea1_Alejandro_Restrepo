# Alejandro Restrepo Giraldo CC: 1001389709


from funciones import Binomial

# Probabilidad para k = 10
v = Binomial(100,10)*2**(-100)


print("(a) El problema del conteo de k resultados cara en n lanzamientos de una moneda sigue una distribución binomial, para este caso particular su distribución masa de probabilidad es B(n,k) = (n,k)*2^-n con k = 0,1,2,...,n. En el problema requerido se repite el experimento n = 100 veces, luego la probabilidad de obtener exactamente k = 10 caras es B(100,10) = (100,10)*2^-100 = %.20f." %v)


# Suma de las probabilidades de k = 0,1,2,...,29,30.
p = 0
for i in range(0,31):
   p = p + Binomial(100,i)*2**(-100)

# Probabilidad de k >= 30
p = 1 - p

print("(b) Para obtener la probabilidad de obtener más de 30 caras, se debe sumar las probabilidades de k = 31,32,...,99,100. O equivalentemente calcular 1 menos las suma de las probabilidades de k = 0,1,2,...,29,30. Este valor es P(k>30) = 1 - P(k<=30) = %.20f." %p)
 

