
class ServiceException(Exception):

  def __init__(self,  errorMessage):
          Exception.__init__(self)

          self.errorMessage = errorMessage

