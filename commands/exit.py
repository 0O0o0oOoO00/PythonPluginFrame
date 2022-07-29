from ..utils.CommandTools.resources import Command, InputCommand
import sys

__all__ = ["Exit", "Quit", "ExitPlugin", "QuitPlugin"]


class Exit(Command):
	def __init__(self):
		super(Exit, self).__init__("exit", False)
	
	@property
	def description(self) -> str:
		return "Exit manager."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		sys.exit()


class Quit(Command):
	def __init__(self):
		super(Quit, self).__init__("quit", False)
	
	@property
	def description(self) -> str:
		return "Quit manager."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		sys.exit()


class ExitPlugin(Command):
	def __init__(self):
		super(ExitPlugin, self).__init__("exit", True, True)
	
	@property
	def description(self) -> str:
		return "Exit plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		return self.globalVarDict
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		self.globalVarDict["CURRENT_PLUGIN"] = None
		self.globalVarDict["PROMPT"] = self.globalVarDict["DEFAULT_PROMPT"]


class QuitPlugin(Command):
	def __init__(self):
		super(QuitPlugin, self).__init__("quit", True, True)
	
	@property
	def description(self) -> str:
		return "Quit plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		return self.globalVarDict
	
	def printHelp(self) -> None:
		pass
	
	def run(self, inputCommand: InputCommand) -> None:
		self.globalVarDict["CURRENT_PLUGIN"] = None
		self.globalVarDict["PROMPT"] = self.globalVarDict["DEFAULT_PROMPT"]
