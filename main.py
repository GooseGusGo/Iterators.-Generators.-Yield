nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, flat_list):
		self.index = -1
		self.list = [x for l in flat_list for x in l]

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == len(self.list) - 1:
			raise StopIteration
		self.index += 1
		return self.list[self.index]



if __name__ == '__main__':
	for item in FlatIterator(nested_list):
	    print(item)
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)
