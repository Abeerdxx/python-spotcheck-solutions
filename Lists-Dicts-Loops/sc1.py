bagpack = {
    "owner": "Dora",
    "base_weight": 1,
    "items": [
        {"name": "rope", "weight": 1},
        {"name": "hatchet", "weight": 2},
        {"name": "mirror", "weight": 1},
        {"name": "water", "weight": 5},
    ]
}

# nothing but a normal dict-access
bagpack["items"][2]["weight"] += 1
