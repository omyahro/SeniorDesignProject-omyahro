from re import T
from typing import List
from cis301.phonebill.abstract_phonebill import AbstractPhoneBill
class PhoneBill(AbstractPhoneBill):
     def get_customer(self) -> str:
         pass
     def add_phonecall(self, phonecall):
         pass
     def get_phonecalls(self) -> List[T]:
         pass
