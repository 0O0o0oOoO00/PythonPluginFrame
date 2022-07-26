from dataclasses import dataclass
from typing import Union, List, NoReturn
from abc import ABCMeta, abstractmethod
import shlex

__all__ = ["InputCommand", "CommandInfo", "Command", "CommandHelp"]


class InputCommand(object):
	def __init__(self, commandStr: str) -> None:
		commandTmpList = shlex.split(commandStr)
		while "" in commandTmpList:
			commandTmpList.remove('')
		self.command = commandTmpList[0]
		if len(commandTmpList) == 1:
			self.parametersList = []
		else:
			self.parametersList = commandTmpList[1:]


@dataclass
class CommandInfo:
	name: str
	usage: Union[str, None]
	description: Union[str, None]


class CommandHelp(object):
	def __init__(self):
		self.commandHelpList: List[CommandInfo] = list()
	
	def add(self, name: str, usage: Union[str, None] = None, description: Union[str, None] = None):
		self.commandHelpList.append(CommandInfo(name, usage, description))
		return self
	
	def print(self):
		print("Command:")
		for i in self.commandHelpList:
			print(f"\t{i.name}:\n\t\t[Usage]: {i.usage}\n\t\t[Description]: {i.description}")


class Command(metaclass=ABCMeta):
	def __init__(self, commandName: str, pluginCommand: bool = False, changeGlobalVal: bool = False):
		self.pluginCommand = pluginCommand
		self.commandName = commandName
		self.changeGlobalVal = changeGlobalVal
		self.globalVarDict = dict()
		
	@property
	@abstractmethod
	def description(self) -> str:
		pass
	
	@property
	@abstractmethod
	def newGlobalVarDict(self) -> dict:
		pass
	
	@abstractmethod
	def printHelp(self) -> NoReturn:
		pass
	
	@abstractmethod
	def run(self, inputCommand: InputCommand) -> NoReturn:
		pass



