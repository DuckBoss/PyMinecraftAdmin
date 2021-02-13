<h2 align="center"> PyMineCraftAdmin </h2>
<p align="center">A simple GUI utility to remotely control a MineCraft Server using the RCON protocol</p>
<br>
<br>

### Requirements
- Python 3.7+
- <code>pip install -r requirements.txt</code>

### Usage
1) Run the folder module in python with the server IP, rcon port and rcon password as launch parameters:
```
> python PyMineCraftAdmin/ -ip <my_server_ip> -rcon_port <my_rcon_port> -rcon_pass <my_rcon_password>

(OR)

> cd PyMineCraftAdmin/
> python __main__.py -ip <my_server_ip> -rcon_port <my_rcon_port> -rcon_pass <my_rcon_password>
```
<b>Note: The rcon port/password can be configured in your server's `server.properties` file.</b>

### Examples
- Login to the Minecraft server rcon connection:<br>
  ![image](https://user-images.githubusercontent.com/20238115/107862996-cea62000-6e1e-11eb-9a10-c9e336997022.png)
- Send commands to the server with a response:<br>
  ![image](https://user-images.githubusercontent.com/20238115/107862979-afa78e00-6e1e-11eb-9b20-060242a9e699.png)
