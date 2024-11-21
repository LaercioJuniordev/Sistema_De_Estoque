from project.models.Estoque import Estoque
from project.models.Item import Item

# Criando itens
item1 = Item(codigo=1, descricao="Cadeira", preco=150.00, quantidade=10)
item2 = Item(codigo=2, descricao="Mesa", preco=300.00, quantidade=5)

# Criando estoque
estoque = Estoque()

# Adicionando itens ao estoque
estoque.adicionar_item(item1)
estoque.adicionar_item(item2)

# Exibindo estoque
estoque.exibir_estoque()

# Atualizando quantidade
estoque.atualizar_quantidade(codigo=1, quantidade=5)

# Buscando um item
item_encontrado = estoque.buscar_item(codigo=1)
print("\nItem encontrado:", item_encontrado)

# Removendo um item
estoque.remover_item(codigo=2)

# Exibindo estoque atualizado
print("\nEstoque atualizado:")
estoque.exibir_estoque()