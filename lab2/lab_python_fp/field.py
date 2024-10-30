#field.py

def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            res = item.get(args[0])
            if res != None:
                yield res
        else:
            result = {arg: item.get(arg) for arg in args if item.get(arg) != None}
            if result:
                yield result

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))