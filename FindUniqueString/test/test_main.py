import unittest

class FindUniqueStrings(unittest.TestCase):

    def basic_test_cases(self):
        self.assertEquals(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
        self.assertEquals(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
        self.assertEquals(find_uniq([ 'silvia', 'vasili', 'victor' ]), 'victor')
        self.assertEquals(find_uniq([ 'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter' ]), 'Harry Potter')

    def basic_test_cases(self):
        self.assertEquals(find_uniq([ '', '', '', 'a', '', '' ]), 'a')
        self.assertEquals(find_uniq([ '    ', '  ', ' ', 'a', ' ', '' ]), 'a')
        self.assertEquals(find_uniq([ 'foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab' ]), '   ')


if __name__ == '__main__':
    unittest.main()
