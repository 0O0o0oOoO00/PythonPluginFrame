from PluginFrame.utils.CommandTools.resources import InputCommand
from PluginFrame.utils.CommandTools.utils import loadCommandClass


def main():
	prompt = ""
	while True:
		inputCommand = InputCommand(input(prompt + " > "))
		command = ...
		pluginCommand = ...


if __name__ == "__main__":
	main()
