#!/usr/bin/python3

import json
from collections import defaultdict

def find_duplicate_urls(node, path=None, duplicates=None):
    """
    Recursively scans the JSON structure and gathers duplicate URLs.

    Args:
        node: Current JSON object (dict, list, or other).
        path: Current path in the tree (for context).
        duplicates: Dict mapping URL -> list of paths where it appears.

    Returns:
        Dictionary of URLs that appear more than once, with their locations.
    """
    if path is None:
        path = []
    if duplicates is None:
        duplicates = defaultdict(list)

    if isinstance(node, dict):
        if node.get("type") == "url" and "url" in node:
            url = node["url"]
            location = " / ".join(path + [node.get("name", "[unnamed]")])
            duplicates[url].append(location)

        # Search children if present
        if "children" in node and isinstance(node["children"], list):
            for child in node["children"]:
                find_duplicate_urls(child, path + [node.get("name", "")], duplicates)

    elif isinstance(node, list):
        for item in node:
            find_duplicate_urls(item, path, duplicates)

    return duplicates


# --- Example usage ---
# Load JSON from file
with open("html/arf.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Scan for duplicates
duplicates = find_duplicate_urls(data)

# Print duplicates
has_duplicates = False
for url, locations in duplicates.items():
    if len(locations) > 1:  # Only show duplicates
        has_duplicates = True
        print(f"\n⚠️ Duplicate URL found: {url}")
        for loc in locations:
            print(f"   - Found at: {loc}")

if not has_duplicates:
    print("✅ No duplicate URLs found!")
