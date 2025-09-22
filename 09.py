import random
from faker import Faker

fake = Faker("en_US")
#users = ["lily", "lidia", "luthan", "Laura", "monika", "Niky", "Ofia", "Hera", "Nithaniel", "Perseous", "Annabeth", "Nix"]
users = [fake.name() for i in range (20)]
#address = ["kitchen", "dining room", "bathroom", "bedroom", "living room", "library", "Olympis temple", "the great hall", "the abis"]
address = [fake.street_address() for i in range(20)]
do_some_thing = ["eating ", "sleeping", "playing games", "learning", "reading", "drinking", "eating snacks", "reading magazines","watching TV series"]

while True:
    choice = input("1 continue, q quit, please choose:")
    if choice =="1":
        text = "{} is {} in the {}"
        user = random.choice(users)
        addr = random.choice(address)
        thing = random.choice(do_some_thing)
        temp = text.format(user, thing, addr)
        print(temp)
    elif choice=="q":
        print("the program ends")
    else:
        print("the command could not be recognized, please choose again")