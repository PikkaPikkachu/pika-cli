"""
pika

Usage:
  pika hello
  pika play
  pika attack
  pika -h | --help
  pika --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  pika hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/PikkaPikkachu/pika-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)


    for k, v in options.iteritems():
        if hasattr(commands, k) and v == True:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            print command
            command.run()
