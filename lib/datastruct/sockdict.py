class Sockdict(dict):
    """
    >>> sockd = Sockdict()
    >>> try:
        >>> sockd.set_address_of_socket("192.168f.0.1", "4753")
    >>> except KeyError as e:
        >>> print(f"Error: {e}")

    >>> print(sockd)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            super().__setitem__(key, value)
        else:
            super().__setitem__(key, value)  # Use super to add the key-value pair

    def set_address_of_socket(self, ip, port):
        # NOTE: Use nmap to gather port
        _ = self[ip] = port
        return _


