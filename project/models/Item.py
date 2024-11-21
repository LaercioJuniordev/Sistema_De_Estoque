class Item():
    def __init__(self, codigo:str, descricao:str, preco:int, quantidade:int):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        
    def __str__(self):
        return f"Item: {self.codigo} - {self.descricao} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade}"
    
    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
    
    def atualizar_quantidade(self,nova_quantidade):
        self.quantidade += nova_quantidade
        