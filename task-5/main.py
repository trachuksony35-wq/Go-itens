odd_sum = sum(range(1, 101, 2))
print(f"Сума непарних чисел від 1 до 100: {odd_sum}")

text = input("Введіть рядок: ")

if text:
    first_letter_count = text.lower().count(text[0].lower())
    print(f"Кількість входжень першої літери ({text[0]}): {first_letter_count}")
else:
    print("Рядок порожній — першої літери немає.")
