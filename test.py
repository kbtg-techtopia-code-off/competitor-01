import unittest

class Testing(unittest.TestCase):
    #// create uniitets for the game rock paper scissors lizard spock
    #// and the game should be game loop and count gampe played and print game winds
    #// add Lizard and Spock to the game
    def test_play(self):
        self.assertEqual(play(), 'P')
        self.assertEqual(play(), 'C')
        self.assertEqual(play(), 'It\'s a tie')
        
    # // test lizard and spock
    def test_is_win(self):
        self.assertEqual(is_win('rock', 'lizard'), True)
        self.assertEqual(is_win('lizard', 'spock'), True)
        self.assertEqual(is_win('spock', 'scissor'), True)
        self.assertEqual(is_win('scissor', 'lizard'), True)
        self.assertEqual(is_win('lizard', 'paper'), True)
        self.assertEqual(is_win('paper', 'spock'), True)
        self.assertEqual(is_win('spock', 'rock'), True)
        self.assertEqual(is_win('rock', 'scissor'), True)
        self.assertEqual(is_win('scissor', 'paper'), True)
        self.assertEqual(is_win('paper', 'rock'), True)
        self.assertEqual(is_win('rock', 'spock'), False)
        self.assertEqual(is_win('spock', 'lizard'), False)
        self.assertEqual(is_win('lizard', 'rock'), False)
        self.assertEqual(is_win('scissor', 'rock'), False)
        self.assertEqual(is_win('paper', 'scissor'), False)
        self.assertEqual(is_win('rock', 'paper'), False)
        self.assertEqual(is_win('scissor', 'spock'), False)
        self.assertEqual(is_win('paper', 'lizard'), False)
        self.assertEqual(is_win('lizard', 'scissor'), False)
        self.assertEqual(is_win('spock', 'paper'), False)
        self.assertEqual(is_win('rock', 'rock'), False)
        self.assertEqual(is_win('scissor', 'scissor'), False)
        self.assertEqual(is_win('paper', 'paper'), False)
        self.assertEqual(is_win('lizard', 'lizard'), False)
        self.assertEqual(is_win('spock', 'spock'), False)

if __name__ == '__main__':
   unittest.main()
