import os
from google.adk.agents.llm_agent import Agent, Workflow



def list_all_files() -> str:
    """
    List all files and folders in the current directory,

    returns:
        A formatted string containing all entries or an error message.

    """

    try:
        items = os.listdir('/Users/varshasingh/Desktop')
        if not items:
            return "the current directory is empty"
        result = "contents of the current directory\n"
        for name in items:
            if os.path.isfile(name):
                size = os.path.getsize(name)
                size_kb = size / 1024
                result += f"[FILE] : {name} | Size : {size_kb} KB\n"

            elif os.path.isdir(name):
                result += f"[DIR] : {name}\n"

        return result

    except Exception as e:
        return f"Error listing directory: {e}"


root_agent = Workflow(
   model='gemini-3.5-flash',
   name='root_agent',
    description='A helpful assistant for user questions.',
   instruction='Answer user questions to the best of your knowledge',
    tools=[list_all_files]
)
