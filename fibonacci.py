def fib(n):

    fib_arr = [0, 1]

    fib_val = fib_arr[-1]

    while True:

        fib_val = fib_arr[-1] + fib_arr[-2]

        fib_arr.append(fib_val)

        if n in fib_arr:
            return True

        if fib_val > n:
            return False


def res(n):

    if fib(n):
        print(f"O valor {n} pertence a sequencia de fibonacci!")
    else:
        print(f"O valor {n} não pertence a sequencia de fibonacci")


valor = int(
    input("Digite um valor para verificar se contem na sequencia de fibonacci: "))

res(valor)
