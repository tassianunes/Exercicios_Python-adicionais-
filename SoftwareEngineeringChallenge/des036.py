print('\033[31m-\033[m'* 25)
print('Bem vindo ao \033[32mCREDIFÁCIL\033[m!')
print('\033[31m-\033[m'*25)
VarCasa = float(input('Quanto custa a casa: '))
VarSalario = float(input('Quanto você recebe: '))
VarParcelas = int(input('Quantos anos de financiamento: '))
VarPrestacao = VarCasa/(VarParcelas * 12)
if VarPrestacao < (30*VarSalario)/100:
    print('Para pagar uma casa de \033[32m{}\033[m em \033[32m{}\033[m anos com o salário de \033[32m{}\033[m, a prestação será de \033[32m{:.2f}\033[m'.format(VarCasa,
                                                                                                        VarParcelas,
                                                                                                        VarSalario,
                                                                                                        VarPrestacao))
    print('\033[32mEmprestimo CONCEDIDO')
else:
    print('Para pagar uma casa de \033[32m{}\033[m em \033[32m{}\033[m anos com o salário de \033[32m{}\033[m, a prestação será de \033[32m{:.2f}\033[m'.format(
            VarCasa,
            VarParcelas,
            VarSalario,
            VarPrestacao))
    print('\033[31mEmpréstimo NEGADO')