import json
from collections import defaultdict

# Load JSON file
with open("publications.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Function to count occurrences in the ID field
def count_dblp_types(entries):
    counts = defaultdict(int)
    
    for entry in entries:
        if "ID" in entry:
            id_value = entry["ID"]
            if id_value.startswith("DBLP:conf/"):
                counts["DBLP:conf"] += 1
            elif id_value.startswith("DBLP:journals/"):
                counts["DBLP:journals"] += 1
            else:
                counts["Other"] += 1  # Count IDs that are neither "conf" nor "journals"

    return counts

# If the JSON file contains a list of entries
if isinstance(data, list):
    counts = count_dblp_types(data)
else:
    counts = count_dblp_types([data])  # If it's a single entry, wrap it in a list

# Print results
print("Counts:", dict(counts))
