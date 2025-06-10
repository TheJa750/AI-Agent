import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(target_file)):
        try:
            os.makedirs(os.path.dirname(target_file))
        except Exception as e:
            return f'Error: creating file: {e}'
        
    with open(target_file, "w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description="Writes to a file, constrained to the working directory, will create all neccessary directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path for the destination file to be written to. Required."
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The information to be written to the file. Required."
                ),
            },
        ),
    )