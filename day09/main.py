
class Marble:
    def __init__(self):
        self.next = None
        self.prev = None
        self.worth = 0

    def __repr__(self):
        return str(self.worth)

class Player:
    def __init__(self):
        self.score = 0

def play_game(num_players, last_marble_worth):

    # Initialize players
    players = [0]*num_players    

    curr_player = 0
    curr_marble_score = 0
    curr_marble = None
    first_time = True
    first_marble = None

    while(True):
        marble_to_insert = Marble()
        marble_to_insert.worth = curr_marble_score

        if first_time:
            marble_to_insert.next = marble_to_insert
            marble_to_insert.prev = marble_to_insert
            curr_marble = marble_to_insert
            first_marble = marble_to_insert
            curr_marble_score += 1
            first_time = False
            continue
        elif (marble_to_insert.worth % 23) == 0:
            players[curr_player] += marble_to_insert.worth

            marble_to_remove = curr_marble
            for i in range(7):
                marble_to_remove = marble_to_remove.prev

            players[curr_player] += marble_to_remove.worth

            # Remove marble
            marble_to_remove_left = marble_to_remove.prev
            marble_to_remove_right = marble_to_remove.next
            marble_to_remove_left.next = marble_to_remove_right
            marble_to_remove_right.prev = marble_to_remove_left

            curr_marble = marble_to_remove_right

        else:
            # Find marble one and two spaces clockwise (which will be left and right of new marble)
            marble_left = curr_marble.next
            marble_right = marble_left.next
            marble_left.next = marble_to_insert
            marble_right.prev = marble_to_insert
            marble_to_insert.prev = marble_left
            marble_to_insert.next = marble_right

            curr_marble = marble_to_insert

        if curr_marble_score == last_marble_worth:
            break

        curr_player = (curr_player + 1)%num_players
        curr_marble_score += 1
    
    # Find highest score
    return max(players)




if __name__ == '__main__':

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.split(' ')
    
    num_players = int(data[0])
    last_marble_worth = int(data[6])

    max_score = play_game(num_players, last_marble_worth)
    print(f'play_game: highest score = {max_score}')

    # This takes about 20s to run
    max_score = play_game(num_players, last_marble_worth*100)
    print(f'part2: highest score = {max_score}')