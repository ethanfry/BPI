import unittest
from fsa import FSA


class FSATestCase(unittest.TestCase):

	def setUp(self):
		self.fsa = FSA()

	def test_integer_input_raises_exception(self):
		with self.assertRaises(Exception):
			self.fsa.transition(0)
	
	def test_not_zero_or_1_inpute_raises_exception(self):
		with self.assertRaises(Exception):
			self.fsa.transition('222')

	def test_0_0_0(self):
		self.fsa.transition('0')
		self.assertEqual(0, self.fsa.state)

	def test_0_1_1(self):
		self.fsa.transition('1')
		self.assertEqual(1, self.fsa.state)

	def test_1_0_2(self):
		self.fsa.state = 1
		self.fsa.transition('0')
		self.assertEqual(2, self.fsa.state)

	def test_1_1_0(self):
		self.fsa.state = 1
		self.fsa.transition('1')
		self.assertEqual(0, self.fsa.state)

	def test_2_0_1(self):
		self.fsa.state = 2
		self.fsa.transition('0')
		self.assertEqual(1, self.fsa.state)

	def test_2_1_2(self):
		self.fsa.state = 2
		self.fsa.transition('1')
		self.assertEqual(2, self.fsa.state)

if __name__ == '__main__':
    unittest.main()
