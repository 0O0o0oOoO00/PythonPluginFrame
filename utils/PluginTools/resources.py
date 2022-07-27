from abc import ABCMeta, abstractmethod
from typing import List, Union, Type
from dataclasses import dataclass


@dataclass
class Parameter(object):
	name: str
	type_: Union[Type[int], Type[float], Type[bool], Type[str]]
	must: bool
	description: Union[None, str] = None


class Plugin(metaclass=ABCMeta):
	
	@abstractmethod
	def parametersList(self) -> List[Parameter]:
		pass
	
	@abstractmethod
	def description(self) -> str:
		pass
	
	@abstractmethod
	def run(self) -> None:
		pass
