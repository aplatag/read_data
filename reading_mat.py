"""
Class to read data type ".Mat"
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Libraries
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Libraries:
from  scipy.io import loadmat


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Class
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ReadingMat:
    def __init__(self,path_data):
        self.path_data = path_data
    
    def variable_names(self):
        #initialization:
        path = self.path_data
        # main
        data_content = loadmat(path)
        variables = data_content.keys()

        for variable_name in variables:
            if not variable_name.startswith('__'):
                variable_value = data_content [variable_name]
                print(f'Variable: {variable_name}, Type value: {type(variable_value)}')

        
    def read_variable(self,variable):
        #initialization:
        path = self.path_data
        variable_name = variable        

        # main
        data_content = loadmat(path)
        data = data_content[variable_name ]
        
        return data

