import json

# Loading the turtles data
the_file = open("turtles.json")
turtle_data = json.load(the_file)

# Empty "template" dict
summary = {
    "male": {
        "total": 0,
        "alive": 0
    },
    "female": {
        "total": 0,
        "alive": 0
    }
}

# Iterating over the data and updatind `summary` accordingly
for turtle in turtle_data:
    if turtle["gender"] == "male":
        summary["male"]["total"] += 1
        if turtle["condition"]["status"] == "alive":
            summary["male"]["alive"] += 1
    else:
        summary["female"]["total"] += 1
        if turtle["condition"]["status"] == "alive":
            summary["female"]["alive"] += 1

# Create the new file with the summary data
with open("turtles_summary.json", "w") as f:
    json.dump(summary, f)
