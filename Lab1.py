from random import randint
import numpy as np
import random

print('Memorice')
print('')

matrix = []

pair_of_cards = int(input('how many pair of cards do you want?: '))
print('')
player1 = 0
player2 = 0 
total_score = 0
turn = 1

#Crear lista que contiene los pares del total de numeros que piden los jugadores
game_list = list(range(1, pair_of_cards + 1)) + list(range(1, pair_of_cards + 1))

#Se revuelven los numeros para que la lista quede desordenada
game_list_aleatory = random.sample(game_list, len(game_list))

#Pasamos de lista a matrix
game_matrix = np.array(game_list_aleatory).reshape(2, pair_of_cards)
#print(game_matrix)

#creamos una matrix que contendra los '*'
def hidden_matrix(filas, n):
    
    matrix = []
    for i in range(filas):
        fila = []

        for j in range(n):
            fila.append('*')

        matrix.append(fila)

    return matrix
result = hidden_matrix(2, pair_of_cards)
result = np.array(result).reshape(2, pair_of_cards)
print(result)

#Reemplazamos primera coordenada
def show_matrix1(x1, y1):

    result[x1][y1] = game_matrix[x1][y1]

    return result

#reemplazamos las dos coordenadas y verificamos si son iguales o no
def show_matrix2(x1, y1, x2, y2):

    result[x1][y1] = game_matrix[x1][y1]
    result[x2][y2] = game_matrix[x2][y2]
    print('')
    print(result)

    if result[x1][y1] == result[x2][y2]:
        result == result
    
    elif result[x1][y1] != result[x2][y2]:

        result[x1][y1] = ('*')
        result[x2][y2] = ('*')
    print('')
    print('ACTUAL BOARD')
    return result

#chequeamos que las coordenadas no se salgan del tablero
#def check_coord(coordx, coordy)

#chequeamos que las coordenadas no se repitan
#def not_repeat(coordx1, coordy1, coordx2, coordy2)

#juego
while total_score != pair_of_cards:
        
        turn += 1

        if turn%2 == 0:

            print('Turn of player 1: ')
            x1_player1 = int(input('what is your x1= '))
            y1_player1 = int(input('what is your y1= '))
            print('The card is a: ',game_matrix[x1_player1][y1_player1])
            print('')
            print(show_matrix1(x1_player1,y1_player1))
            print('')

            x2_player1 = int(input('cual es tu x2= '))
            y2_player1 = int(input('cual es tu y2= '))

            print('The first card is a: ', game_matrix[x1_player1][y1_player1])
            print('The second card is a: ', game_matrix[x2_player1][y2_player1])
            
            print(show_matrix2(x1_player1,y1_player1,x2_player1,y2_player1))
            print('')

            if game_matrix[x1_player1][y1_player1] == game_matrix[x2_player1][y2_player1]:
                player1 += 1
                total_score = player1 + player2

                print('you guessed, player 1 has now', player1, 'points')
                  
            else: 
                print('you did not guess, player 1 has ',player1, ' points')
                
            

        elif turn%2 != 0:
            print('Turn of player 2: ')
            x1_player2 = int(input('what is your x1= '))
            y1_player2 = int(input('what is your y1= '))

            print('the card is a: ', game_matrix[x1_player2][y1_player2])
            print('')
            print(show_matrix1(x1_player2,y1_player2))
            print('')

            x2_player2 = int(input('What is your x2= '))
            y2_player2 = int(input('What is your y2= '))

            print('The first card is a: ', game_matrix[x1_player2][y1_player2])
            print('The second card is a: ', game_matrix[x2_player2][y2_player2])
            print('')
            print(show_matrix2(x1_player2,y1_player2,x2_player2,y2_player2))   
            print('')

            if game_matrix[x1_player2][y1_player2] == game_matrix[x2_player2][y2_player2]:
                player2  += 1
                print('You guessed, player 2 has now', player2, 'points')
               
                total_score = player1 + player2
            else: 
                print('You did not guess, player 2 has',player2,' points')
                
        
print('Player 1 ended with: ', player1, 'points')
print('Player 2 ended with: ', player2, 'points')
print('')

if player1 > player2:
    print('Player 1 has more points (',player1,')')

elif player1 == player2:
    print('The two players tied (',player1,')')

else:
    print('Player 2 has more points (',player2,')')

        
