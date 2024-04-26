import json


members = [
    {"name": "Никита", "added_date": ""},
    {"name": "Ильмир", "added_date": "25.03.2024"},
    {"name": "Антон", "added_date": "14.04.2024"},
    {"name": "Ренат", "added_date": "28.03.2024"},
    {"name": "Алексей", "added_date": ""},
    {"name": "Артём", "added_date": ""},
    {"name": "Р Ш", "added_date": ""},
    {"name": "Leo", "added_date": "28.03.2024"},
    {"name": "Aleksey", "added_date": ""},
    {"name": "user", "added_date": "28.03.2024"},
    {"name": "🐝", "added_date": ""}
]

with open ("members.json", "w") as file:
    json.dump(members, file)

