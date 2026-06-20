# def check_char(word: str , c: str):
#     for character in range(len(word)):
#         if c in word:
#             return True, f"{c} is in {word}"
#         else:
#             f"{c} is not in {word}"
#             break

# word = input("Enter word: ")
# c = input("Enter a character: ")
# print(f"{check_char(word, c)}")

factors = {
    "gina": 3,
    "dave": 6,
    "donna": 19
}

def analyse_factor(fact):
    total = 0
    count = 0
    max_payment = 3
    max_person = ' '
    for person, payment in fact.items():
        if payment > max_payment:
            max_person = person
            max_payment = payment
        total += payment
        count += 1
    avg = total / count

    return avg, total, max_person

avg, total, max_person = analyse_factor(factors)

print(f"the average payment is {avg}")
print(f"total payment is {total}")
print(f"maximum payment belongs to {max_person}")