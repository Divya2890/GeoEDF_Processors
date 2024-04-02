#!/usr/bin/env python3

import os
import subprocess
from subprocess import CalledProcessError

from geoedfframework.GeoEDFPlugin import GeoEDFPlugin
from geoedfframework.utils.GeoEDFError import GeoEDFError

"""Module for running the 01_data_clean R script that helps process the 
   FAOSTAT data for preparing the SIMPLE database.
"""

class SimpleDataProc(GeoEDFPlugin):

    # required inputs are:
    # (1) input directory where the CSV files from FAO have been stored
    # (2) start year
    # (3) end year


    __required_params = ['input_dir','start_year','end_year']

    # we use just kwargs since this makes it easier to instantiate the object from the 
    # GeoEDFProcessor class
    def __init__(self, **kwargs):

        #list to hold all parameter names
        self.provided_params = self.__required_params 

        # check that all required params have been provided
        for param in self.__required_params:
            if param not in kwargs:
               raise GeoEDFError('Required parameter %s for SimpleDataClean not provided' % param)
           
        # set all required parameters
        for key in self.__required_params:
            setattr(self,key,kwargs.get(key))

            
        self.data_proc_script = '/usr/local/bin/02_data_proc.r'

        # super class init
        super().__init__()

    # the process method that calls the 01_data_clean.r script 
    def process(self):

        # the R script is invoked with the following command line arguments:
        # 1. start year
        # 2. end year
        # 3. input directory where FAO files are stored
        # 4. output directory

        # dummy init to catch error in stdout
        stdout = ''

        try:
            for i in range(int(self.start_year),int(self.end_year)+1):
                command = "Rscript"
                args = [str(i),self.input_dir,self.target_path]
                
                cmd = [command, self.data_proc_script] + args

                stdout = subprocess.check_output(cmd,universal_newlines=True)

        except CalledProcessError:
            raise GeoEDFError('Error occurred when running data_proc processor: %s' % stdout)
            
            
        

    
