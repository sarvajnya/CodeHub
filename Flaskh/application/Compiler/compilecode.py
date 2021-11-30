from application.Compiler.java_compiler import java_compiler
from application.Compiler.python_compiler import python_compiler
from application.Compiler.Ccompiler import c_compiler
from application.Compiler.cppcompiler import cpp_compiler
from application.Compiler.CSharp_compiler import csharp_compiler
import os


def Compile(code: str, compiler: str, arg: any):
    compiler = compiler.upper()
    arg = arg.strip()
    has_arg = True
    if arg == "":
        has_arg = False
    result = ""
    code_file = creating_file(code, compiler)
    if compiler == "JAVA":
        # region Java Compiler
        compiler_java_code = java_compiler()
        result = compiler_java_code.compile_java(code_file, arg, has_arg)
        # endregion
    elif compiler == "C":
        # region C Compiler
        C_compiler_code = c_compiler()
        result = C_compiler_code.executeC(code_file, arg, has_arg)
        # endregion
    elif compiler == "C++":
        # Region Cpp Compiler
        cpp_compiler_code = cpp_compiler()
        result = cpp_compiler_code.executeCpp(code_file, arg, has_arg)
        # Endregion
    elif compiler == "PYTHON":
        # region Python Compiler
        compiler_python_code = python_compiler()
        result = compiler_python_code.compile_python(code_file, arg, has_arg)
        # endregion
    elif compiler == "C#":
        # region C# Compiler
        compiler_csharp_code = csharp_compiler()
        result = compiler_csharp_code.compile_CSharp(code_file, arg, has_arg)
        # Endregion
    return result


def creating_file(code_file: str, compiler: str):
    path = "R:\Pace\CompilerFile"  # os.path.dirname(__file__)
    file_name = path + "\Sample"
    if compiler == "C":
        file_name = file_name + ".c"
    elif compiler == "C++":
        file_name = file_name + ".cpp"
    elif compiler == "C#":
        file_name = file_name + ".cs"
    elif compiler == "PYTHON":
        file_name = file_name + ".py"
    elif compiler == "JAVA":
        file_name = file_name + ".java"

    # if os.path.exist(file_name):
    #     os.remove(file_name)
    f = open(file_name, "w")
    f.write(code_file)
    f.close()
    return file_name
