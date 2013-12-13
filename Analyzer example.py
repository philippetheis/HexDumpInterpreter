# ---------------------------------------------------------------------------|
# PROJECT   : Template
# MODULE    : Analyze comunication in hex
# AUTHORS   : GSI
# ---------------------------------------------------------------------------|
from __future__ import print_function

import ASW_Analyzer_example


# ---------------------------------------------------------------------------|
class Analyzer(object):
    """
        This class can be used as a hex Analyzer
    """

    # -----------------------------------------------------------------------|
    def __init__(self, *args, **kwargs):
        super(Analyzer, self).__init__(*args, **kwargs)
        self.an = ASW_Analyzer_example.ASW_Analyzer_example()
        
    # -----------------------------------------------------------------------|
    def setUp(self):
        pass

    # -----------------------------------------------------------------------|
    def analyze_log(self):
        """ analyze a hex log file """
        
        an = self.an
        
        # open the log file
        log_hex = open('skynet.log', 'r')
        
        # generate a Command file
        
        # loop for analyzing every line in the log file
        for line in log_hex:
                            
            hex_array = line.split(" ")
            print("\n")
            print(hex_array)
    
            # ascii array to hex array
            for i in range(len(hex_array)):
                hex_array[i] = int(hex_array[i], 16)             
            an.translate(asw = hex_array)
            print("---------------------------------------")
            
# ---------------------------------------------------------------------------|
if __name__ == "__main__":

    az = Analyzer()
    
    az.analyze_log()

# ---------------------------------------------------------------------------|
# end of file
