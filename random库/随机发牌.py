import random

cards = [str(i) for i in range(2, 11)]
cards.extend(list("JQKA"))

allcards = []
for c in "♥♠♣◇":
    for s in cards:
        allcards.append(c + s)

random.shuffle(allcards)  # 洗牌
for k in range(4):
    player = allcards[k::4]
    player.sort()
    print(player)
