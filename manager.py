import os
import sys
import colorama
from colorama import Fore, Style
from pathlib import Path
from utils.CommandTools.resources import InputCommand
from utils.CommandTools.utils import getAllCommandDict, getAllPluginCommandDict


def init():
	global DEFAULT_PROMPT, PROMPT, COMMAND, PLUGIN_COMMAND, CURRENT_PLUGIN, LOADED_PLUGIN_LIST
	DEFAULT_PROMPT = " > "
	PROMPT = DEFAULT_PROMPT
	COMMAND = getAllCommandDict()
	PLUGIN_COMMAND = getAllPluginCommandDict()
	CURRENT_PLUGIN = None
	LOADED_PLUGIN_LIST = dict()


def main():
	while True:
		inputCommand = InputCommand(input(PROMPT))
		print()
		if CURRENT_PLUGIN is None:
			if inputCommand.command in COMMAND.keys():
				setattr(COMMAND[inputCommand.command], "globalVarDict", globals())
				COMMAND[inputCommand.command].run(inputCommand)
				if getattr(COMMAND[inputCommand.command], "changeGlobalVal"):
					globals().update(COMMAND[inputCommand.command].newGlobalVarDict)
			else:
				print(Fore.RED + "Invalid command" + Style.RESET_ALL)
		else:
			if inputCommand.command in PLUGIN_COMMAND.keys():
				setattr(PLUGIN_COMMAND[inputCommand.command], "globalVarDict", globals())
				PLUGIN_COMMAND[inputCommand.command].run(inputCommand)
				if getattr(PLUGIN_COMMAND[inputCommand.command], "changeGlobalVal"):
					globals().update(PLUGIN_COMMAND[inputCommand.command].newGlobalVarDict)
			else:
				print(Fore.RED + "Invalid command" + Style.RESET_ALL)


if __name__ == "__main__":
	sys.path.append(str(Path(os.path.dirname(__file__)) / ".."))
	colorama.init()
	init()
	main()
