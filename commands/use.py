from ..utils.CommandTools.resources import Command, InputCommand

__all__ = ["UsePlugin"]


class UsePlugin(Command):
	def __init__(self):
		super(UsePlugin, self).__init__("use", False, True)
	
	@property
	def description(self) -> str:
		return "Use plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		return self.globalVarDict
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		if inputCommand.parametersList[0] in self.globalVarDict["LOADED_PLUGIN_LIST"].keys():
			self.globalVarDict["CURRENT_PLUGIN"] = inputCommand.parametersList[0]
			self.globalVarDict["PROMPT"] = inputCommand.parametersList[0] + self.globalVarDict["PROMPT"]
