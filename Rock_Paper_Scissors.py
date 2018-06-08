num = 2
while num > 1:
    player_input = input('Player one: ')
    player2_input = input('Player two: ')

    while player_input == 'rock' and player2_input == 'paper':
        print('Player 2 wins')
        break
    while player_input == 'paper' and player2_input == 'rock':
        print('Player 1 wins')
        break
    while player_input == 'rock' and player2_input == 'scissor':
        print('Player 1 wins')
        break
    while player_input == 'scissor' and player2_input == 'rock':
        print('Player 2 wins')
        break
    while player_input == 'scissor' and player2_input == 'paper':
        print('Player 1 wins')
        break
    while player_input == 'paper' and player2_input == 'scissor':
        print('Player 2 wins')
        break
