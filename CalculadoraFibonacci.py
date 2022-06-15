N = int(input("Escolha um número: "))

N1 = 0
N2 = 1

for i in range(0, N):
    N3 = N1 + N2
    N1 = N2
    N2 = N3

print("O Fibonacci de " + str(N) + " é o número: " + str(N1))
