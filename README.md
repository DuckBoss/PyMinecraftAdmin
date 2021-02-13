<h2 align="center"> PyMineCraftAdmin </h2>
<p align="center">A simple utility to remotely control a MineCraft Server using the RCON protocol</p>
<br>
<br>

### Requirements
- Python 3.7+
- <code>pip install mcrcon</code>

### Usage
1) Run the folder module in python with the server IP/Port and rcon password as launch parameters:
```
> python PyMineCraftAdmin/ -ip <my_server_ip> -rcon_port <my_rcon_port> -rcon_pass <my_rcon_password>
> 
```
<b>Note: The rcon port/password can be configured in your server's `server.properties` file.</b>

### Examples
- Echo messages to the server chat:<br>
  ![image](https://user-images.githubusercontent.com/20238115/107843702-40d52100-6d9b-11eb-8518-0cb3d1be8f6d.png)
- Send commands to the server with a response:<br>
  ![image](https://user-images.githubusercontent.com/20238115/107843707-4af71f80-6d9b-11eb-8bf3-e7acd478323b.png)
- Stop the connection and exit the app:<br>
  ![image](https://user-images.githubusercontent.com/20238115/107843709-4df21000-6d9b-11eb-9075-1319b273b496.png)
