from typing import NoReturn
from ..utils.CommandTools.resources import Command, InputCommand
from ..utils.PluginTools.utils import getParametersDict, setParameter, unsetParameter

__all__ = ["SetParameters", "UnsetParameters"]


class SetParameters(Command):
	def __init__(self):
		super(SetParameters, self).__init__("set", True, True)
	
	@property
	def description(self) -> str:
		return "Set plugin's parameter."
	
	@property
	def newGlobalVarDict(self) -> dict:
		return self.globalVarDict
	
	def printHelp(self) -> NoReturn:
		pass
	
	def run(self, inputCommand: InputCommand) -> NoReturn:
		i = 0
		pluginMain = self.globalVarDict["LOADED_PLUGIN_LIST"][self.globalVarDict["CURRENT_PLUGIN"]]
		parametersDict = getParametersDict(pluginMain)
		while i < len(inputCommand.parametersList):
			if parametersDict[inputCommand.parametersList[i]].type_ == bool:
				setattr(pluginMain, inputCommand.parametersList[i], True)
				i += 1
			else:
				setParameter(pluginMain, inputCommand.parametersList[i], inputCommand.parametersList[i+1])
				i += 2


class UnsetParameters(Command):
	def __init__(self):
		super(UnsetParameters, self).__init__("unset", True, True)
	
	@property
	def description(self) -> str:
		return "Unset plugin's parameter."
	
	@property
	def newGlobalVarDict(self) -> dict:
		return self.globalVarDict
	
	def printHelp(self) -> NoReturn:
		pass
	
	def run(self, inputCommand: InputCommand) -> NoReturn:
		pluginMain = self.globalVarDict["LOADED_PLUGIN_LIST"][self.globalVarDict["CURRENT_PLUGIN"]]
		if len(inputCommand.parametersList) == 0:
			for i in pluginMain.parametersList:
				unsetParameter(pluginMain, i.name)
		else:
			for i in inputCommand.parametersList:
				unsetParameter(pluginMain, i)
				