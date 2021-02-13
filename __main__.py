from service import MCServerAdmin
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A utility for administration control over a minecraft server using the RCON protocol."
    )
    parser._action_groups.pop()
    required_args = parser.add_argument_group("Required Arguments")
    required_args.add_argument('-ip', dest='server_ip', required=True, default='127.0.0.1',
                               help='Enter the Minecraft Server IP')
    required_args.add_argument('-rcon_port', dest='rcon_port', required=True, default=25575,
                               help='Enter the Minecraft Server RCON Port')
    required_args.add_argument('-rcon_pass', dest='rcon_password', required=True, default=None,
                               help='Enter the Minecraft Server RCON password')


    args = parser.parse_args()
    service = MCServerAdmin(args.server_ip, args.rcon_port, args.rcon_password)
