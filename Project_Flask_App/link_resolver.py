
#############################
#                           #
##     Bleach | Linker     ##
##  convert text to link   ##
#                           #
#############################

from bleach.linkifier import Linker

class LinkResolver:

    def __init__(self):
        '''
            Class constructor
            Class to linkify the text using bleach module.
        '''
        self.linker = Linker()
    
    def resolve_link(self, bot_response):
        '''
            Function to linkify the bot response.
            Return the linkified bot response using bleach module.
            The link in the response is linkified in the process.
        '''
        
        response = self.linker.linkify(bot_response)

        return response

