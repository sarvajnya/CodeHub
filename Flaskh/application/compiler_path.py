import os
import configparser


class compiler_path:

    def fetch_path(self):
        default_path = os.path.dirname(__file__)
        config = configparser.ConfigParser()
        config.read('path.ini')
        self.java_path = config['DEFAULT']['java_path']
        self.c_path = config['DEFAULT']['c_path']
        self.cpp_path = config['DEFAULT']['cpp_path']
        self.csharp_path = config['DEFAULT']['csharp_path']

    java_path = "C:/Program Files/Java/jdk-16/bin"
    c_path = "C:/MinGW/bin"
    cpp_path = "C:/MinGW/bin"
    csharp_path = "c:/windows/Microsoft.NET/Framework/v3.5/csc.exe"
    python_path = ""
