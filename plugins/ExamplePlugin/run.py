from typing import List, NoReturn
from PluginFrame.utils.PluginTools import Plugin, Parameter
import os
import multiprocessing
import subprocess

class Main(Plugin):
	def __init__(self):
		print("init")
		self.parameter1 = None
		self.parameter2 = None
		self.parameter3 = True
		self.parameter4 = "hauid"
	
	@property
	def parametersList(self) -> List[Parameter]:
		return [Parameter("parameter1", int, True, None, ""),
		        Parameter("parameter2", float, True, None, ""),
		        Parameter("parameter3", bool, False, True, ""),
		        Parameter("parameter4", str, False, "hauid", "")]
	
	@property
	def description(self) -> str:
		pass
	
	def run(self) -> NoReturn:
		print("djabdawijdnakdc")
		print(self.parameter1)
		print(self.parameter2)
		print(self.parameter3)
		print(self.parameter4)


if __name__ == "__main__":
	print(Main().__dict__)
	os.system("start cmd.exe /k 'start /?'")