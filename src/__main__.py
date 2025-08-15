import os
import sys
from src.commands import Commands, ProjectOpener
from src.configurator import Configurator

def main():
    first_argument = sys.argv[1]

    configurator = Configurator()
    project_opener = ProjectOpener(first_argument, configurator)

    if not project_opener.open_folder():
        return

    # match(first_argument):
    #     case Commands.SET_PROJECTS_PATH:
    #         new_projects_path = os.path.abspath(sys.argv[2])
    #         configurator.setproperty(Configurator.CONFIG_MAIN_AREA, Configurator.PROJECTS_FOLDER, new_projects_path)
    #     case Commands.SET_SASS_PATH:
    #         new_sass_path = os.path.abspath(sys.argv[2])
    #         configurator.setproperty(Configurator.CONFIG_MAIN_AREA, Configurator.SASS_FOLDER, new_sass_path)
    #     case _:
    #         print(f"Error: \033[1m{first_argument}\033[0m is not a valid command")
            

if __name__ == "__main__":
    main()