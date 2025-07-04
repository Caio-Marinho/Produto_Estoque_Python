from typing import Any, Generator, Optional
from Produto import Produto


class Estoque:
    def __init__(self) -> None:
        """
        Inicializa um novo estoque vazio, utilizando um dicionário
        onde as chaves são os nomes dos produtos (em letras minúsculas)
        e os valores são instâncias da classe Produto.
        """
        self.produtos = {}

    def adicionar_produto(self, nome: str, preco: float, quantidade: int = 1) -> None:
        """
        Adiciona um produto ao estoque. Se o produto já existir (mesmo nome, case-insensitive),
        sua quantidade será incrementada. Caso contrário, ele será criado com a quantidade informada.

        Parâmetros:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
            quantidade (int): Quantidade do produto (padrão: 1).
        """
        novo: Produto = Produto(nome, preco, quantidade)
        chave = nome.lower()

        self.produtos.setdefault(chave, Produto(nome, preco, 0))
        self.produtos[chave] += novo

        print(f"📦 Produto atualizado/adicionado: {nome}")

    def remover_produto(self, nome: str, quantidade: int = 1) -> None:
        """
        Remove um produto do estoque, decrementando a quantidade.
        Se a quantidade a ser removida for maior que a disponível, 
        uma mensagem de erro será exibida.

        Parâmetros:
            nome (str): Nome do produto a ser removido.
            quantidade (int): Quantidade a ser removida. Padrão é 1.
        """
        chave = nome.lower()

        if chave in self.produtos and self.produtos[chave].quantidade > 0:
            if self.produtos[chave].quantidade - quantidade < 0:
                print("❌ Quantidade solicitada para remoção excede o estoque.")
            else:
                preco = self.produtos[chave].preco
                novo = Produto(nome, preco, quantidade)
                self.produtos[chave] -= novo
                print(f"🗑️ Produto removido: {nome}, Quantidade: {quantidade}")
        else:
            print(f"❌ Produto '{nome}' não encontrado ou com estoque insuficiente.")

    def atualizar_valor(self, nome: str, preco: float) -> None:
        """
        Atualiza o valor de um produto no estoque.

        Parâmetros:
            nome (str): Nome do produto a ser atualizado.
            preco (float): Novo preço do produto.
        """
        chave = nome.lower()
        if chave in self.produtos:
            self.produtos[chave].preco = preco
            print(f"💰 Preço do produto '{nome}' atualizado para R$ {preco:.2f}")
        else:
            print(f"❌ Produto '{nome}' não encontrado.")

    def atualizar_nome(self, nome_antigo: str, nome_novo: str) -> None:
        """
        Atualiza o nome de um produto no estoque, modificando a chave correspondente 
        no dicionário de produtos. O nome é tratado de forma case-insensitive.

        Parâmetros:
            nome_antigo (str): Nome atual do produto a ser alterado.
            nome_novo (str): Novo nome que será atribuído ao produto.

        Observações:
            - Se o produto com nome_antigo não for encontrado, uma mensagem será exibida.
            - Se já existir um produto com o nome_novo, a operação será cancelada para evitar conflito.
        """
        chave_antiga = nome_antigo.lower()
        chave_nova = nome_novo.lower()

        if chave_antiga not in self.produtos:
            print(f"❌ Produto '{nome_antigo}' não encontrado.")
            return

        if chave_nova in self.produtos:
            print(f"⚠️ Já existe um produto com o nome '{nome_novo}'.")
            return

        produto = self.produtos.pop(chave_antiga)
        produto.nome = nome_novo
        self.produtos[chave_nova] = produto
        print(f"🔄 Nome do produto atualizado: '{nome_antigo}' → '{nome_novo}'")

    def listar(self) -> Generator[str, Any, None]:
        """
        Lista todos os produtos no estoque com suas quantidades e preços.

        Retorna:
            generator: Um gerador de strings com informações formatadas dos produtos.
        """
        print("\n📦 Produtos no estoque:")
        if not self.produtos:
            yield "⚠️ Estoque vazio."
        else:
            for produto in self.produtos.values():
                yield f"• {produto}"
        yield "📄 Fim da listagem."

    def obter_produto(self, nome: str) -> Optional[Produto]:
        """
        Retorna o produto pelo nome (case-insensitive), se existir.

        Parâmetros:
            nome (str): Nome do produto a ser procurado.

        Retorna:
            Produto ou None se não encontrado.
        """
        return self.produtos.get(nome.lower())
