from pprint import pprint


products = [
    "Гречка",
    "Макарони",
    "Спагеті",
    "Картопля",
    "Буряк",
    "Морква",
    "Капуста",
    "Цибуля",
    "Часник",
    "Борошно",
    "Яйця",
    "Соняшникова олія",
    "Вершкове масло",
    "Сіль",
    "Перець",
    "Цукор",
    "Оцет",
    "Сода",
    "Чай",
    "Кава"
]

products_sold = []

commands = [
    "1. Показати список наявних товарів",
    "2. Додати новий товар до списку",
    "3. Додати список товарів",
    "4. Видалити товар за ім'ям",
    "5. Видалити товар за номер",
    "6. Показати відсортований список товарів за ім'ям",
    "7. Продати товар",
    "8. Знайти номер товару за ім'ям",
    "9. Показати список проданих товарів",
    "10. Показати історію продажів",
    "11. Вийти з програми"
]

while True:
    pprint(commands)
    comm = input(f"Виберіть дію (цифру) або введіть 'exit' для завершення:\n-> ")
    if comm.lower() == "exit":
        print("Дякуємо що були з нами")
        break

    if int(comm) <= 0 or int(comm) > len(commands):
        print("Ви ввели не вірну дію, спробуйте ще раз")
        input("Натисніть enter для продовження")
        continue

    if int(comm) == 1:
        pprint(products)
        input("Натисніть enter для продовження")

    elif int(comm) == 2:
        new_prod = input("Введи назву товару\n-> ")
        if new_prod not in products:
            products.append(new_prod)
            input(f"Товар '{new_prod}' успішно додано.\nНатисність enter для продовження ")
        else:
            input(f"Товар '{new_prod}' вже є у списку.\nНатисність enter для продовження ")

    elif int(comm) == 3:
        new_prods = input("Введіть список товарів через пробіл\n-> ")
        new_prod = new_prods.split()
        # products += new_prods
        for prod in new_prods:
            if prod not in products:
                products.append(prod)

    elif int(comm) == 7:
        prod = input("Введіть назву товару\n-> ")
        if prod in products:
            products.remove(prod)
            products_sold.append(prod)
            print(f"Товар '{prod}' продано.")
        else:
            print(f"Товару '{prod}' немає.")

    elif int(comm) == 10:
        pprint(products_sold[::-1])
