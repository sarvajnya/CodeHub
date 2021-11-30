import json
from subprocess import check_output, check_call, Popen, PIPE, CalledProcessError
import os
from application.compiler_path import compiler_path
from application.Compiler.Error_code import Error_code


class cpp_compiler:

    def executeCpp(self, code_to_compile: str, arg: any, has_args: bool) -> any:
        # Creating Pre-defined input Pipe
        return_string = ""
        try:
            data, temp = os.pipe()
            error = ""

            # write to STDIN as a byte object(convert string to bytes with encoding utf8)
            if has_args:
                os.write(temp, bytes(arg + "\n", "utf-8"))
            else:
                os.write(temp, bytes("" + "\n", "utf-8"))
            os.close(temp)
            path = "g++ " + code_to_compile + " -o sample_out.out"
            # store output of the program as a byte string in cpp_output.exe for main execution
            check_output(path, stdin=data, stderr=PIPE, shell=True,
                                    env={'PATH': compiler_path.cpp_path})

            # execute cpp_output for main execution
            # check_call("sample_out.out", stdin=data, stderr=PIPE, shell=True, env={'PATH': 'C:/MinGW/bin'})
            popen_result = check_output("sample_out.out", stdin=data, stderr=PIPE, shell=True,
                                 env={'PATH': compiler_path.cpp_path})
            return_string = popen_result

            # decode s to a normal string
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


