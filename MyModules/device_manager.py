

class DeviceManager:
    def __init__(self):
        self.protocols = {} # to store registered communication protocols.

    def add_protocol(self, protocol_name, protocol_instance): # This method adds a communication protocol to the device manager.
        self.protocols[protocol_name] = protocol_instance
        """
        protocol_name: A string representing the name of the protocol.
        protocol_instance: An instance of a class that inherits from CommunicationProtocol (e.g., TCPIPProtocol).
        It adds the protocol name and instance to the self.protocols dictionary.
        """
    async def read(self, device_id, protocol_name):
        """
        This asynchronous method reads data from a device using a specific protocol.
        device_id: A string representing the identifier of the device to read from.
        
        It tries to find the protocol instance using the protocol_name from the self.protocols dictionary
        If found, it calls the read method of the protocol instance with the device_id and returns the received data.
        
        If the protocol is not found, it raises a KeyError which is caught and a message is printed.
        It also returns None to indicate the failure
        """
        try:
            protocol = self.protocols[protocol_name]
            return await protocol.read(device_id)
        except KeyError:
            print(f"Protocol {protocol_name} not found")
            return None  # Indicate protocol not available
        

    async def write(self, device_id, protocol_name, data):
        try:
            protocol = self.protocols[protocol_name]
            await protocol.write(device_id, data)
        except KeyError:
            print(f"Protocol {protocol_name} not found")
            
        """
        This asynchronous method writes data to a device using a specific protocol.
        It has the same arguments and functionality as the read method, 
        but it calls the write method of the protocol instance to write the provided data to the device.
        """
