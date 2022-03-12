items_count = 0
items_sum = 0
line_error = 0

with open('shopping_list.txt', encoding='utf-8') as file:
    for item_data in file:
        line_error += 1

        if item_data.count(':') < 2:
            print(f'{line_error} строка некорректна')
            continue

        item, quantity, price = item_data.strip().split(':')
        items_count += 1
        items_sum += int(price) * int(quantity)
    print(f'В списке {items_count} позиций, на сумму {items_sum} руб.')
