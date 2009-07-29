import hashlib

class HashDict(dict):
	def hash(self):
		values = self.values()
		values.sort()
		aux = ""
		for value in values:
			aux += value
		return hashlib.md5(aux).hexdigest()

