class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def ImprimeArvoreRecurs(raiz, nivel, cont):
    if (raiz == None):
        return nivel

    # Imprime Filhos à Direita
    nivel = ImprimeArvoreRecurs(raiz.direita, nivel + 1, cont)
    print()
    for i in range(cont[0], nivel):
        print(end=" ")
    print(f"{raiz.chave}")

    # Imprime Filhos à Esquerda
    nivel = ImprimeArvoreRecurs(raiz.esquerda, nivel + 1, cont)
    return nivel

def ImprimeArvore(raiz):
    cont = [10]
    nivel = ImprimeArvoreRecurs(raiz, 0, cont)

if __name__ == '__main__':
    raiz = NoArvore(6)
    raiz.esquerda = NoArvore(8)
    raiz.direita = NoArvore(4)

    ImprimeArvore(raiz)

    raiz2 = NoArvore(55)
    raiz2.esquerda = NoArvore(35)
    raiz2.direita = NoArvore(75)

    raiz2.direita.esquerda = NoArvore(65)
    raiz2.direita.direita = NoArvore(85)
    raiz2.esquerda.esquerda = NoArvore(25)
    raiz2.esquerda.direita = NoArvore(45)

    ImprimeArvore(raiz2)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Criação da árvore
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traversing (percorrendo) a árvore em ordem (in-order traversal)
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

in_order_traversal(root)  

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)
def DeleteBST(raiz, chave):
  if raiz is None: 
      return raiz
  if chave < raiz.chave:
      raiz.esquerda = DeleteBST(raiz.esquerda, chave)
  elif(chave > raiz.chave):
      raiz.direita = DeleteBST(raiz.direita, chave)
  else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
         temp = raiz.esquerda
         raiz = None
         return temp
        temp = ValorNo(raiz.direita)
        raiz.chave = temp.chave
        raiz.direita = DeleteBST(raiz.direita, temp.chave)
  return raiz

def DeleteBST(raiz, chave):
    if raiz is None: 
        return raiz
    if chave < raiz.chave:
        raiz.esquerda = DeleteBST(raiz.esquerda, chave)
    elif(chave > raiz.chave):
        raiz.direita = DeleteBST(raiz.direita, chave)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
            temp = ValorNo(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = DeleteBST(raiz.direita, temp.chave)
            return raiz

# Criação da BST
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

in_order_traversal(root)  


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def is_bst(root, prev=[None]):
    if root:
        if not is_bst(root.left, prev):
            return False
        if prev[0] is not None and root.value <= prev[0].value:
            return False
        prev[0] = root
        return is_bst(root.right, prev)
    return True

# Criação de uma árvore binária de busca
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

if is_bst(root):
    print("É uma árvore binária de busca.")
else:
    print("Não é uma árvore binária de busca.")

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")  # Visitar o próprio nó
        in_order_traversal(root.right)

# Criação de uma árvore binária de busca
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

# Realiza o percurso em ordem simétrica
in_order_traversal(root)  # Saída: 3 5 7 10 15
