from typing import List
from PluginFrame.utils.PluginTools import Plugin, Parameter


class Main(Plugin):
	def __init__(self):
		self.parameter1 = None
		self.parameter2 = None
		self.parameter3 = None
		self.parameter4 = None
	
	def parametersList(self) -> List[Parameter]:
		return [Parameter("parameter1", int, True, ""), Parameter("parameter2", float, True, ""), Parameter("parameter3", bool, False, ""), Parameter("parameter4", str, False, "")]
	
	def description(self) -> str:
		pass
	
	def run(self) -> None:
		print("djabdawijdnakdc")
		print(self.parameter1)
		print(self.parameter2)
		print(self.parameter3)
		print(self.parameter4)


if __name__ == "__main__":
	print(Main().__dict__)
