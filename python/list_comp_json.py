# Quest: Listans Mästare
# Läser en JSON-struktur och skriver ut alla värden med list comprehension
import json

data = {"scores": [95, 87, 72, 100], "names": ["Alice", "Bob", "Charlie"]}

all_values = [val for lst in data.values() for val in (lst if isinstance(lst, list) else [lst])]
print(all_values)
