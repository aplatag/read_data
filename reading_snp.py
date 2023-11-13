"""
Function to read data type ".snp"
"""
#=======================================================================================================
# Libraries
#======================================================================================================
# Libraries:
from pylab import *
import skrf as rf
rf.stylely()

import skrf


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Classes
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class ReadingSnp:
    def __init__(self,path_data):
        self.path_data = path_data
    
    #================================================================
    # Graph all parameters
    #=================================================================
    
    def plot_snp_all(self,option):
        #initialization:
        path_full = self.path_data
        type_opt = option

        #main:
        if type_opt == 'dB':                  
            red = skrf.Network(path_full)  
            red.plot_s_db(lw=2)
            plt.show()

        elif type_opt == 'smith':
                                        
            red = skrf.Network(path_full)  
            red.plot_s_smith(lw=2)
            plt.show()
        
        elif type_opt == 'deg':
                                         
            red = skrf.Network(path_full)  
            red.plot_s_deg(lw=2)
            plt.show()
        else: 
            raise ValueError("\033[91m Option invalid. \033[0m")
    #================================================================
    # Graph one parameter S
    #=================================================================
    def plot_snp_data(self,option,parameter_s):
        #initialization:
        path_full = self.path_data
        type_opt = option
        parameter=parameter_s

        #main:
        if  parameter == 'S11':
            m=0
            n=0
        elif parameter == 'S12':
            m=0
            n=1
        elif parameter == 'S21':
            m=1
            n=0
        elif parameter == 'S22':
            m=1
            n=1
        else:
            raise ValueError("\033[91m Unidentified S parameter. \033[0m")

        
        if type_opt == 'dB':
            try:       
                red = skrf.Network(path_full)  
                red.plot_s_db(m,n,lw=2)
                plt.show()
            except Exception as e:
                print(f"\033[91m An exception occured: {type(e).__name__} \033[0m")
                print(f" \033[91m Error processing path {path_full} \033[0m")

        elif type_opt == 'smith':
            try:                          
                red = skrf.Network(path_full)  
                red.plot_s_smith(m,n,lw=2)
                plt.show()
            except Exception as e:
                print(f"\033[91m An exception occured: {type(e).__name__} \033[0m")
                print(f" \033[91m Error processing path {path_full} \033[0m")   

        elif type_opt == 'deg':
            try:                             
                red = skrf.Network(path_full)  
                red.plot_s_deg(m,n,lw=2)
                plt.show()
            except Exception as e:
                print(f"\033[91m An exception occured: {type(e).__name__} \033[0m")
                print(f" \033[91m Error processing path {path_full} \033[0m")
        else: 
            raise ValueError("\033[91m Option invalid. \033[0m")
         
    #================================================================
    # Read the parameters S
    #=================================================================

    def read_snp_data(self,option,parameter_s):

        #initialization:
        path_full = self.path_data
        type_opt = option
        parameter=parameter_s
        
        #main:
        if  parameter == 'S11':
            m=0
            n=0
        elif parameter == 'S12':
            m=0
            n=1
        elif parameter == 'S21':
            m=1
            n=0
        elif parameter == 'S22':
            m=1
            n=1
        else:
            raise ValueError("\033[91m Unidentified S parameter. \033[0m")

       
        if type_opt == 'RI':        

            try:
                red = skrf.Network(path_full)
                                    
                Snn_real = red.s_re[:,m,n]
                Snn_imag = red.s_im[:,m,n]               
                snn = [complex(r, i) for r, i in zip(Snn_real , Snn_imag )]                                                                   
                frequency = red.f
                

            except Exception as e:
                print(f"\033[91m An exception occured: {type(e).__name__} \033[0m")
                print(f" \033[91m Error processing path {path_full} \033[0m")
          
        elif type_opt == 'dB':
                
            try:            
                red = skrf.Network(path_full)                               
                Snn_db = red.s_db[:,m,n]
                Snn_deg = red.s_deg[:,m,n]              

                snn = [(r, i) for r, i in zip(Snn_db , Snn_deg)]
                frequency = red.f
               

            except Exception as e:
                print(f"\033[91m An exception occured: {type(e).__name__} \033[0m")
                print(f"\033[91m  Error processing path {path_full} \033[0m")
          
        elif type_opt == 's':

            try:
                red = skrf.Network(path_full)                               
                snn = red.s[:,m,n]           
                frequency = red.f
                

            except Exception as e:
                print(f"\033[91m  An exception occured: {type(e).__name__} \033[0m")
                print(f"\033[91m  Error processing path {path_full} \033[0m")
        
        else:
            raise ValueError("\033[91m Option invalid. \033[0m")
        
        return snn, frequency
                    
        
        








