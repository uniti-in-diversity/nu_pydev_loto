import loto
import game
import unittest

class TestPlayer(unittest.TestCase):

    def testPlayer(self):
        self.player = loto.Player('Testplayer', True, False)
        self.assertEquals(self.player.winer, False)
        self.assertIsInstance(self.player, loto.Player)


class TestCard(unittest.TestCase):

    def setUp(self):
        self.testcard = loto.Card('card_for_test')

    def test_init_card(self):
        self.assertEqual(self.testcard.username, 'card_for_test')

    def test_card(self):
        trigger = []
        for num in self.testcard.array:
            for i in num:
                if i == 'n':
                    trigger.append(i)
        self.assertEquals(len(trigger), 12)

    def test_is_num_in_card(self):
        self.assertIs(loto.Card.bochonoknum_is_in_card(self.testcard, '0'), None)

    def test_cover_bochonok(self):
        nums = []
        newnums = []
        for n in self.testcard.array:
            for a in n:
                if a != 'n':
                    nums.append(a)
        checkednum = nums[0]
        newcard = self.testcard.cover_bochonoknum(checkednum)
        for num in newcard:
            for i in num:
                if i != 'n':
                    newnums.append(i)
        self.assertNotEqual(nums, newnums)

    def test_win(self):
        self.assertIs(self.testcard.check_win(), False)

class TetsBochonki(unittest.TestCase):

    def setUp(self):
        self.testbag = loto.Bag()

    def test_bochonki(self):
        self.assertEqual(self.testbag.__class__.__name__, 'Bag')

    def test_take_num(self):
        assert 0 < self.testbag.take_bochonok() < 90

class TestGame(unittest.TestCase):

    def setUp(self):
        self.testgame = game.Game()
        self.int_players = []
        self.winers = []
        self.player1 = loto.Player('comp1', False, False)
        self.player2 = loto.Player('comp2', False, False)
        self.int_players.append(self.player1)
        self.int_players.append(self.player2)
        self.lottobag = loto.Bag()

    def get_input(text):
        return input(text)

    def test_game_init(self):
        self.assertIsInstance(self.testgame, game.Game)

    def test_gaming(self):
        self.testgame.run(self.int_players)
        self.assertIsNotNone(self.testgame.winers)
        self.assertIs(self.testgame.usererror, False)

class TestGameHumans(unittest.TestCase):

    def setUp(self):
        self.testgame = game.Game()
        self.int_players = []
        self.winers = []
        self.player1 = loto.Player('comp1', True, False)
        self.player2 = loto.Player('comp2', True, False)
        self.int_players.append(self.player1)
        self.int_players.append(self.player2)
        self.lottobag = loto.Bag()

    def get_input(text):
        return input(text)

    def test_gamin_human(self):
        self.testgame.run(self.int_players)
        self.assertIs(self.testgame.usererror, True)





