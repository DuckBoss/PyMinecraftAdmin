from service import MCServerAdmin
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A utility for administration control over a minecraft server using the RCON protocol."
    )
    parser._action_groups.pop()
    optional_args = parser.add_argument_group("Optional Arguments")
    optional_args.add_argument('-ip', dest='server_ip', required=False, default=None,
                               help='Enter the Minecraft Server IP')
    optional_args.add_argument('-rcon_port', dest='rcon_port', required=False, default=None,
                               help='Enter the Minecraft Server RCON Port')
    optional_args.add_argument('-rcon_pass', dest='rcon_password', required=False, default=None,
                               help='Enter the Minecraft Server RCON password')

    args = parser.parse_args()
    if args.server_ip and args.rcon_port and args.rcon_password:
        service = MCServerAdmin(args.server_ip, args.rcon_port, args.rcon_password)
    else:
        service = MCServerAdmin()
