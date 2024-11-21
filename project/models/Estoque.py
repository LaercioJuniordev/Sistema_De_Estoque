class Estoque:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        for existente in self.itens:
            if existente.codigo == item.codigo:
                existente.atualizar_quantidade(item.quantidade)
                return
        self.itens.append(item)

    def remover_item(self, codigo):
        self.itens = [item for item in self.itens if item.codigo != codigo]

    def atualizar_quantidade(self, codigo, quantidade):
        for item in self.itens:
            if item.codigo == codigo:
                item.atualizar_quantidade(quantidade)
                return
        print(f"Item com código {codigo} não encontrado.")

    def buscar_item(self, codigo=None, descricao=None):
        for item in self.itens:
            if (codigo and item.codigo == codigo) or (descricao and descricao.lower() in item.descricao.lower()):
                return item
        return None

    def exibir_estoque(self):
        for item in self.itens:
            print(item)
