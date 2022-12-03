import constants

#get friction loss coefficient                  
def get_fitting_c (connection, fitting_type):
        return constants.fitting[connection][fitting_type]
        

