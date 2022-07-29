from ..utils.CommandTools.resources import Command, InputCommand
import os

__all__ = ["Help", "PluginHelp"]


def printLine(prompt: str = "-", number: int = None):
	if number is None:
		number = os.get_terminal_size().columns
	print(prompt * number)


class Help(Command):
	def __init__(self):
		super(Help, self).__init__("help", False)
	
	@property
	def description(self) -> str:
		return "Show command help."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		print("help")
	
	def run(self, inputCommand: InputCommand) -> None:
		if len(inputCommand.parametersList) == 0:
			print("\tCommand:")
			for i in self.globalVarDict["COMMAND"].values():
				print("\t\t{0:10}\t{1:}".format(i.commandName, i.description))
		else:
			if len(inputCommand.parametersList) == 1:
				self.globalVarDict["COMMAND"][inputCommand.parametersList[0]].printHelp()
			else:
				for i in inputCommand.parametersList:
					printLine()
					self.globalVarDict["COMMAND"][i].printHelp()


class PluginHelp(Command):
	def __init__(self):
		super(PluginHelp, self).__init__("help", True)
	
	@property
	def description(self) -> str:
		return "Show plugin command help."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		if len(inputCommand.parametersList) == 0:
			print("\tCommand:")
			for i in self.globalVarDict["PLUGIN_COMMAND"].values():
				print("\t\t{0:10}\t{1:}".format(i.commandName, i.description))
		else:
			if len(inputCommand.parametersList) == 1:
				self.globalVarDict["PLUGIN_COMMAND"][inputCommand.parametersList[0]].printHelp()
			else:
				for i in inputCommand.parametersList:
					printLine()
					self.globalVarDict["PLUGIN_COMMAND"][i].printHelp()
