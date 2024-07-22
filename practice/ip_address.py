# Import the 'socket' module to work with networking functionalities.
import socket
# Define the 'addr' variable with an IP address string. This IP address is '127.0.0.2561',
# which is intentionally an invalid IP address.

addr = '192.168.0.9'

# Start a try-except block to catch potential errors.

try:
    # Use the 'socket.inet_aton()' function to attempt to convert the IP address string into a packed binary format.
    socket.inet_aton(addr)

    # If the 'inet_aton()' function succeeds without raising an error, it is a valid IP address.

    # Print a message indicating that the IP address is valid.
    print("Valid IP")

except socket.error:
    # If the 'inet_aton()' function raises a 'socket.error', it is not a valid IP address.

    # Print a message indicating that the IP address is invalid.
    print("Invalid IP")
