def factorial(n):
 if n = 0;
	return 1
 else 
	retur n * factorial(n-1)
def sen(x,n):
	i = 0
	suma = 0
	while i < n:
	        aux = 2*i +1
                suma = ((-1)**i/factorial(aux))*x**aux + suma
	        i += 1
	return suma 
