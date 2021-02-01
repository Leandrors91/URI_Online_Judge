nome = input()
salario = float(input())
valorDeVendas = float(input())
salarioComBonos = salario + valorDeVendas * 0.15
print('TOTAL = R$ {:.2f}'.format(salarioComBonos))
