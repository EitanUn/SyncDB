"""
Author: Eitan Unger
Date: 08/11/22
Base Database class for the IPC-sync database project, very similar to a regular dictionary
"""


class DB:
    """
    Base database class
    """
    def __init__(self):
        """
        Constructor for DB class
        """
        self.database = {}

    def set_value(self, key, val):
        """
        If key is a key in the database dictionary, change its value to val. Else, add key: val as a pair to the dict
        :param key: key to check
        :param val: value to set
        :return: succeeded (True/False)
        """
        self.database.update({key: val})
        return True

    def get_value(self, key):
        """
        Return the value of key if it is a key in dict, else None
        :param key: key to check
        :return: self.database[key] if key is a key in the dict, else None
        """
        return self.database[key] if key in self.database.keys() else None

    def delete_value(self, key):
        """
        Deletes the value of key in the dict and returns it, if nonexistent raise KeyError
        :param key: key to check
        :return: deleted value if successfull
        """
        return self.database.pop(key)
