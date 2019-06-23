def check_get_player_winner(game, number_player_1, number_player_2):
    # In this part, I tried to do just one conditional to get the winner
    # TODO: Implement PEP8 in this part
    if (((game.board[6] == game.player_1.id or game.board[6] == game.player_2.id) and (game.board[7] == game.player_1.id or game.board[7] == game.player_2.id) and (game.board[8] == game.player_1.id or game.board[8] == game.player_2.id)) or  # across the top
            ((game.board[3] == game.player_1.id or game.board[3] == game.player_2.id)and (game.board[4] == game.player_1.id or game.board[4] == game.player_2.id) and (game.board[5] == game.player_1.id or game.board[5] == game.player_2.id)) or  # across the middle
            ((game.board[0] == game.player_1.id or game.board[0] == game.player_2.id)and (game.board[1] == game.player_1.id or game.board[1] == game.player_2.id) and (game.board[2] == game.player_1.id or game.board[2] == game.player_2.id)) or  # across the bottom
            ((game.board[6] == game.player_1.id or game.board[6] == game.player_2.id)and (game.board[3] == game.player_1.id or game.board[3] == game.player_2.id) and (game.board[0] == game.player_1.id or game.board[0] == game.player_2.id)) or  # down the left side
            ((game.board[7] == game.player_1.id or game.board[7] == game.player_2.id)and (game.board[4] == game.player_1.id or game.board[4] == game.player_2.id) and (game.board[1] == game.player_1.id or game.board[1] == game.player_2.id)) or  # down the middle
            ((game.board[8] == game.player_1.id or game.board[8] == game.player_2.id)and (game.board[5] == game.player_1.id or game.board[5] == game.player_2.id) and (game.board[2] == game.player_1.id or game.board[2] == game.player_2.id)) or  # down the right side
            ((game.board[6] == game.player_1.id or game.board[6] == game.player_2.id)and (game.board[4] == game.player_1.id or game.board[4] == game.player_2.id) and (game.board[2] == game.player_1.id or game.board[2] == game.player_2.id)) or  # diagonal number 1
            ((game.board[8] == game.player_1.id or game.board[8] == game.player_2.id)and (game.board[4] == game.player_2.id or game.board[4] == game.player_2.id) and (game.board[0] == game.player_1.id or game.board[0] == game.player_2.id))):  # diagonal number 2
        if number_player_1 > number_player_2:
            game.winner = game.player_1
        elif number_player_1 < number_player_2:
            game.winner = game.player_2
        game.status = 'done'
        game.save()
        return True
    else:
        return False


def see_status_game(game):
    finish = False
    number_player_1 = 0
    number_player_2 = 0
    for position in game.board:
        if position == game.player_1.id:
            number_player_1 = number_player_1 + 1
        elif position == game.player_2.id:
            number_player_2 = number_player_2 + 1
        if number_player_1 > 2 or number_player_2 > 2:
            # The minimum number to win is 3
            # TODO: Recommend to make with Celery (tasks asynchronous)
            if check_get_player_winner(game, number_player_1, number_player_2):
                finish = True
                return finish
        if position != -1 and (number_player_1 + number_player_2) > 8 :
            # TODO: Recommend to make with Celery (tasks asynchronous)
            check_get_player_winner(game, number_player_1, number_player_2)
            finish = True
            return finish
    return finish

