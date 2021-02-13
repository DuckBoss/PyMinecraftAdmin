from time import sleep
from mcrcon import MCRcon


class MCServerAdmin:
    def __init__(self, ip, port, password):
        self.exit_flag = False
        self.ip = ip
        try:
            self.port = int(port)
        except ValueError:
            raise ValueError("The Minecraft Server RCON port must be an integer (1-65535)")
        self.mcr_instance = MCRcon(host=self.ip, port=self.port, password=password)
        self.mcr_instance.connect()
        self.loop()

    def loop(self):
        while not self.exit_flag and self.mcr_instance:
            cmd_input = input("Enter a command: ")
            if cmd_input == "!quit":
                self.exit_flag = True
                self.exit()
                return
            elif cmd_input[0] != "/":
                cmd_input = f"say {cmd_input}"
            else:
                cmd_input = cmd_input[1:]
            resp = self.mcr_instance.command(cmd_input)
            print(resp)
            sleep(0.1)
        self.exit()

    def exit(self):
        if self.mcr_instance:
            self.exit_flag = True
            self.mcr_instance.disconnect()
