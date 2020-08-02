from os import scandir
from os.path import abspath
import os
import importlib
import ntpath


class Loader:
    def __init__(self, path, ext='.whl'):
        self.load_components(path, ext)

    def load_components(self, path, ext):
        files_path_components = self.filter_files_by_ext(path=path, ext=ext)
        for file_path in files_path_components:
            name_component = ntpath.basename(file_path)
            index= name_component.find('-')
            name_component = name_component[:index]
            self.uninstall_package(name_component)
            if self.install_package_whl(file_path):
                if not self.import_component(name_component):
                    print('No fue posible importar el componente: ', name_component)
            else:
                print('No fue posible cargar el componente: ', name_component)

    @staticmethod
    def get_list_files(path):
        return [abspath(arch.path) for arch in scandir(path) if arch.is_file()]

    def filter_files_by_ext(self,path, ext):
        return list(filter(lambda x: x.endswith(ext), self.get_list_files(path)))

    @staticmethod
    def install_package_whl(path):
        try:
            os.system('python3 -m pip install '+'"'+path+'"')
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def import_component(name_component):
        try:
            importlib.import_module(name_component)
            return True
        except ImportError as e:
            print(e)
            return False

    @staticmethod
    def uninstall_package(name_package):
        try:
            os.system('python3 -m pip uninstall -y {}'.format(name_package))
            return True
        except Exception as e:
            print(e)
            return False

