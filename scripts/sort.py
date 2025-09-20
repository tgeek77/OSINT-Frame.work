#!/usr/bin/python3

import json

def sort_children(node):
    """Recursively sort folders and their children by 'name'."""
    if isinstance(node, dict):
        # If it has children, sort them
        if "children" in node and isinstance(node["children"], list):
            node["children"] = sorted(
                (sort_children(child) for child in node["children"]),
                key=lambda x: x.get("name", "").lower(),
            )
        return node
    elif isinstance(node, list):
        return [sort_children(item) for item in node]
    else:
        return node


# --- Example usage ---
# Load JSON from a file
with open("..html/arf.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Sort the structure
sorted_data = sort_children(data)

# Save alphabetized JSON
with open("html/arf-temp.json", "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, indent=2, ensure_ascii=False)

print("✅ JSON has been alphabetized and saved to html/arf-temp.json")
