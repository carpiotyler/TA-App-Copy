from Managers.myStorageManager import AbstractStorageManager
from abc import ABC, abstractmethod


class ManagerInterface(ABC):
    @abstractmethod
    def __init__(self, database: AbstractStorageManager):
        pass

    @abstractmethod
    def add(self, fields: dict)->bool:
        pass

    @abstractmethod
    def view(self, fields: dict)->str:
        pass

    @abstractmethod
    def edit(self, fields: dict)->bool:
        pass

    @abstractmethod
    def delete(self, fields: dict)->bool:
        pass

    @staticmethod
    @abstractmethod
    def reqFields()->list:
        pass

    @staticmethod
    @abstractmethod
    def optFields()->list:
        pass
