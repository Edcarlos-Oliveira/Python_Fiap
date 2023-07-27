from identificacaoDeFuncoes import *

mylist = []
print('Preenchendo!!')
preencher_inventario(mylist)

print('Exibindo!!!')
exibir_inventario(mylist)

print('Pesquisando!!!')
localizar_nome(mylist)

print('Alterando!!!')
depreciar_item(mylist, 20)

print('Excluindo...')
print(remover_serial(mylist))
exibir_inventario(mylist)

print('Resumindo!!!')
resumir_valores(mylist)
