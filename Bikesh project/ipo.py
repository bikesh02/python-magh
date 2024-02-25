import random

ipo_ids = {
    "ID_1": 12343,
    "ID_2": 23566,
    "ID_3": 38790,
    "ID_4": 43424,
    "ID_5": 53560,
    "ID_6": 67840,
    "ID_7": 74688,
    "ID_8": 85767,
    "ID_9": 96354,
    "ID_10": 10537
}
selected_ids = random.sample(list(ipo_ids), 2)

print("Selected ipo ids:")
print(f"Congratulations ! {selected_ids}")
 
for selected_id in selected_ids:
    print(f"{selected_id}: {ipo_ids[selected_id]}")