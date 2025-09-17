def find_the_redheads(family):
    result = []
    for i in family:
        if family.get(i) == "red":
            result.append(i)
    return result

dupont_family = { "florian": "red", "marie": "blond", "virginie": "brunette", "david": "red", "franck": "red" }
print(find_the_redheads(dupont_family))
