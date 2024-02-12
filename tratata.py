class TreeNode: #Создание вершины 
    def __init__(self, val, left, right):
        self.val = val
        self.left = self.right=None

def build_tree(nums): #Создание дерева
    if not nums:      
        return None

    root = TreeNode(nums.pop(0))
    queue = [root]

    while queue:      #Заполнение дерева по ширине(по уровням слева на право)
        current = queue.pop(0)
        if nums:                                       #Левые дети узла
            left_val = nums.pop(0)
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)

        if nums:                                        #Правые дети узла
            right_val = nums.pop(0)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)

    return root

def find_paths(root, target_sum, path=[], paths=[]):     #Функция обработки дерева по условию задачи
    if root is None:
        return []

    path.append(root.val)

    if root.left is None and root.right is None and sum(path) == target_sum:
        paths.append(path[:])

    find_paths(root.left, target_sum, path, paths)
    find_paths(root.right, target_sum, path, paths)

    path.pop()

    return paths

if __name__ == "__main__":
    # Ввод списка чисел для построения дерева
    num_list = list(map(int, input("Введите список чисел для построения дерева, разделенных пробелом(отсутсвующие узлы заполнять как "0"): ").split()))
    target_sum = int(input("Введите целевую сумму: "))

    # Строим дерево из списка чисел
    root = build_tree(num_list)

    # Ищем пути с заданной суммой в дереве
    paths = find_paths(root, target_sum)

    # Выводим найденные пути
    print("Пути с суммой", target_sum, ":")
    for path in paths:
        print("->".join(map(str, path)))
