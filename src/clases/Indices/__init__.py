# from os.path import dirname, basename, isfile, join
# import glob

# modules = glob.glob(join(dirname(__file__), "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# import os
# for module in os.listdir(os.path.dirname(__file__)):
#     if module == '__init__.py' or module[-3:] != '.py':
#         continue
#     __import__(module[:-3], locals(), globals())
# del module

import sys
sys.path.append("C:\\Users\\Javi\\Documents\\SistemasWeb\\bambina\\backend\\src\\clases\\conexion")