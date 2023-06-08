import  random
def flip_coin():
    return random.choices(['heads','tails'])
print(flip_coin())

for i in range(10):
    print("Flip" +str(i+1)+":",flip_coin())

