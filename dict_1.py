"""
Создайте словарь:
{"city": "Москва", "temperature": "20"}
Выведите на экран значение ключа city
Уменьшите значение "temperature" на 5
Выведите на экран весь словарь
"""
sky = {"city": "Москва", "temperature": "20"}
print(sky["city"])
sky["temperature"] = str(int(sky["temperature"])-5)
print(sky)