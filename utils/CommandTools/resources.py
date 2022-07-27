from dataclasses import dataclass
from typing import Union, List
from abc import ABCMeta, abstractmethod

__all__ = ["InputCommand", "CommandInfo", "Command", "CommandHelp"]


class InputCommand(object):
	def __init__(self, commandStr: str) -> None:
		commandTmpList = commandStr.split(" ")
		while "" in commandTmpList:
			commandTmpList.remove('')
		self.command = commandTmpList[0]
		if len(commandTmpList) == 1:
			self.parametersList = commandTmpList[1:]
		else:
			self.parametersList = []


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
	def __init__(self, commandName: str, pluginCommand: bool = False):
		self.pluginCommand = pluginCommand
		self.commandName = commandName
	
	@abstractmethod
	def usage(self) -> str:
		pass
	
	@abstractmethod
	def description(self) -> str:
		pass
	
	@abstractmethod
	def printHelp(self) -> None:
		pass
	
	@abstractmethod
	def run(self, *args, **kwargs) -> None:
		pass
