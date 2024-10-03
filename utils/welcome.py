class Session(object):

    def __init__(self) -> None:
        
        self.language = None
        self.embedding_type = None
        self.operation = None
        self.explain_path = None
        self.cluster_path = None

    def set_params(self, language, embedding_type, operation, explain_path, cluster_path):
        self.language = language
        self.embedding_type = embedding_type
        self.operation = operation
        self.explain_path = explain_path
        self.cluster_path = cluster_path       

    def set_language(self, language):
        self.language = language

    def set_embedding_type(self, embedding_type):
        self.embedding_type = embedding_type

    def set_operation(self, operation):
        self.operation = operation

    def set_explain_path(self, explain_path):
        self.explain_path = explain_path

    def set_cluster_path(self, cluster_path):
        self.cluster_path = cluster_path

    def get_language(self):
        return self.language
    
    def get_embedding_type(self):
        return self.embedding_type
    
    def get_operation(self):
        return self.operation
    
    def get_explain_path(self):
        return self.explain_path
    
    def get_cluster_path(self):
        return self.cluster_path



