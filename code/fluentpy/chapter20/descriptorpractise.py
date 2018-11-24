import abc

class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#'




class Account:
    def __init__(self, user, account, password, description):
        self.user = user
        self.account = account
        self.password = password
        self.description = description

    def __repr__(self):
        return f"""<Account,user={self.user},
        account={self.account},
        password={self.password}\n
        description:\n{self.description}>"""

