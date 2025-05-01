# Pre-order traversal
def pre_order(node):
    if node is None:
        return []

    result = [node.value]
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))

    return result

# In-order traversal
def in_order(node):
    if node is None:
        return []

    result = in_order(node.left)
    result.append(node.value)
    result.extend(in_order(node.right))

    return result

# Post-order traversal
def post_order(node):
    if node is None:
        return []

    result = post_order(node.left)
    result.extend(post_order(node.right))
    result.append(node.value)

    return result
