def get_person(name: str, age: int):
    name = name.title()
    return f'name is {name} and age is {age}'


print(get_person("jon", 13))

