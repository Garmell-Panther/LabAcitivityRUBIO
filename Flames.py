def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common characters
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    total_count = len(name1) + len(name2)

    if total_count == 0:
        return "Not compatible! Single forever </3"

    flames = list("FLAMES")
    index = 0

    while len(flames) > 1:
        index = (index + total_count - 1) % len(flames)
        flames.pop(index)

    result = {
        "F": "Friendship",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sibling"
    }

    return result[flames[0]]


# --- Main Program with Input ---
print("💘 Welcome to the FLAMES Game 💘")
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

result = flames_game(name1, name2)
print("\nResult:", result)
