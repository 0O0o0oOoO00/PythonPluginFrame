import os,sys
from pathlib import Path

from utils.CommandTools.resources import InputCommand
from utils.CommandTools.utils import getAllCommandDict, getAllPluginCommandDict


def main():
	global PROMPT, PLUGIN, COMMAND, PLUGIN_COMMAND
	PROMPT = " > "
	PLUGIN = None
	COMMAND = getAllCommandDict()
	PLUGIN_COMMAND = getAllPluginCommandDict()
	while True:
		inputCommand = InputCommand(input(PROMPT))
		if PLUGIN is None:
			if inputCommand.command in COMMAND.keys():
				for i in COMMAND[inputCommand.command].mainFunctionParametersList:
					COMMAND[inputCommand.command].mainFunctionParametersDict.update({i: globals()[i]})
				COMMAND[inputCommand.command].run(inputCommand)
			else:
				print("Invalid command")
		else:
			if inputCommand.command in PLUGIN_COMMAND.keys():
				PLUGIN_COMMAND[inputCommand.command].run(InputCommand)
			else:
				print("Invalid command")


if __name__ == "__main__":
	sys.path.append(str(Path(os.path.dirname(__file__)) / ".."))
	# print(Path(os.path.dirname(__file__)) / "..")
	main()
