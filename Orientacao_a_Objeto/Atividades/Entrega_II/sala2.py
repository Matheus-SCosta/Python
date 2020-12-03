class Sala2:
	def __init__(self, status: str = None):
		self.__status = status

	def get_status(self):
		return self.__status

	def set_status(self, status: str):
		self.__status = status	

	status = property(get_status, set_status)	
