import abc
from typing import Any
# ABC stands for Abstract Base Class. It is a module in Python’s abc (abstract base class) module.
# Defines an abstract class named CommunicationProtocol that inherits from ABC. 
# This class serves as a template for concrete communication protocols.

class CommunicationProtocol(abc.ABC):

    @abc.abstractmethod #This decorator marks methods as abstract, meaning they must be implemented by subclasses
    async def read(self, device_id: str) -> Any:
        """
        This method reads data from a device asynchronously.

        Args:
            device_id (str): The identifier of the device to read from.

        Returns:
            Any: The data read from the device. The specific type depends on the protocol implementation.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def write(self, device_id: str, data: Any) -> None:
        """
        This method writes data to a device asynchronously.

        Args:
            device_id (str): The identifier of the device to write to.
            data (Any): The data to be written to the device. The specific type depends on the protocol implementation.
        """
        raise NotImplementedError
