def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]


def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
    return False

        
def add_friend(person, new_friend):
    person["friends"].append(new_friend)
        
def remove_friend(person, ex_friend):
    person["friends"].remove(ex_friend)
    
def total_money(people):
    wallet = []
    for person in people:
        wallet.append(person["monies"])
        total_wallet = sum(wallet)
    return total_wallet

def l_money(lender, lendee, amount):
    lender["monies"]  = lender["monies"] - amount
    lendee["monies"] = lendee["monies"] + amount
    print(lender["monies"])
    print(lendee["monies"])


def all_favourite_foods(people):
    favourite_snacks=[]
    for person in people:
        favourite_snacks.extend(person["favourites"]["snacks"])
    return favourite_snacks

def find_no_friendends(people):
    no_friends =[]
    for person in people:
        if person["friends"] == []:
            no_friends.append(person)
    return no_friends