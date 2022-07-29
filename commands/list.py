import os
from ..utils.CommandTools.resources import Command, InputCommand
from ..utils.PluginTools.utils import listPlugin
from ..utils.PluginTools.utils import listParameters

__all__ = ["ListPlugin", "ListPluginParameters", "Loaded"]


class ListPlugin(Command):
	
	def __init__(self):
		super(ListPlugin, self).__init__("list", False)
	
	@property
	def description(self) -> str:
		return "List all plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		print("test")
	
	def run(self, inputCommand: InputCommand) -> None:
		listPlugin()


class ListPluginParameters(Command):
	def __init__(self):
		super(ListPluginParameters, self).__init__("list", True)
	
	@property
	def description(self) -> str:
		return "List plugin's parameters."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		listParameters(self.globalVarDict["LOADED_PLUGIN_LIST"][self.globalVarDict["CURRENT_PLUGIN"]])


class Loaded(Command):
	def __init__(self):
		super(Loaded, self).__init__("loaded", False)
	
	@property
	def description(self) -> str:
		return "List loaded plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		print("Loaded plugins:")
		for plugin in self.globalVarDict["LOADED_PLUGIN_LIST"].keys():
			print("\t", plugin)

