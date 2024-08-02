#  serves as a mock implementation of a TCP/IP protocol for testing purposes

import asyncio
class MockTCPSocket: # This class will be used to simulate the behavior of a TCP socket for testing.
    def __init__(self, data: bytes) -> None: # data represents the data that the socket will pretend to receive or send
        self.data = data
        self.received_data: bytes = None # to store data received during the mock write operation

    async def read(self, n: int) -> bytes: #  simulates reading data from the socket.
        return self.data[:n] # returns a slice of the self.data with a maximum length of n bytes, represents the data "read" from the mock socket.

    async def write(self, data: bytes) -> None: # simulates writing data to the socket.
        self.received_data = data  # variable to keep track of what was "written" during the test.




class TCPIPStub: #simulates a TCP/IP connection using the MockTCPSocket class.
    def __init__(self, data: bytes) -> None:
        self.reader = MockTCPSocket(data) # Creates a MockTCPSocket instance to simulate the reader side of the connection, initialized with some data 
        self.writer = self.reader # This simplifies usage in tests where you might not need separate reader and writer behavior

    async def read(self, device_id: str) -> bytes: #  takes a device ID (string) as input
        return await self.reader.read(1024)

    async def write(self, device_id: str, data: bytes) -> None:
        await self.writer.write(data) # Delegates the writing task to the writer object's write method with the provided data, simulating writing to the simulated connection.
