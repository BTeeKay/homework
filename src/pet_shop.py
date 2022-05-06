# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):

    answer = name["name"]
    return answer

def get_total_cash(name):

    answer = name["admin"]["total_cash"]
    return answer

def add_or_remove_cash(name, cash):

    name["admin"]["total_cash"] += cash

def get_pets_sold(name):
    answer = name["admin"]["pets_sold"]
    return answer

def increase_pets_sold(name, num):

    name["admin"]["pets_sold"] += num

def get_stock_count(name):
    
    total = 0
    for cat in name["pets"]:
        total += 1
    
    return total

def get_pets_by_breed(name, cat):
    
    found = []
    i = name["pets"]
    for j in i:
        if j["breed"] == cat:
            found.append(j)
    return found

def find_pet_by_name(name, pet):

    found = None
    pets = name["pets"]
    for i in pets:
        if i["name"] == pet:
            found = i       
    return found

def remove_pet_by_name(list, name):
    petts = find_pet_by_name(list, name)
    list["pets"].remove(petts)


