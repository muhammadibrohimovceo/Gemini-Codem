import json
from pydantic import BaseModel, Field

class ToolDefenition:
	def __init__(self, name, description, input_schema, function):
		self.name = name
		self.description = description
		self.input_schema = input_schema
		self.function = function


def read_file(input_data):
	input_dict = json.loads(input_data)
	path = input_dict["path"]

	try:
		with open(path, "r") as file:
			content = file.read()

		return content, None

	except Exception as e:
		return "", str(e)

class ReadFileInput(BaseModel):
	path: str = Field(
		description="The relative path of file in the working directory."
	)


read_file_defenition = ToolDefenition(
	name = "read_file",
	description = "Read the contents of a given realtive path. Use this whan you want to see what's inside a file. Do not use this with directory names.",
	input_schema = ReadFileInput.model_json_schema(),
	function = read_file,
)