from re import split


class Hostname:
    """
    The Hostname class abstracts each line of /etc/hosts file,
    mapping a single IP address to an array of strings, representing
    hostnames accessible by network requests and mapped to these IP addresses
    """

    # TODO - need help - some IP check could be included to validate line's start
    def __init__(self, current_line):
        current_line_array = split(' ', current_line)

        # We can have only one address per line, since it's how hosts file recognizes commands
        # So, our address property can be only a string that will receive current hostname address
        self.address = current_line_array[0]  # first value we'll our IP address

        # Identify if our current line is commented
        self.is_commented = self.address.startswith('#')

        # Identify if our current IP address it's pointing to localhost
        self.is_localhost = self.address == '127.0.0.1'

        # Since the hosts file can hold more than one host, we'll split all strings when receiving our
        # information and put all name values here
        current_line_array.pop(0)
        self.hostname = current_line_array
