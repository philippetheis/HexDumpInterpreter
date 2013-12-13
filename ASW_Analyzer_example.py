# ---------------------------------------------------------------------------|
# PROJECT   : Template
# MODULE    : Parser
# AUTHORS   : GSI
# ---------------------------------------------------------------------------|

from __future__ import print_function

import sys


# ---------------------------------------------------------------------------|
class ASW_Analyzer_example(object):
    """
    The class provides the parser for hex to Human translation
    
    """

    # -----------------------------------------------------------------------|
    def __init__(self):
        """
        constructor
        """
        
    # -----------------------------------------------------------------------|
    def translate(self, asw):
        """get and parse next answer """
        self.asw = asw


        # parse answer per command
        dictionary = {
            0x42: self._parse_the_answer,
            0xC3: self._parse_the_goal,

        }
        command = asw[1]
        dictionary[command](asw)

        # force output
        sys.stdout.flush()
        
    # -----------------------------------------------------------------------|
    def _parse_the_answer(self, asw):
        """ Analyze THE ANSWER """
        
        # check length
        assert len(asw) == 5
        length = asw[0]
        assert length == 4

        # show message
        message = asw[2:(len(asw))]
        
        print("The Answer to the Ultimate Question of Life, the Universe, and Everything: \n", message)
        

    # -----------------------------------------------------------------------|
    def _parse_the_goal(self, asw):
        """ Analyze THE MISSION """
        
        # show message
        message = asw[2:(len(asw))]
        
        print("Our mission: \n", message)
            

# ---------------------------------------------------------------------------|
if __name__ == "__main__":
    unittest.main()

# ---------------------------------------------------------------------------|
# end of file
