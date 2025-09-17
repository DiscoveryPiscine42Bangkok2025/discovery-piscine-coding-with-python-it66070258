def array_of_names(persons):
    result = []
    for i in persons:
        fullname = f"{i.capitalize()} {persons.get(i).capitalize()}"
        result.append(fullname)
    return result

persons = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}
print(array_of_names(persons))
