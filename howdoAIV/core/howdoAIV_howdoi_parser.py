from howdoi import howdoi

class HowdoAIV_Parser:
    def __init__(self, search_engine = 'google'):
        self.parser= howdoi.get_parser()
        self.search_engine= search_engine
    
    def howdoAIV_query(self,query)->str:
        return howdoi.howdoi(query + " -e " + self.search_engine)