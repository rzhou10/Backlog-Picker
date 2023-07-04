import random

sheets = ["metal", "non_metal", "discogs"]

items = { 
    "metal" : 936,
    "non_metal" : 183,
    "discogs" : 104
}


index = random.randrange(0, 2)
sheet_index = items[sheets[index]]

print(f"sheet: {sheets[index]}")

row_number = random.randrange(0, sheet_index)

print(f"row number: {row_number}")