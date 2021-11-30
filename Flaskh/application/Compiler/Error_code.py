class Error_code:
    def Error_String_formatting(self, error_string: str):
        if error_string == "":
            return_string = "Unexpected Error"
        else:
            error_index = error_string.index('error')
            error_line = error_string[error_index + 6:]
            error_line.replace("/", " ")
            return_string = error_line
        return return_string