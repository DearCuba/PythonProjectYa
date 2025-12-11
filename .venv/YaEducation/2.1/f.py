"""
Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.

Формат ввода
название товара;
цена товара;
вес товара;
количество денег у пользователя.

Формат вывода
Чек
<название товара> - <вес>кг - <цена>руб/кг
Итого: <итоговая стоимость>руб
Внесено: <количество денег от пользователя>руб
Сдача: <сдача>руб
"""
product_name = input()
product_price = int(input())
product_weight = int(input())
user_money = int(input())

print(f"Чек\n{product_name} - {product_weight}кг - {product_price}руб/кг\nИтого: {product_price * product_weight}руб\n"
      f"Внесено: {user_money}руб\nСдача: {user_money - product_price * product_weight}руб")