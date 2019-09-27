from random import randint

game_running = True

# *** Definitions ***
def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

def calculate_player_heal():
    return randint(player['heal_min'], player['heal_max'])

while game_running == True:
    new_round = True
    player = {'name': 'Murfa', 'attack': 13, 'heal_min': 15, 'heal_max': 30, 'health': 100}

    monster = {'name': 'Bolgore', 'attack_min': 10, 'attack_max': 20, 'health': 100}
    print(calculate_monster_attack())
    print('---' * 7)
    print('Enter Player Name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health.')

    while new_round == True:


        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_choice = input()

# *** Choice 1 - attack ***
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            player['health'] = player['health'] - calculate_monster_attack()

            if monster['health'] <= 0:
                player_won = True

            else:
                #player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

# *** Choice 2 - heal ***
        elif player_choice == '2':
            player['health'] = player['health'] + calculate_player_heal() - calculate_monster_attack()
            print(player['name'] + ' has been healed for ' + str(calculate_player_heal()) + ' points of health before ' + monster['name'] + ' attacked for ' + str(calculate_monster_attack()) + ' health.')
            if player['health'] <= 0:
                monster_won = True

# *** Choice 3 - exit ***
        elif player_choice == '3':
            print('Exit Game')
            new_round = False
            game_running = False

        else:
            print('invalid input')

# *** Win Scenario ***
        if player_won == False and monster_won == False:
            print('---' * 7)
            print(player['name'] + ' has ' + str(player['health']) + ' left.')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left.')

        elif player_won:
            print(player['name'] + ' won!')
            new_round = False

        elif monster_won:
            print('The Monster won...')
            new_round = False

