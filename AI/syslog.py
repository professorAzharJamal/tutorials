import socket

HOST = "127.0.0.1"
PORT = 514

message = "Simple syslog message"  # Your actual message here

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Combine message and send to syslog server
data = message.encode()
sock.sendto(data, (HOST, PORT))

sock.close()  # Optional: Close the socket

print(f"Sent syslog message: {message} to {HOST}:{PORT}")