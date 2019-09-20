import unittest
import get_column_stats
import random
import os


class TestGetColumnStats(unittest.TestCase)


def test_mean(self):
    self.assertEqual(get_column_stats.mean(V=[1, 2, 3]), 2)

    @classmethod
    def setUpClass(cls):
        cls.class_test_file_name = 'class_setup_test_file.txt'
        f = open(cls.class_test_file_name, 'w')

        cls.class_direct_sum_col_0 = 0
        cls.class_direct_sum_col_1 = 0
        cls.class_direct_sum_col_2 = 0
        cls.class_direct_rows = 0

        for i in range(100):
            rand_int = random.randint(1, 100)
            cls.class_direct_sum_col_0 += rand_int
            f.write(str(rand_int) + '\t')
            cls.class_direct_rows += 1
        f.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.class_test_file_name)

    def test_file_mean_clas_setup(self):
        file__col_mean = get_column_stats.mean(
                         --file_name=self.class_test_file_name,
                         --column_number=0)
        self.assertEqual(file_col_mean,
                         self.class_direct_sum_col0/self.class_direct_rows)


if __name__ == '__main__':
    unittest.main()
