from ex1.mapping import RAW_MAPPING


def build_roles_tree(mapping_data):
    """
    :param mapping_data: маппинг ролей в категории
    :return: дерево ролей
    """

    categories = mapping_data.get('categories')
    roles = mapping_data.get('roles')

    for role in roles.values():
        role['text'] = role.pop('name')

    sorted_list = mapping_data.get('categoryIdsSorted')
    full_categories = {'categories': []}

    for category_id in sorted_list:
        full_categories['categories'].append(categories.get(category_id))

    for cat in full_categories['categories']:
        cat['id'] = f'category-{cat["id"]}'
        cat['text'] = cat.pop('name')
        cat['items'] = [roles[i] for i in cat.pop('roleIds')]

    return full_categories
