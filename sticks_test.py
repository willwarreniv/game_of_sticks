from sticks import *
from nose.tools import raises

# test file for games of sticks


test_player = Player("test player")
test_player2 = Player("test player 2")
test_sticks = 20
test_game = Game(20, test_player, test_player2)
ai = AI(test_game)
test_game2 = Game(10, test_player, ai)
ai2 = AI(test_game2)

"""Testing Player class"""
def test_player_str():
    assert test_player.__str__() == "Player name: test player"

def test_player_eq():
    assert test_player.__eq__(test_player) == True

def test_player_not_eq():
    assert test_player.__eq__(test_player2) == False

def test_game_str():
    assert test_game.__str__() == "This game is between Player name: test player and Player name: test player 2 with 20 sticks."

def test_game_eq():
    assert test_game.__eq__(test_game) == True

def test_game_not_eq():
    assert test_game.__eq__(test_game2) == False

def test_ai_str():
    assert ai.__str__() == "AI"

def test_ai_eq():
    assert ai.__eq__(ai) == True

def test_ai__not__eq():
    assert ai.__eq__(ai2) == False



def test_get_move():
    pass


def test_user_turn():
    pass
if __name__ == "__main__":
    main()
