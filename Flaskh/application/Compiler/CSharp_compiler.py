import code
import os
from io import StringIO
from subprocess import Popen, PIPE, check_output, CalledProcessError
from flask_mongoengine import json
from application.compiler_path import compiler_path
from application.Compiler.Error_code import Error_code


class csharp_compiler:
    def __init__(self):
        pass

    def compile_CSharp(self, code_to_compile: str, arg: any, has_arg: bool) -> any:
        try:
            result_string = ""

            data, temp = os.pipe()
            if has_arg:
                os.write(temp, bytes(arg + "\n", "utf-8"))
            else:
                os.write(temp, bytes("" + "\n", "utf-8"))
            os.close(temp)

            # executing class file for the main execution

            cmd = compiler_path.csharp_path + " /out:Sample.exe " + code_to_compile
            proc = check_output(cmd, shell=True, stderr=PIPE)

            cmd = 'Sample'
            popen_result = check_output(cmd, shell=True, stdin=PIPE, stderr=PIPE, universal_newlines=True, bufsize=1)

            # output formatting
            return_string = popen_result

        except CalledProcessError as e:
            error_string = str(e.stderr)
            if error_string == "":
                return_string = "Unexpected Error"
            else:
                if 'error' in error_string:
                    error_index = error_string.index('error')
                    error_line = error_string[error_index + 6:]
                    error_line.replace("/", " ")
                else:
                    error_line = error_string
                return_string = error_line
        except Exception as e:
            error_string = e
            if error_string == "":
                return_string = "Unexpected Error"
            else:
                if 'error' in error_string:
                    error_index = error_string.index('error')
                    error_line = error_string[error_index + 6:]
                    error_line.replace("/", " ")
                else:
                    error_line = error_string
                return_string = error_line
        return return_string
