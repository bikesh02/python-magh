import random
def coin_toss():
    return random.choice(["Head", "Tail"])

result= coin_toss()

print(f"The coin are {result}")
