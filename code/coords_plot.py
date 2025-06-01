import matplotlib.pyplot as plt

def get_coords(node, x=0, y=0, coords=None, edges=None):
    if coords is None:
        coords = {}
    if edges is None:
        edges = []

    if node is None:
        return x, coords, edges

    x, coords, edges = get_coords(node.left, x, y - 1, coords, edges)

    coords[node] = (x, y)
    if node.left:
        edges.append((node, node.left))
    if node.right:
        edges.append((node, node.right))

    x += 1

    x, coords, edges = get_coords(node.right, x, y - 1, coords, edges)

    return x, coords, edges

def draw_cartesian_tree(root):
    _, coords, edges = get_coords(root)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Координатная визуализация декартова дерева")

    for parent, child in edges:
        x1, y1 = coords[parent]
        x2, y2 = coords[child]
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1)

    for node, (x, y) in coords.items():
        ax.scatter(x, y, color='blue', s=100)
        ax.text(x, y + 0.2, f"{node.key};{node.priority}", ha='center', fontsize=9)

    ax.invert_yaxis()
    ax.grid(True)
    plt.show()
