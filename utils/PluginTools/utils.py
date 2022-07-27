from importlib.resources import Package
import importlib
from typing import Dict, List, Union, ClassVar
from .resources import Parameter
from ..CommandTools.utils import InputCommand, printHelp


def listParameters(pluginMain: ClassVar):
	print(f"Name\t\t|\tType\t|\tMust\t|\tNowValue\t|\tDescription")
	for i, parameter in enumerate(pluginMain.parametersList()):
		print(f"{parameter.name}\t|\t{parameter.type_.__name__}\t|\t{parameter.must}\t|\t{getattr(pluginMain, parameter.name)}\t\t|\t{parameter.description}")


def getParametersDict(pluginMain: ClassVar) -> Dict[str, Parameter]:
	parametersDict = dict()
	for parameter in pluginMain.parametersList():
		parametersDict[parameter.name] = parameter
	return parametersDict


# def setParameter(plugin: Package, parameter: str, value: Union[int, float, bool, str]):
# 	while True:
# 		commandStr = input("\n>> ")
# 		if commandStr:
# 			inputCommand = InputCommand(commandStr)
# 			if inputCommand.command == "set" and hasattr(inputCommand, "parameter") and hasattr(inputCommand, "value"):
# 				parameter, value = inputCommand.parameter, inputCommand.value
# 				parametersDict = dict()
# 				for i in plugin.parametersList():
# 					parametersDict[i.name] = i
# 				setattr(plugin, parameter, parametersDict[parameter].type_(value))
# 			elif inputCommand.command == "list":
# 				listParameters(plugin)
# 			elif inputCommand.command == "help":
# 				printHelp("help", None, "Show this help message.")
# 				printHelp("set", "set [PARAMETER] [VALUE]", "Set the plugin's parameter.")
# 				printHelp("list", None, "List plugin parameters.")
# 				printHelp("quit", None, "Quit.")
# 				printHelp("exit", None, "Exit.")
# 			elif inputCommand.command == "run":
# 				plugin.run()
# 				break
# 			elif inputCommand.command == "quit" or inputCommand.command == "exit":
# 				break
def setParameter(pluginMain: ClassVar, parameter: str, value: Union[int, float, bool, str]):
	parametersDict = getParametersDict(pluginMain)
	setattr(pluginMain, parameter, parametersDict[parameter].type_(value))


def loadPlugin(pluginName: str) -> Package:
	return importlib.import_module(f"PluginFrame.plugins.{pluginName}.run")


def loadPluginMain(plugin: Package) -> ClassVar:
	return plugin.Main()


def runPlugin(pluginMian: ClassVar):
	pluginMian.run()
