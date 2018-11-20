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

    # Edit will need cnum, snum and dept (like all other commands)
    # Any other fields specified that aren't above(e.g. room, instructor, ect.) will replace what is already in the section
    # You can not change cnum and dept, but if you want to change snum use key "snumNew" as a replacement
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