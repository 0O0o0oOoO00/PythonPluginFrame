import sys
import os
import pathlib
import importlib.util
import importlib
import click
from dataclasses import dataclass
from typing import Union, List
from importlib.resources import Package

PLUGIN_PATH = pathlib.Path(os.path.dirname(__file__)) / ".." / "plugins"


@dataclass
class Command(object):
	command: str
	usage: Union[str, None]
	description: Union[str, None]


class CommandHelp(object):
	def __init__(self):
		self.commandHelpList: List[Command] = list()
	
	def add(self, command: str, usage: Union[str, None] = None, description: Union[str, None] = None):
		self.commandHelpList.append(Command(command, usage, description))
		return self
	
	def print(self):
		print("Command:")
		for i in self.commandHelpList:
			print(f"\t{i.command}:\n\t\t[Usage]: {i.usage}\n\t\t[Description]: {i.description}")


def printLine():
	print("-" * os.get_terminal_size().columns)


def printHelp():
	CommandHelp().add("help", None, "Show this help message.") \
		.add("set", "set [PARAMETER] [VALUE]") \
		.add("list", None, "List plugin parameters.") \
		.add("quit", None, "Quit.") \
		.add("exit", None, "Exit.") \
		.print()


def listParameters(package: Package):
	print(f"Name\t\t|\tType\t|\tMust\t|\tNowValue\t|\tDescription")
	for i, parameter in enumerate(package.parametersList()):
		print(f"{parameter.name}\t|\t{parameter.type_.__name__}\t|\t{parameter.must}\t|\t{getattr(package, parameter.name)}\t\t|\t{parameter.description}")


class InputCommand(object):
	def __init__(self, commandStr: str) -> None:
		commandTmpList = commandStr.split(" ")
		while "" in commandTmpList:
			commandTmpList.remove('')
		self.command = commandTmpList[0]
		if len(commandTmpList) != 1:
			self.parameter = commandTmpList[1]
			self.value = commandTmpList[2]


def listPlugin():
	print("Plugins:")
	for i in os.listdir(PLUGIN_PATH):
		if i in ["__pycache__"]:
			continue
		else:
			print("\t", i)


def runPlugin(pluginName: str):
	plugin = importlib.import_module(f"BilibiliTool.plugins.{pluginName}.run").Main()
	while True:
		commandStr = input("\n>> ")
		if commandStr:
			inputCommand = InputCommand(commandStr)
			if inputCommand.command == "set" and hasattr(inputCommand, "parameter") and hasattr(inputCommand, "value"):
				parameter, value = inputCommand.parameter, inputCommand.value
				parametersDict = dict()
				for i in plugin.parametersList():
					parametersDict[i.name] = i
				setattr(plugin, parameter, parametersDict[parameter].type_(value))
			elif inputCommand.command == "list":
				listParameters(plugin)
			elif inputCommand.command == "help":
				printHelp()
			elif inputCommand.command == "run":
				plugin.run()
				break
			elif inputCommand.command == "quit" or inputCommand.command == "exit":
				break
			# else:
			# 	print(NameError("Invalid instruction"))


@click.command()
@click.option("-l", "--list_plugin", is_flag=True, default=False)
@click.option("-m", "--use_plugin", type=str)
def BilibiliTool_CommandLine(list_plugin: bool, use_plugin: str):
	if list_plugin:
		listPlugin()
	elif use_plugin:
		runPlugin(use_plugin)


if __name__ == "__main__":
	# print(str(pathlib.Path(os.path.dirname(__file__)) / ".."))
	sys.path.append(str(pathlib.Path(os.path.dirname(__file__)) / ".." / ".."))
	if len(sys.argv) == 1:
		BilibiliTool_CommandLine(["--help"])
	BilibiliTool_CommandLine()
