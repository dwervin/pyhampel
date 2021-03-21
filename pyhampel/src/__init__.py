
import importlib
import inspect

from .filtering import *
from .multiproc_filtering import *
from .filtering_with_dev import *
from .multiproc_filtering_w_dev import *

code_hampel_with_dev = 'HampelWithDev.py'
code_out1 = open(code_hampel_with_dev, 'w')

print("Writing local code files needed for multiprocessing")

moda = importlib.import_module('pyhampel.src.HampelWithDev')
src_code = inspect.getsource(moda)
code_out1.write(src_code)
code_out1.close()

# second file
code_hampel = 'HampelFiltering.py'
code_out2 = open(code_hampel, 'w')

# print("Writing local code file needed for multiprocessing")

modb = importlib.import_module('pyhampel.src.HampelFiltering')
src_code2 = inspect.getsource(modb)
code_out2.write(src_code2)
code_out2.close()
