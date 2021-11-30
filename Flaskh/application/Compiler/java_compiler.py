import code
import os
from io import StringIO
from subprocess import Popen, PIPE, check_output, CalledProcessError
from flask_mongoengine import json
from application.compiler_path import compiler_path
from application.Compiler.Error_code import Error_code



class java_compiler:
    def __init__(self):
        pass

    def compile_java(self, code_to_compile: str, arg: any, has_arg: bool) -> any:
        try:
            result_string = ""
            # Compiling by javac and creating .class file
            cmd = 'javac ' + code_to_compile
            proc = check_output(cmd, shell=True, stderr=PIPE,
                                env={'PATH': compiler_path.java_path})

            # Creating Pre-defined input Pipe
            data, temp = os.pipe()
            if has_arg:
                os.write(temp, bytes(arg + "\n", "utf-8"))
            else:
                os.write(temp, bytes("" + "\n", "utf-8"))
            os.close(temp)

            # executing class file for the main execution
            cmd = 'java ' + code_to_compile
            popen_result = check_output(cmd, shell=True, stdin=PIPE, stderr=PIPE, universal_newlines=True, bufsize=1,
                                        env={'PATH': compiler_path.java_path})

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

        # except Exception as e:
        #     print(e.output)
        # if e.output.startswith('error: {'):
        #     error = json.loads(e.output[7:])  # Skip "error: "
        #     print(error['code'])
        #     print(error['message'])
        # adding predefined arguments to the code

        # executing class file for the main execution
        # cmd = 'java ' + code_to_compile
        # try:
        #     p = check_output(cmd, shell=True, stdin=PIPE, universal_newlines=True, bufsize=1,
        #             env={'PATH': 'C:/Program Files/Java/jdk-16/bin'})
        # except Exception as e:
        #     print(e.output)
        #     if e.output.startswith('error: {'):
        #         error = json.loads(e.output[7:])  # Skip "error: "
        #         print(error['code'])
        #         print(error['message'])
        # # adding predefined arguments to the code
        # print(p)
        # if has_arg:
        #     out, err =p.communicate(arg)
        # else:
        #     out, err = p.communicate()
        # print(out, err)
