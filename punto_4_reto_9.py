import time

start_time = time.time()

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        max = 1
        for _ in range(2, n):
            a, b = b, a + b
            if b > max:
                max = b
        return max

n = int(input("ingrese el digito de la secuencia: "))

while True:
  if time.time() - start_time < 5:

    ultimo = fib(n)
    print(f"El número de Fibonacci en {n} es {ultimo}")
    break
  print("el tiempo se exedio")
  break

end_time = time.time()

timer = end_time - start_time
print(f"se demoro {timer:.2f} segundos")