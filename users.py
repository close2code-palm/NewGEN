from dataclasses import dataclass


@dataclass
class Contract:
    """The very same as smart-contract"""
    # remind and expire funs for event_loop


    def __init__(self, contract_id, expires, *parties):
        self.id = contract_id
        self.parties = [parties]

    def remind(self):
        pass

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
    companie: str
    contracts = []


class Bank:
    pass


@dataclass
class Bank(Representer):

    def __init__(self):
        super().__init__()

    def resell(self, contract, acquirer: Bank):
        acquirer.contract


@dataclass()
class InsuranceCompanie(Representer):

    slogan = "/n Мы стали надёжней!!!"

    def __init__(self, companie):
        super(InsuranceCompanie, self).__init__()
        ads = self.companie + self.slogan

    def wall_customers(self):
        #всем кастомерам предложение от компаний
        pass