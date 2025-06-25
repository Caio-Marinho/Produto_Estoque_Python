from Estoque import Estoque

estoque = Estoque()

estoque.adicionar_produto("Notebook", 3500, 2)
estoque.adicionar_produto("Notebook", 3500, 3)
estoque.adicionar_produto("Celular", 2500)
estoque.adicionar_produto("Celular", 2500,4)
for item in estoque.listar():
    print(item)
estoque.remover_produto("Notebook", 6)
for item in estoque.listar():
    print(item)
estoque.remover_produto("Notebook", 5)
for item in estoque.listar():
    print(item)