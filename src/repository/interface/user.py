import abc


class UserInterface(abc.ABC):

    @abc.abstractmethod
    def create_user(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def update_user_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user_by_id(self, id):
        raise NotImplementedError

