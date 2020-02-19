import unittest

from GithubRepoReader import main

class TestGithubReader(unittest.TestCase):
    def test1(self):
        self.assertEqual(main('StormNemesisgod'), [['firekings', 1], ['truedraco', 2]], 'Repo: firekings Number of commits: 1, Repo: truedraco Number of commits: 2')
    def test2(self):
        self.assertEqual(main(5), 'ERROR: username must be a string')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

#I pledge my honor that I have abided by the Stevens Honor System - Michael Ameer
