class FSA():

	def __init__(self, state=None):
		self.state = state or 0
		self.transitions = {
			0: {'0': 0, '1': 1},
			1: {'0': 2, '1': 0},
			2: {'0': 1, '1': 2},
		}

	def transition(self, input):
		if not isinstance(input, str):
			raise Exception('invalid input')
		for ch in input:
			if ch not in ['0', '1']:
				raise Exception(f'invalid input: {ch} is not a valid character')
			self.state = self.transitions[self.state][ch]
		return self.state
	
	@property
	def is_final_state(self):
		return self.state in [0, 1, 2]
	
	def print(self):
		if self.is_final_state:
			print(f'output for state S{self.state} = {self.state}')


if __name__ == '__main__':
	choice = input("Enter input for your finite automaton: ")
	fsa = FSA()
	try:
		fsa.transition(choice)
		fsa.print()
	except Exception as  e:
		print(e)