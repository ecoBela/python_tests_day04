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
        



