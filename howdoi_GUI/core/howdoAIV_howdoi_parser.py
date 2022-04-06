from howdoi import howdoi

class HowdoAIV_Parser:
    def __init__(self):
        self.parser= howdoi.get_parser()
        
    
    def howdoAIV_query(self,query)->str:
       args = self.parser.parse_args(query.split(' '))
       return howdoi.howdoi(args)