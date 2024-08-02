# Assessment Problem
In a manufacturing plant, multiple devices need to be connected in order to “read” and “write” real time data. However, the devices support different protocols for “reading” and “writing”. Develop a program that will:

a) support TCP/IP communication (IP Address and Port Number) for both reading and writing values.
b) communicate with multiple devices simultaneously.
c) support future additions of communication protocols.
d) provide a stub to test TCP/IP communication.
e) have program/code driven unit test cases.



## What is TCP/IP Communication?
* TCP/IP is a suite of protocols used for communication over networks
* IP (Internet Protocol): Handles the addressing and routing of packets between networks.
* TCP (Transmission Control Protocol): Provides reliable, ordered, and error-checked delivery of data between applications on different hosts
* It involves establishing a connection between two devices, sending data in packets, and ensuring the data arrives correctly at the destination. 

## Reading and Writing Values using TCP/IP

### Reading
* Involves receiving data from a remote device
* Establishing a TCP connection with the device.
* Sending a request to the device to send data.
* Receiving the data in packets, reassembling them, and interpreting the data as values

### Writing
* Involves sending data to a remote device. This is done by:
* Establishing a TCP connection with the device.
* Formatting the data into packets.
* Sending the packets to the device.
* Ensuring the data is received correctly by the device

# Solution Approach
* Use Python for its versatility, extensive libraries, and clear syntax.
* Employ the socket library for TCP/IP communication.
* Create an base class interface for protocol abstraction.
* Implement specific protocol classes inheriting from the base interface.
* Utilize asynchronous programming for concurrent handling of multiple devices.
* Implement unit tests for core functionalities.

## Diffrent Classes Used 

### CommunicationProtocol Class (Abstract Class)
* Abstract base class for protocol implementations.
* This abstract class provides a contract for any communication protocol used in our system. 
* Specific protocols like TCP/IP will inherit from this class and implement the abstract methods with their specific communication logic. * This allows us to treat different protocols in a uniform manner through the DeviceManager class.

### DeviceManager Class
* It acts as a facade for different communication protocols.
* It allows you to manage and utilize different protocols by name without directly interacting with their specific implementations.
* This simplifies device communication as we can use the same interface (read/write methods) for various devices regardless of their communication protocol.

### TCPIPProtocol Class
* Concrete implementation for TCP/IP communication.
* Creates TCP connections to specified devices using their IP addresses and port numbers
* Keeps track of established connections using a dictionary to store reader and writer objects for each connected device.
* Reads data from a connected device through its associated reader object.
* Sends data to a connected device through its associated writer object.

### TCPIPStub Class
* The TCPIPStub class allows to test the functionalities of the TCPIPProtocol class without actually establishing a network connection. 
* We can provide the expected data in the constructor and verify if the TCPIPProtocol interacts with the mock socket as intended during read and write operations. 
* This helps ensure the logic of your TCP/IP protocol implementation works correctly.

### TestTCPIPProtocol Class
* It is a unit test class designed to verify the functionality of the TCPIPProtocol class.
* It employs the Python unittest framework to create and execute test cases
* Uses unittest.mock to simulate network interactions without actually establishing real connections.
* Covers essential aspects of the TCPIPProtocol class, such as connecting to devices, reading data, writing data, and handling potential errors.
* Asserts that the TCPIPProtocol class behaves as expected under various conditions, including successful connections, failed connections, reading and writing data, and handling disconnections.


# How to Run the Code

* You can run the code by using terminal command " python test_tcp_ip_protocol.py"
* You will get the result like " Ran 8 tests in 0.102s OK " which tells that all our test cases passed everything working perfectly fine