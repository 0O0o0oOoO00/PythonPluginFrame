from typing import NoReturn

from ..utils.CommandTools.resources import Command, InputCommand

__all__ = ["RunPlugin"]


class RunPlugin(Command):
	def __init__(self):
		super(RunPlugin, self).__init__("run", True, False)
	
	@property
	def description(self) -> str:
		return "Run plugin."
	
	@property
	def newGlobalVarDict(self) -> dict:
		pass
	
	def printHelp(self) -> NoReturn:
		pass
	
	def run(self, inputCommand: InputCommand) -> NoReturn:
		self.globalVarDict["LOADED_PLUGIN_LIST"][self.globalVarDict["CURRENT_PLUGIN"]].run()
