#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.

def dictionary(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(dictionary(dog='Jack', cat={'Leopold': 2, 'Murka': 3}, horse=['bill', 'jack', 'anatoliy'],
                     hamster={'edward', 'homa'}))