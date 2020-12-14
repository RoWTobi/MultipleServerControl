# by Tobias Seelinger
# https://sedware.net

"""
Diese Datei beinhaltet die Klasse für die Verbindung zum OS
"""

# Imports
from pypsrp.client import Client


class Connection:
    """
    Klasse für die Verbindung
    """

    def __init__(self, os_type, hostname, username, password, port=None, key_file=None):
        self.os_type = os_type
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.key_file = key_file

        # Predefine Variables
        self.conn = None

        if os_type == "windows":
            self.windows()

        elif os_type == "linux":
            self.linux()

        elif os_type == "macos":
            self.macos()

        else:
            raise Exception("Unknown OS")

    def windows(self):
        """
        Connect to Windows powershell
        :return: True
        """

        self.conn = Client(self.hostname, username=self.username, password=self.password)

    def linux(self):
        """
        Connect to Linux ssh
        :return: True
        """

    def macos(self):
        """
        Connect to MacOS
        :return: True
        """

    def exec_command(self, command, ps=False):
        """
        Diese Funktion führt einen Befehl aus
        :param command: str
        :param ps: PowerShell
        :return:
        """

        if self.os_type == "windows":
            if ps:
                return self.conn.execute_ps(command)
            else:
                return self.conn.execute_cmd(command)

        elif self.os_type == "linux":
            return self.conn.exec_command(command)

        elif self.os_type == "macos":
            return False

        else:
            raise Exception("Unknown OS - Exec Command")

    def send_file(self, local_path, remote_path):
        """
        This function send a file to Remote
        :param local_path: str
        :param remote_path: str
        :return: bool
        """

        if self.os_type == "windows":
            "None"

        elif self.os_type == "linux":
            "None"

        elif self.os_type == "macos":
            "None"

        else:
            raise Exception("Unknown OS - Send File")

    def recv_file(self, local_path, remote_path):
        """
        This Function recv a File from Remote
        :param local_path: str
        :param remote_path: str
        :return: bool
        """

        if self.os_type == "windows":
            "None"

        elif self.os_type == "linux":
            "None"

        elif self.os_type == "macos":
            "None"

        else:
            raise Exception("Unknown OS - Recv File")
