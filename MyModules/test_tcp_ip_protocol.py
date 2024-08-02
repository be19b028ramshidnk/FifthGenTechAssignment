import unittest # unittest framework for writing and running tests.
import asyncio
from unittest.mock import patch # to mock functions during testing.
from tcp_ip_protocol import TCPIPProtocol
from tcp_ip_stub import TCPIPStub # for mocking network connections.


class TestTCPIPProtocol(unittest.TestCase): # This class will contain all the unit tests for the TCPIPProtocol class.
    @patch('asyncio.open_connection') # This decorator mocks the asyncio.open_connection function to simulate network connections without actually making network calls.
    async def test_connect_success(self, mock_open_connection): # return a successful connection.
        mock_open_connection.return_value = asyncio.Future()
        mock_open_connection.return_value.set_result(('reader', 'writer'))

        protocol = TCPIPProtocol("localhost", 1234)
        await protocol.connect("test_device") # Calls the connect method with a device ID.

        self.assertEqual(len(protocol.clients), 1) # Verifies that the clients dictionary of the protocol contains the connected device.
        self.assertIn("test_device", protocol.clients)

    @patch('asyncio.open_connection')
    async def test_connect_failure(self, mock_open_connection):
        mock_open_connection.side_effect = ConnectionRefusedError

        protocol = TCPIPProtocol("localhost", 1234)
        await protocol.connect("test_device")

        self.assertEqual(len(protocol.clients), 0) # Verifies that the clients dictionary remains empty due to the failed connection.

    async def test_read(self):
        stub = TCPIPStub(b"test data")
        protocol = TCPIPProtocol("localhost", 1234)
        protocol.clients = {"test_device": (stub.reader, None)}
        result = await protocol.read("test_device")
        self.assertEqual(result, b"test data") # Verifies that the received data matches the data sent by the TCPIPStub.

    async def test_write(self):
        stub = TCPIPStub(b"")
        protocol = TCPIPProtocol("localhost", 1234)
        protocol.clients = {"test_device": (None, stub.writer)}
        await protocol.write("test_device", b"test data")
        self.assertEqual(stub.writer.received_data, b"test data") # Verifies that the TCPIPStub received the written data.

    async def test_read_disconnected(self): 
        #  Simulates a disconnected device by creating a connection and then removing it from the clients dictionary
        stub = TCPIPStub(b"test data")
        protocol = TCPIPProtocol("localhost", 1234)
        protocol.clients = {"test_device": (stub.reader, None)}
        del protocol.clients["test_device"]  # Simulate disconnection
        result = await protocol.read("test_device")
        self.assertEqual(result, None)  # Verifies that the read method returns None to indicate a failed read operation.

    async def test_write_disconnected(self):
        # Simulate disconnected device
        stub = TCPIPStub(b"")
        protocol = TCPIPProtocol("localhost", 1234)
        protocol.clients = {"test_device": (None, stub.writer)}
        del protocol.clients["test_device"]  # Simulate disconnection
        await protocol.write("test_device", b"test data")
        self.assertFalse(hasattr(stub.writer, 'received_data'))  # Verifies that the TCPIPStub writer doesn't have the received_data attribute anymore

    async def test_read_error(self):
        # Simulate error during read
        stub = TCPIPStub(b"test data")
        protocol = TCPIPProtocol("localhost", 1234)
        protocol.clients = {"test_device": (stub.reader, None)}
        stub.reader.read.side_effect = OSError 

        with self.assertRaises(OSError):
            await protocol.read("test_device") #to verify that an OSError is raised during read.

    async def test_write_error(self):
        # Simulate error during write
        stub = TCPIPStub(b"")
        protocol = TCPIPProtocol("localhost", 1234)
        protocol.clients = {"test_device": (None, stub.writer)}
        stub.writer.write.side_effect = OSError

        with self.assertRaises(OSError):
            await protocol.write("test_device", b"test data")


if __name__ == "__main__": # ensures the tests are only executed when the file is run directly 
    unittest.main()
