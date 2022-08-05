from abc import ABCMeta, abstractmethod
from typing import List, Union, Type, NoReturn
from dataclasses import dataclass


@dataclass
class Parameter(object):
	name: str
	type_: Union[Type[int], Type[float], Type[bool], Type[str]]
	must: bool
	default: Union[int, float, bool, str, None]
	description: Union[None, str] = None


class Plugin(metaclass=ABCMeta):
	
	@property
	@abstractmethod
	def parametersList(self) -> List[Parameter]:
		pass
	
	@property
	@abstractmethod
	def description(self) -> str:
		pass
	
	@abstractmethod
	def run(self) -> NoReturn:
		pass
