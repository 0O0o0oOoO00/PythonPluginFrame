from ..utils.CommandTools.resources import Command, InputCommand
from ..utils.PluginTools.utils import loadPlugin, loadPluginMain, getAllPlugin

__all__ = ["Load", "Reload"]


class Load(Command):
	def __init__(self):
		super(Load, self).__init__("load", False, True)
	
	@property
	def description(self) -> str:
		return "Load plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		return self.globalVarDict
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		allPlugin = getAllPlugin()
		if len(inputCommand.parametersList) != 0:
			for i in inputCommand.parametersList:
				if i in allPlugin:
					self.globalVarDict["LOADED_PLUGIN_LIST"][i] = loadPluginMain(loadPlugin(i))
				else:
					...
		else:
			...


class Reload(Command):
	def __init__(self):
		super(Reload, self).__init__("reload", False)
	
	@property
	def description(self) -> str:
		return "Reload plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		pass
