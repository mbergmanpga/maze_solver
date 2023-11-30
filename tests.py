import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 15
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Assert that total number of rows and columns is equal
        self.assertEqual(
            num_cols * num_rows,
            len(m1._cells) * len(m1._cells[0])
        )
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells_largest(self):
        num_cols = 20
        num_rows = 25
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Assert that total number of rows and columns is equal
        self.assertEqual(
            num_cols * num_rows,
            len(m1._cells) * len(m1._cells[0])
        )
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        

if __name__ == "__main__":
    unittest.main()

