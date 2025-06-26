from typing import Self


class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        """
        Inicializa um novo objeto Produto.

        Parâmetros:
            nome (str): O nome do produto.
            preco (float): O preço unitário do produto.
            quantidade (int): A quantidade disponível do produto.
        """
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __eq__(self, outro: Self) -> bool:
        """
        Compara dois produtos com base no nome (ignorando letras maiúsculas/minúsculas).

        Parâmetros:
            outro (Produto): Outro produto a ser comparado.

        Retorna:
            bool: True se os nomes forem iguais (ignorando maiúsculas/minúsculas), False caso contrário.
        """
        return self.nome.lower() == outro.nome.lower()

    def __hash__(self) -> int:
        """
        Retorna o hash do nome do produto (em letras minúsculas) para garantir consistência
        com a comparação de igualdade.

        Retorna:
            int: Valor de hash do nome.
        """
        return hash(self.nome.lower())

    def __str__(self) -> str:
        """
        Retorna uma representação amigável do produto, adequada para exibição ao usuário.

        Retorna:
            str: Representação formatada do produto.
        """
        return f"{self.nome} - R${self.preco:.2f} (Qtd: {self.quantidade})"

    def __repr__(self) -> str:
        """
        Retorna uma representação detalhada do produto, útil para depuração e logs.

        Retorna:
            str: Representação oficial do objeto.
        """
        return f"Produto(nome={self.nome!r}, preco={self.preco}, quantidade={self.quantidade})"

    def __iadd__(self, outro: Self) -> Self:
        """
        Implementa a operação de adição acumulativa (+=) entre dois produtos com o mesmo nome.

        Parâmetros:
            outro (Produto): Outro produto a ser somado.

        Retorna:
            Produto: O próprio produto com a quantidade atualizada, caso os nomes coincidam.
        """
        if isinstance(outro, Produto) and self == outro:
            self.quantidade += outro.quantidade
        return self

    def __isub__(self, outro: Self) -> Self:
        """
        Implementa a operação de subtração acumulativa (-=) entre dois produtos com
        o mesmo nome.

        Parâmetros:
            outro (Produto): Outro produto a ser subtraído.

        Retorna:
            Produto: O próprio produto com a quantidade atualizada, caso os nomes coincidam.
        """
        if isinstance(outro, Produto) and self == outro:
            self.quantidade -= outro.quantidade
        return self
