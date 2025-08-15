import os
import sys
import webbrowser
from src.configurator import Configurator

class ProjectOpener:
    def __init__(self, folder_to_open: str, configurator: Configurator):
        self.folder_to_open = folder_to_open
        self.configurator = configurator

        self.sass_folder = configurator.getproperty(Configurator.CONFIG_MAIN_AREA, Configurator.SASS_FOLDER)
        self.projects_folder = configurator.getproperty(Configurator.CONFIG_MAIN_AREA, Configurator.PROJECTS_FOLDER)

        self.projects = list(filter(lambda folder_or_file: os.path.isdir(f"{self.projects_folder}\\{folder_or_file}"), os.listdir(self.projects_folder)))

    def open_folder(self) -> bool:
        if self.folder_to_open in self.projects and len(sys.argv) == 2:
            account_label = "account"
            account = self.configurator.getproperty(self.folder_to_open, account_label)
    
            workspace_label = "workspace"
            workspace = self.configurator.getproperty(self.folder_to_open, workspace_label)

            if not account or not workspace:
                account = input("Register the project account: ")
                self.configurator.setproperty(self.folder_to_open, account_label, account)

                workspace = input("Register the project workspace: ")
                self.configurator.setproperty(self.folder_to_open, workspace_label, workspace)

            print(f"Opening \033[1m{self.folder_to_open}\033[0m project in account \033[1m{account}\033[0m with workspace \033[0m{workspace}\033[0m")

            os.system(f"vtex login {account}")
            os.system(f"vtex use {workspace}")
            os.system(f"code {self.projects_folder}\\{self.folder_to_open} {self.projects_folder}\\{self.sass_folder}")
            
            webbrowser.open_new_tab(f"https://{workspace}--{account}.myvtex.com")

            return True

        print(f"Error: \033[1m{self.folder_to_open}\033[0m folder does not exists")
        return False