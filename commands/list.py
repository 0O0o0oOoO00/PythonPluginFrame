import os
import pathlib

from PluginFrame.utils.CommandTools.resources import Command

PLUGIN_PATH = pathlib.Path(os.path.dirname(__file__)) / ".." / "plugins"
__all__ = ["ListPlugin", "ListPluginParameters"]


def listPlugin():
	print("Plugins:")
	for plugin in os.listdir(PLUGIN_PATH):
		if plugin in ["__pycache__", "ExamplePlugin"]:
			continue
		else:
			print("\t", plugin)


class ListPlugin(Command):
	
	def __init__(self):
		Command.__init__(self, "list", False)
	
	def usage(self) -> str:
		pass
	
	def description(self) -> str:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, *args, **kwargs) -> None:
		print("baidcuaiwd")
		


class ListPluginParameters(Command):
	def __init__(self):
		Command.__init__(self, "list", True)
	
	def usage(self) -> str:
		pass
	
	def description(self) -> str:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, *args, **kwargs) -> None:
		print("neaoi")
		


if __name__ == "__main__":
	print(PLUGIN_PATH)
	listPlugin()
	print(ListPluginParameters.__name__)
	print(os.path.basename(__file__))
	print(ListPlugin().pluginCommand)
	print(dir(ListPlugin()))
