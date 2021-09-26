import datetime
from dataclasses import dataclass

import self as self


@dataclass
class Contract:
    """The very same as smart-contract"""
    # remind and expire funs for event_loop


expires: datetime.date
price_rub: int

    def __init__(self, contract_id, expires, *parties):
        self.id = contract_id
        self.parties = [parties]

    def remind(self, warning=False):
        if warning:
            return f"{self.__class__} {self.id} почти расторгнут!!!"
        else:
            return f"срок действия договора {self.id} скоро истечёт."


    def __del__(self):
        #expires or break or occurance
        #where is Solidity????!!!!
        pass


@dataclass()
class Hypothec(Contract):

    def withdrawal(self):
        #Выселяем
        pass


@dataclass
class User:
    #licencies, passports, DNK signature
    proof: str
    tg_id:str
    contracts: Contract()

    def proof(self):
        pass

    def view_contract(self):
        return self.contracts


@dataclass
class Representer(User):
    companie_name: str
    contracts = ()


class Bank(Representer):

    def __init__(self):
        super().__init__()

    def resell(self, contract, acquirer: __init__):
        acquirer.contract.append(contract)
        self.contracts.remove(contract)


@dataclass()
class InsuranceCompanie(Representer):

    slogan = "/n Мы стали надёжней!!!"

    def __init__(self, companie):
        super(InsuranceCompanie, self).__init__()
        ads = self.companie_name + self.slogan

    def wall_customers(self):
        #всем кастомерам предложение от компаний
        pass