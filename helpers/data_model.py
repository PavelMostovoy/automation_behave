# -----------------------------------------------------------------------------
# DATA - model:
# -----------------------------------------------------------------------------



class DataModel:
    """
    Data

    """

    def __init__(self):
        self.users = dict()

    def add_user(self, name: str, phone: str, e_mail: str, comments: str,):

        for user in self.users:
            assert name != self.users[user].name, "User name not unique"
        self.users[name] = User(name, phone, e_mail, comments)



class User:
    """
    Data model for user that used in test scenarios

    """

    def __init__(self, name, phone, e_mail, comments):
        """

        :param name:
        :param phone:
        :param e_mail:
        :param comments:
        """
        self.name = name
        self.phone = phone
        self.e_mail = e_mail
        self.comments = comments
