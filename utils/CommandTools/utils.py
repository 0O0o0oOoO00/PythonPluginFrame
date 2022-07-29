from typing import List, Union, Dict
from .resources import CommandHelp, CommandInfo, InputCommand
from importlib.resources import Package
import importlib
import pathlib
import os


COMMAND_FILE_PATH = pathlib.Path(os.path.dirname(__file__)) / ".." / ".." / "commands"


def printHelp(name: Union[str, None] = None, usage: Union[str, None] = None, description: Union[str, None] = None, commandList: Union[List[CommandInfo], None] = None):
	commandHelp = CommandHelp()
	if commandList is None and name is not None:
		commandHelp.add(name, usage, description)
	else:
		for command in commandList:
			commandHelp.add(command.name, command.usage, command.description)
	commandHelp.print()


def listCommandFile() -> List[str]:
	commandFile = list()
	for file in os.listdir(COMMAND_FILE_PATH):
		if file in ["__pycache__"]:
			continue
		else:
			commandFile.append(str(file.replace(".py", "")))
	return commandFile


def loadCommandFile(commandFileName: str) -> Package:
	return importlib.import_module(f"PluginFrame.commands.{commandFileName}")


def loadCommandClass(commandFile: Package, className: str) -> object:
	commandClass = getattr(commandFile, className)
	return commandClass()


def getCommand(commandFile: Package) -> List[str]:
	command = list()
	if hasattr(commandFile, "__all__"):
		for i in commandFile.__all__:
			commandClass = loadCommandClass(commandFile, i)
			if getattr(commandClass, "pluginCommand") is False:
				command.append(i)
	return command


def getCommandDict(commandFile: Package) -> Dict[str, object]:
	command = getCommand(commandFile)
	commandDict = dict()
	for i in command:
		commandClass = loadCommandClass(commandFile, i)
		commandDict[commandClass.commandName] = commandClass
	return commandDict


def getAllCommandDict() -> Dict[str, object]:
	allFile = listCommandFile()
	allCommandDict = dict()
	for file in allFile:
		allCommandDict.update(getCommandDict(loadCommandFile(file)))
	return allCommandDict


def runCommand(command: str, commandList: InputCommand, allCommandDict: Union[Dict[str, object], None] = None):
	if allCommandDict is None:
		allCommandDict = getAllCommandDict()
	allCommandDict[command].run(commandList)


def getPluginCommand(commandFile: Package) -> List[str]:
	pluginCommand = list()
	if hasattr(commandFile, "__all__"):
		for i in commandFile.__all__:
			pluginCommandClass = loadCommandClass(commandFile, i)
			if getattr(pluginCommandClass, "pluginCommand"):
				pluginCommand.append(i)
	return pluginCommand


def getPluginCommandDict(commandFile: Package) -> Dict[str, object]:
	pluginCommand = getPluginCommand(commandFile)
	pluginCommandDict = dict()
	for i in pluginCommand:
		pluginCommandClass = loadCommandClass(commandFile, i)
		pluginCommandDict[pluginCommandClass.commandName] = pluginCommandClass
	return pluginCommandDict


def getAllPluginCommandDict() -> Dict[str, object]:
	allFile = listCommandFile()
	allPluginCommandDict = dict()
	for file in allFile:
		allPluginCommandDict.update(getPluginCommandDict(loadCommandFile(file)))
	return allPluginCommandDict


def runPluginCommand(command: str, commandList: InputCommand, allPluginCommandDict: Union[Dict[str, object], None] = None):
	if allPluginCommandDict is None:
		allPluginCommandDict = getAllPluginCommandDict()
	allPluginCommandDict[command].run(commandList)


if __name__ == "__main__":
	print(listCommandFile())
	print(loadCommandFile("list"))
	print(getCommandDict(loadCommandFile("list")))
	print(getPluginCommandDict(loadCommandFile("list")))
	print()
	print(getAllCommandDict())
	print(getAllPluginCommandDict())
	print()
	# runCommand("list")
	# runPluginCommand("list")
