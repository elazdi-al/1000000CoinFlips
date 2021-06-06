import random
flips = ["head", "tail"]
result = random.choice(flips)
times = 0
head = 0
tail = 0
while times < 1000000:
    result = random.choice(flips)
    if result == "head":
        head += 1
    elif result == "tail":
        tail += 1
    times +=1

percentage_heads = (head / times) * 100
percentage_tail = (tail / times) * 100

print(f"The computer flipped {times} times and got {tail} tails and {head} heads, {percentage_tail} % of tail and {percentage_heads} % of heads ")
    

