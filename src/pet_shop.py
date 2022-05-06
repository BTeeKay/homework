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

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

def get_customer_cash(bob):
    return bob["cash"]

def remove_customer_cash(cust, cash):
    cust["cash"] -= cash

def get_customer_pet_count(cust):
    return len(cust["pets"])

def add_pet_to_customer(cust, pet):
    cust["pets"].append(pet)

def customer_can_afford_pet(cust, pet):
    
    afford = False

    if cust["cash"] >= pet["price"]:
        afford = True

    return afford


def sell_pet_to_customer(list, pet, cust):
    # check customer has enough, remove pet from store, remove cash and add pet to customer
    # add money to store
    
    if pet != None:
        check = False
        check = customer_can_afford_pet(cust, pet)
        if check == True:
            add_pet_to_customer(cust, pet)
            increase_pets_sold(list, 1)
            remove_customer_cash(cust, pet["price"])
            add_or_remove_cash(list, pet["price"])
