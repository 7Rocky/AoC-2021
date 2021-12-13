import io
import sys
import unittest

from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        rescued_stdout = io.StringIO()
        sys.stdout = rescued_stdout

        main()

        want = 'Number of points after first fold (1): 735\n' + \
               'Hidden message (2):\n' + \
               '#..#.####.###..####.#..#..##..#..#.####\n' + \
               '#..#.#....#..#....#.#.#..#..#.#..#....#\n' + \
               '#..#.###..#..#...#..##...#..#.#..#...#.\n' + \
               '#..#.#....###...#...#.#..####.#..#..#..\n' + \
               '#..#.#....#.#..#....#.#..#..#.#..#.#...\n' + \
               '.##..#....#..#.####.#..#.#..#..##..####\n'

        sys.stdout = sys.__stdout__
        self.assertEqual(want, rescued_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
