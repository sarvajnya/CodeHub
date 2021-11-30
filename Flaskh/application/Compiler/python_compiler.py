import os
from subprocess import Popen, PIPE, check_output, call, CalledProcessError
from application.Compiler.Error_code import Error_code

import code
import sys
from io import StringIO



class python_compiler:
    def compile_python(self, code_to_compile: str, arg: any, has_arg: bool) -> any:
        try:
            result_string = ""

            data, temp = os.pipe()
            if has_arg:
                os.write(temp, bytes(arg + "\n", "utf-8"))
            else:
                os.write(temp, bytes("" + "\n", "utf-8"))
            os.close(temp)

            # executing class file for the main execution
            cmd = 'python ' + code_to_compile
            popen_result = check_output(cmd, shell=True, stdin=PIPE, stderr=PIPE, universal_newlines=True, bufsize=1)
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

        # codeOut = StringIO()
        # codeErr = StringIO()
        # sys.stdout = codeOut
        # sys.stderr = codeErr
        # sys.argv = arg
        # exec(code_to_compile, {"send": 10})
        # sys.stdout = sys.__stdout__
        # sys.stderr = sys.__stderr__
        # s = codeErr.getvalue()
        # print("error:\n%s\n" % s)
        # s = codeOut.getvalue()
        # print("output:\n%s" % s)
        # codeOut.close()
        # codeErr.close()

        # script_descriptor = open(code_to_compile)
        # a_script = script_descriptor.read()
        # if has_arg:
        #     sys.argv = [code_to_compile, arg]
        # else:
        #     sys.argv = [code_to_compile]
        #
        # exec(a_script)
        #
        # script_descriptor.close()

