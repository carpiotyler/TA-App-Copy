from Managers.DjangoStorageManager import DjangoStorageManager as dsm
from Managers.managerInterface import ManagerInterface
from TAServer.models import Section
import abc


class SectionManager(ManagerInterface):

    def __init__(self, dsm):
        self.db = dsm

    def add(self, fields: dict)->bool:
        pass

    def view(self, fields: dict)->str:
        pass

    def edit(self, fields: dict)->bool:
        pass

    def delete(self, fields: dict)->bool:
        pass

    @static
    def reqFields(self)->list:
        pass

    @static
    def optFields(self)->list:
        pass