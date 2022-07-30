from importlib.resources import Package
import importlib, os, pathlib
from typing import Dict, Union, List
from .resources import Parameter
from tabulate import tabulate

PLUGIN_PATH = pathlib.Path(os.path.dirname(__file__)) / ".." / ".." / "plugins"


def listPlugin():
	print("Plugins:")
	for plugin in os.listdir(PLUGIN_PATH):
		if plugin in ["__pycache__"]:
			continue
		else:
			print("\t", plugin)


def getAllPlugin() -> List[str]:
	pluginList = list()
	for plugin in os.listdir(PLUGIN_PATH):
		if plugin in ["__pycache__"]:
			continue
		else:
			pluginList.append(str(plugin))
	return pluginList


def listParameters(pluginMain: object):
	content = list()
	for i, parameter in enumerate(pluginMain.parametersList):
		content.append([parameter.name, parameter.type_.__name__, parameter.must, getattr(pluginMain, parameter.name), parameter.description])
	print(tabulate(content, headers=["Name", "Type", "Must", "CurrentValue", "Description"]))


def getParametersDict(pluginMain: object) -> Dict[str, Parameter]:
	parametersDict = dict()
	for parameter in pluginMain.parametersList:
		parametersDict[parameter.name] = parameter
	return parametersDict


def setParameter(pluginMain: object, parameter: str, value: Union[int, float, bool, str], parametersDict: Union[Dict[str, object], None] = None):
	if parametersDict is None:
		parametersDict = getParametersDict(pluginMain)
	setattr(pluginMain, parameter, parametersDict[parameter].type_(value))


def loadPlugin(pluginName: str) -> Package:
	return importlib.import_module(f"PluginFrame.plugins.{pluginName}.run")


def loadPluginMain(plugin: Package) -> object:
	return plugin.Main()


def runPlugin(pluginMian: object):
	pluginMian.run()
