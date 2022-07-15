numbers = list(map(int, input().split(', ')))
positives, negatives, evens, odds = [], [], [], []
for x in numbers:
    positives.append(str(x)) if x >= 0 else negatives.append(str(x))
    evens.append(str(x)) if x % 2 == 0 else odds.append(str(x))
print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
