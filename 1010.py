linha1 = input().split(' ')
linha2 = input().split(' ')

id1, quantidade1, valor1 = linha1
id2, quantidade2, valor2 = linha2

quntidade1 = int(quantidade1)
quntidade2 = int(quantidade2)
valor1 = float(valor1)
valor2 = float(valor2)

ValorAPagar = quntidade1 * valor1 + quntidade2 * valor2
print('VALOR A PAGAR: R$ %.2f' %ValorAPagar)
