from typing import NoReturn

from ..utils.CommandTools.resources import Command, InputCommand
__all__ = ["SetParameters"]

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
		while i < len(inputCommand.parametersList):
			setattr(self.globalVarDict["LOADED_PLUGIN_LIST"][self.globalVarDict["CURRENT_PLUGIN"]], inputCommand.parametersList[i], inputCommand.parametersList[i + 1])
			i += 2
