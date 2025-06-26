from typing import Any, Generator
from Produto import Produto


class Estoque:
    def __init__(self):
        """
        Inicializa um novo estoque vazio, utilizando um dicionário
        onde as chaves são os nomes dos produtos (em letras minúsculas)
        e os valores são instâncias da classe Produto.
        """
        self.produtos = {}

    def adicionar_produto(self, nome:str, preco:float, quantidade:int=1) -> None:
        """
        Adiciona um produto ao estoque. Se o produto já existir (mesmo nome, case-insensitive),
        sua quantidade será incrementada. Caso contrário, ele será criado com a quantidade informada.

        Parâmetros:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
            quantidade (int, opcional): Quantidade a ser adicionada (padrão = 1).
        """
        novo:Produto = Produto(nome, preco, quantidade)
        chave = nome.lower()  # usa o nome em minúsculas como chave para consistência

        # Se o produto ainda não existe, cria uma entrada com quantidade 0
        self.produtos.setdefault(chave, Produto(nome, preco, 0))

        # Usa o método __iadd__ da classe Produto para somar quantidades
        self.produtos[chave] += novo

        print(f"📦 Produto atualizado/adicionado: {nome}")
    
    def remover_produto(self, nome:str, quantidade:int=1) -> None:
        """
        Remove um produto do estoque . Se o produto já existir (mesmo nome, case-insensitive),
        sua quantidade será decrementada. Caso contrário, ele será criado com a quantidade informada
        
        Parâmetros:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
            quantidade (int, opcional): Quantidade a ser adicionada (padrão = 1).
        """ 
        chave = nome.lower()  # usa o nome em minúsculas como chave para consistência
        novo = Produto(nome, self.produtos[chave].preco, quantidade)

        if chave in self.produtos and self.produtos[chave].quantidade > 0:
            if self.produtos[chave].quantidade - novo.quantidade < 0:
                print("A quantidade do produto supera a quantidade em estoque informe uma nova quantidade")
            else:
                # Usa o método __isub__ da classe Produto para subtrair quantidades
                self.produtos[chave] -= novo
        else:
            print(f"Produto {nome} não encontrado ou quantidade insuficiente")

    def listar(self) -> Generator[str, Any, None]:
        """
        Lista todos os produtos no estoque com suas quantidades e preços.

        Retorna:
            generator: Um gerador de strings formatadas com as informações dos produtos.
        """
        print("\n📦 Produtos no estoque:")
        for produto in self.produtos.values():
            yield f"• {produto}"
