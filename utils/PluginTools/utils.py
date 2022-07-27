from importlib.resources import Package
import importlib
from typing import Dict, Union
from .resources import Parameter


def listParameters(pluginMain: object):
	print(f"Name\t\t|\tType\t|\tMust\t|\tNowValue\t|\tDescription")
	for i, parameter in enumerate(pluginMain.parametersList()):
		print(f"{parameter.name}\t|\t{parameter.type_.__name__}\t|\t{parameter.must}\t|\t{getattr(pluginMain, parameter.name)}\t\t|\t{parameter.description}")


def getParametersDict(pluginMain: object) -> Dict[str, Parameter]:
	parametersDict = dict()
	for parameter in pluginMain.parametersList():
		parametersDict[parameter.name] = parameter
	return parametersDict


def setParameter(pluginMain: object, parameter: str, value: Union[int, float, bool, str]):
	parametersDict = getParametersDict(pluginMain)
	setattr(pluginMain, parameter, parametersDict[parameter].type_(value))


def loadPlugin(pluginName: str) -> Package:
	return importlib.import_module(f"PluginFrame.plugins.{pluginName}.run")


def loadPluginMain(plugin: Package) -> object:
	return plugin.Main()


def runPlugin(pluginMian: object):
	pluginMian.run()
