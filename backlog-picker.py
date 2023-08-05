import random

sheets = ["metal", "non_metal", "essentials", "discogs"]

items = { 
    "metal" : 759,
    "non_metal" : 266,
    "essentials": 59,
    "discogs" : 95
}

index = random.randrange(0, 3)
sheet_index = items[sheets[index]]

row_number = random.randrange(0, sheet_index)

print(f"sheet: {sheets[index]}")
print(f"row number: {row_number}")