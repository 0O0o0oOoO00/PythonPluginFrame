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
	# print("{0:10}\t|\t{1:5}\t|\t{2:5}\t|\t{3:15}\t|\t{4:}".format("Name", "Type", "Must", "CurrentValue", "Description"))
	content = list()
	for i, parameter in enumerate(pluginMain.parametersList()):
		# print(f"\t{parameter.name}\n\t\t[Type]: {parameter.type_.__name__}\n\t\t[Must]: {parameter.must}\n\t\t[CurrentValue]: {getattr(pluginMain, parameter.name)}\n\t\t[Description]: {parameter.description}")
		# print("{0:10}\t|\t{1:5}\t|\t{2:5}\t|\t{3:15}\t|\t{4:}".format(str(parameter.name), str(parameter.type_.__name__), str(parameter.must), str(getattr(pluginMain, parameter.name), str(parameter.description))))
		content.append([parameter.name, parameter.type_.__name__, parameter.must, getattr(pluginMain, parameter.name), parameter.description])
	print(tabulate(content, headers=["Name", "Type", "Must", "CurrentValue", "Description"]))


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
