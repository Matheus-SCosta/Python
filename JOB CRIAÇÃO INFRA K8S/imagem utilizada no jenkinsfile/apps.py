class app:
    def __init__(self, name_app: str = None, ambiente: str = None, new_branch: str = None):
        self.__name_app = name_app
        self.__ambiente = ambiente
        self.__new_branch = new_branch
        self.__name_deployment = name_app + "-deployment.yaml"
        self.__name_ingress = name_app + "-ingress.yaml"
        
    
    # GETS
    def get_name_app(self):
	    return self.__name_app     
 
    def get_ambiente(self):
        	return self.__ambiente
    
    def get_name_deployment(self):
    	return self.__name_deployment
     
    def get_name_ingress(self):
    	return self.__name_ingress
 
    def get_new_branch(self):
        return self.__new_branch
 
 
    # SETS
    def set_name_app(self, name_app: str = None):
        self.__name_app = name_app
         
    def set_ambiente(self, ambiente: str = None):
        self.__ambiente = ambiente
        
    def set_new_branch(self, new_branch: str = None):
        self.__new_branch = new_branch    
        
    # PROPERTY    
    name_app = property(get_name_app, set_name_app)
    ambiente = property(get_ambiente, set_ambiente)
    name_deployment = property(get_name_deployment)
    name_ingress = property(get_name_ingress)
    new_branch = property(get_new_branch, set_new_branch)
