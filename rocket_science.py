from numpy.random import uniform

class ArticleClassifier(object):
    """ ArticleClassifier contains a state-of-the-art (not) machine learning model. 
            Given an <article_id> and a <user_id>, it outputs the user's predicted interest level (float :0-1) for the article
    Args:
        article_id  (integer): Article Identifier
        user_id     (integer): User Identifier
        return_result (Bool) : Whether or not to return the result after computation and store. (Default=True)
    Returns:
        [float]: User's predicted interest level in the article (If return_result=True)
    Example: 
        > response = ArticleClassifier().run(article_id=123, user_id=358)
        > print(response)
    """

    def __init__(self, return_result=True):
        """Initialization"""
        self.return_result = return_result

    def run(self, article_id, user_id):
        """Main RUN method. Fetches the article, runs the classifier, stores the result and returns it if return_result = True"""
        article_text = self.get_article(article_id)
        result = self.classifier(article_text, user_id)
        self.store_result(article_id, user_id, result)
        if self.return_result:
            return result


    def get_article(self, article_id):
        """ Fetch the article's text from database and return it as a string """
        raise Exception("You must implement the get_article() method which fetches the article's text and returns it as a string")

    def store_result(self, user_id, article_id, result):
        """ Store the predicted result in the database """
        raise Exception("You must implement the store_result() method which stores the result in the storage engine")

    @staticmethod
    def classifier(article_text, user_id):
        """ Our research has proven that whether the level of interest correlates with :
            whether the user_id is odd or even and the length of the article's text """
        if user_id % 2 == 0:
            if len(article_text.split(" ")) % 2 == 0:
                return uniform(0,1,1)[0]
            else:
                return 0.0    
        else:
            if len(article_text) > 120:
                return 1.0
            else:
                return uniform(0,1,1)[0]


