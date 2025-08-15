import os
import configparser

CONFIG_FILE_NAME = "config.cfg"
USER_PATH = os.path.expanduser("~")

class Configurator:
    CONFIG_MAIN_AREA = "main"
    PROJECTS_FOLDER = "projects_folder"
    SASS_FOLDER = "sass_folder"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE_NAME)

        if not self.config.has_section(Configurator.CONFIG_MAIN_AREA):
            documents = f"{USER_PATH}\\Documents"
            sass = f"{documents}\\sass"

            self.setproperty(Configurator.CONFIG_MAIN_AREA, Configurator.PROJECTS_FOLDER, documents)
            self.setproperty(Configurator.CONFIG_MAIN_AREA, Configurator.SASS_FOLDER, sass)

    def getproperty(self, section: str, name: str) -> str | None:
        if self.config.has_option(section, name):
            return self.config.get(section, name)

        return None

    def setproperty(self, section: str, name: str, value: str):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, name, value)

        with open(CONFIG_FILE_NAME, "w") as config_file:
            self.config.write(config_file)