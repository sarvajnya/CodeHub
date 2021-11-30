from subprocess import check_output, check_call, Popen, PIPE, CalledProcessError
import os
from application.compiler_path import compiler_path
from application.Compiler.Error_code import Error_code


class c_compiler:
    def executeC(self, code_to_compile: str, arg: any, has_args: bool) -> any:
        return_string = ""
        try:
            data, temp = os.pipe()

            # Creating Pre-defined input Pipe
            if has_args:
                os.write(temp, bytes(arg + "\n", "utf-8"))
            os.close(temp)

            # Compiling C++ file and creating Cpp_out1.exe for execution with strdin = data pipLine
            cmd_string = "gcc " + code_to_compile + " -o sample_out_c"
            check_output(cmd_string, stdin=data, stderr=PIPE, shell=True,
                         env={'PATH': compiler_path.c_path})

            # Executing cpp_out1.exe for main execution of the code
            # subprocess.check_call("gcc HelloWorld.c -o out1", shell=True,  env={'PATH': 'C:/MinGW/bin'})
            popen_result = check_output("sample_out_c", stdin=data, shell=True, env={'PATH': compiler_path.c_path})
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
