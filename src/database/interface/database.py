
import abc


class Database(abc.ABC):

    def __int__(self):
        pass

    @abc.abstractmethod
    def get_connection(self):
        raise NotImplementedError
