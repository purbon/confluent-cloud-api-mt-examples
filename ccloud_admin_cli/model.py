import yaml


class ResourceApi:

    def __init__(self):
        self.service = None

    def open(self, resource_file):
        with open(resource_file, 'r') as file:
            self.service = yaml.safe_load(file)