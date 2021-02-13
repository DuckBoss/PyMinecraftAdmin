from mcrcon import MCRcon
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class MCServerAdmin:
    def __init__(self, ip=None, rcon_port=None, rcon_pass=None):
        self.tk_window = tk.Tk()
        self.tk_style = ttk.Style(self.tk_window)
        self.tk_window.call('source', 'azure/azure.tcl')
        self.tk_style.theme_use('azure')
        self.tk_window.withdraw()

        if not ip and not rcon_port and not rcon_pass:
            self.generate_login_ui()
        else:
            self.connectToServer(ip, rcon_port, rcon_pass)
            self.generate_main_ui()
        self.tk_window.mainloop()

    def generate_main_ui(self):
        self.tk_window.deiconify()
        self.tk_window.title(f"PyMineCraft Administration - {self.ip}:{self.port}")

        commandLabel = ttk.Label(self.tk_window, text="Enter a command: ")
        commandLabel.grid(column=0, row=0, padx=10, pady=10, sticky='w')
        commandInput = ttk.Entry(self.tk_window, width=50)
        commandInput.grid(column=0, row=1, padx=10, pady=10, sticky='w')
        sendCommandButton = ttk.Button(self.tk_window, command=lambda: self.processCommand(commandInput.get()) or commandInput.delete(0, len(commandInput.get())),
                                       text='Send Command', style='Accentbutton')
        sendCommandButton.grid(column=0, row=2, padx=10, pady=10, sticky='w')
        self.tk_window.bind('<Return>', lambda x: self.processCommand(commandInput.get()) or commandInput.delete(0, len(commandInput.get())))

        serverResponseLabel = ttk.Label(self.tk_window, text="Server Response:")
        serverResponseLabel.grid(column=0, row=3, padx=10, pady=10, sticky='w')
        self.serverResponseText = ttk.Label(self.tk_window, text="N/A")
        self.serverResponseText.grid(column=0, row=4, padx=10, pady=10, sticky='NSEW')

    def generate_login_ui(self):
        self.tk_window.deiconify()
        self.tk_window.title("PyMineCraft Administration - Login")

        serverIPLabel = ttk.Label(self.tk_window, text="Minecraft Server IP: ")
        serverIPLabel.grid(column=0, row=0, padx=10, pady=10, sticky='w')
        serverIPInput = ttk.Entry(self.tk_window)
        serverIPInput.grid(column=0, row=1, padx=10, pady=10, sticky='w')
        rconPortLabel = ttk.Label(self.tk_window, text="RCON Port: ")
        rconPortLabel.grid(column=1, row=0, padx=10, pady=10, sticky='w')
        rconPortInput = ttk.Entry(self.tk_window)
        rconPortInput.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        rconPasswordLabel = ttk.Label(self.tk_window, text="RCON Password: ")
        rconPasswordLabel.grid(column=0, row=2, padx=10, pady=10, sticky='w')
        rconPasswordInput = ttk.Entry(self.tk_window)
        rconPasswordInput.grid(column=0, row=3, padx=10, pady=10, sticky='w')

        connectButton = ttk.Button(self.tk_window, command=lambda: self.connectToServer(
            serverIPInput.get(), rconPortInput.get(), rconPasswordInput.get()
        ), text='Connect to Server', style='Accentbutton')
        connectButton.grid(column=0, row=4, padx=10, pady=10, sticky='w')
        self.tk_window.bind('<Return>', lambda: self.connectToServer(
            serverIPInput.get(), rconPortInput.get(), rconPasswordInput.get()
        ))

    def connectToServer(self, serv_ip, rcon_port, rcon_pass):
        self.ip = serv_ip
        try:
            self.port = int(rcon_port)
        except ValueError:
            messagebox.showerror("Server Connectivity - ERROR", "The Minecraft Server RCON port must be an integer (1-65535)")
            raise ValueError("The Minecraft Server RCON port must be an integer (1-65535)")
        self.mcr_instance = MCRcon(host=self.ip, port=self.port, password=rcon_pass)
        self.mcr_instance.connect()
        if self.mcr_instance:
            messagebox.showinfo("Server Connectivity - Success", "Successfully connected to the server!")
            self.resetWindow()
            self.generate_main_ui()
        else:
            messagebox.showinfo("Server Connectivity - Failed", "Failed connecting to the server!")

    def resetWindow(self):
        self.tk_window.destroy()
        self.tk_window = tk.Tk()
        self.tk_style = ttk.Style(self.tk_window)
        self.tk_window.call('source', 'azure/azure.tcl')
        self.tk_style.theme_use('azure')

    def processCommand(self, command):
        if self.mcr_instance:
            cmd_input = command.strip()
            if len(cmd_input) == 0:
                return
            elif cmd_input == "!quit":
                self.exit()
                return
            elif cmd_input[0] != "/":
                resp = f"> {cmd_input}"
                cmd_input = f"say {cmd_input}"
                self.mcr_instance.command(cmd_input)
            else:
                cmd_input = cmd_input[1:]
                resp = self.mcr_instance.command(cmd_input)
            print(resp)
            if self.serverResponseText:
                self.serverResponseText.config(text=resp)

    def exit(self):
        if self.mcr_instance:
            self.mcr_instance.disconnect()
        if self.tk_window:
            self.tk_window.destroy()
