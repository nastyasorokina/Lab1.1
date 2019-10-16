"""
JSON, XML and YAML Parsers
"""

import json
import xml.dom.minidom as md
import yaml
    



class JsonWriter():
    
    
    
    """
    JSON Parser
    """

    def __init__(self, data=None):
        self.data = data

    def __repr__(self):
        return json.dumps(self.data, sort_keys=True, indent=4)

    def from_file(self, route):
        """
        Read data from file
        Arguments:
            route {string} -- file's path
        """
    
        try:
            with open(route, "r") as read_file:
                self.data = json.load(read_file)
        except FileNotFoundError:
            print('File Not Found')

    def to_file(self, route):
        """
        Write self.data to file
        Arguments:
            route {string} -- file's path
        """
        if self.data is None:
            print('Empty data')
        with open(route, "w") as write_file:
            json.dump(self.data, write_file, indent=4)

    def to_file_sorted(self, route):
        """
        Write sorted self.data to file
        Arguments:
            route {string} -- file's path
        """
        with open(route, "w") as write_file:
            json.dump(self.data, write_file, sort_keys=True, indent=4)
