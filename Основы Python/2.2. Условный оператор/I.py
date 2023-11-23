player1 = input()
player2 = input()
player3 = input()

if player1 < player2 and player1 < player3:
    print(player1)
elif player2 < player1 and player2 < player3:
    print(player2)
else:
    print(player3)