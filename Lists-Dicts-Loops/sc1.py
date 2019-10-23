backpack = {
    "owner": "Dora",
    "base_weight": 1,
    "items": [
        {"name": "rope", "weight": 1},
        {"name": "hatchet", "weight": 2},
        {"name": "mirror", "weight": 1},
        {"name": "water", "weight": 5},
    ]
}

items = backpack["items"]
total_weight = 0
for item in items:
	weight = item["weight"]
	total_weight += weight

print(total_weight)
