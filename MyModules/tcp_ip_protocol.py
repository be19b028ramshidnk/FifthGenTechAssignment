import asyncio
from communication_protocol import CommunicationProtocol

class TCPIPProtocol(CommunicationProtocol): # TCPIPProtocol will implement the abstract methods defined in CommunicationProtocol
    def __init__(self, host, port): # constructor
        self.host = host # Stores the provided host address
        self.port = port # Stores the provided port number.
        self.clients = {} # Dictionary to store connected devices (device_id: (reader, writer))

    async def connect(self, device_id): # This asynchronous method attempts to establish a TCP/IP connection with a device identified by device_id
        
        try:
            reader, writer = await asyncio.open_connection(self.host, self.port)
            self.clients[device_id] = (reader, writer)

        except ConnectionRefusedError:
            print(f"Connection refused for device {device_id}")
        except Exception as e:
            print(f"Error connecting to device {device_id}: {e}")
        """
        opens an asynchronous connection to the specified host and port. 
        It awaits the connection to be established and assigns the reader and writer objects to the variables reader and writer.
        
        The established connection (reader, writer) is stored in the clients dictionary with the device_id as the key.
        
        except ConnectionRefusedError block handles cases where the connection attempt is refused by the device.
        
        except Exception as e block catches any other exceptions during connection establishment.
        """

    async def read(self, device_id): # This asynchronous method attempts to read data from a device identified by device_id
        try:
            reader, _ = self.clients[device_id]
            data = await reader.read(1024) # Reads up to 1024 bytes of data from the reader object asynchronously and stores it in the data variable.
            return data
        except KeyError:  # Device might be disconnected
            print(f"Device {device_id} not connected")
        except Exception as e:
            print(f"Error reading from device {device_id}: {e}")

    async def write(self, device_id, data):
        try:
            _, writer = self.clients[device_id] # Retrieves the writer object from the clients
            writer.write(data) # Writes the provided data to the writer object.
            await writer.drain() # Waits for the data to be completely written to the network.
        except KeyError:  # Device might be disconnected
            print(f"Device {device_id} not connected")
        except Exception as e:
            print(f"Error writing to device {device_id}: {e}")
