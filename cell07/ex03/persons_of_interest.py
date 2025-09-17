def famous_births(wc):
    # นับจำนวน key
    pop = 0
    # นับจำนวน year
    count = 0
    # เก็บค่า
    key = []
    year = []
    # เข้าไปใน dict ทีละตัว
    for i in wc:
        # เก็บค่า key ทีละตัว
        key.append(i)
        # เก็บค่า year ทีละตัว
        year.append(wc.get(i)["date_of_birth"])
    # sort year
    sort_year = sorted(year)
    # ลูปจนกว่า dict จะหมด
    while wc:
        # เอาค่าปีใน dict มาเทียบกับปีที่ sort แล้ว
        if wc.get(key[pop])["date_of_birth"] == sort_year[count]:
            print(f"{wc.get(key[pop])['name']} is a great scientist born in {wc.get(key[pop])['date_of_birth']}.")
            # เอาค่า key ออกจาก dict
            wc.pop(key[pop])
            # เอาค่า key ออก
            key.pop(pop)
            # นับ key ใหม่
            pop = 0
            # ปีที่ sort แล้วเพิ่มอีก 1
            count += 1
        else:
            # นับ key เพิ่มอีก 1
            pop += 1

women_scientists = { "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" }, "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" }, "lise": { "name": "Lise Meitner", "date_of_birth": "1878" }, "grace": { "name": "Grace Hopper", "date_of_birth": "1906" } }
famous_births(women_scientists)
