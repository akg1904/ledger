import abc


class ItemInterface(abc.ABC):

    @abc.abstractmethod
    def create_item(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def get_items(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_item_by_code(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_item_by_code(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_item_by_code(self):
        raise NotImplementedError
