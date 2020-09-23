import re 
import json

class TextStats: 
	def __init__(
		self,
		input_path = None,
		save_data_path = None,	
		load_data_path = './',
	): 
		self.path = input_path
		self.save_data_path = save_data_path
		self.dic = {}

#	def pre_processing(self): 

	def stat(self):
		file = open(self.path)
		for line in file: 
			words = line.split()
			for word in words: 
				if (word in self.dic): 
					self.dic[word] += 1 
				else: 
					self.dic[word] = 1 
		file.close()
		return self.dic

#	def top(self): 
	def save_dict_to_json(self, file_name = 'data.json'): 
		# Notice here, stat(self) must be called before save_dict_toJson 
		json.dump(self.dic, open(file_name, 'w')) 
		print('File saved as', file_name)




a = TextStats('./text.txt')
print(a.stat())
a.save_dict_to_json()











