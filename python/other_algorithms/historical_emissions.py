class Company:
    TAX_GTC = 10
    def __init__(self, name : str, net_profit : int, previous_emissions : int):
        self.name = name
        self.net_profit = net_profit
        self.previous_emissions = previous_emissions

    @staticmethod
    def init_new_company(name : str):
        return Company(name, 0, 0)
    @staticmethod
    def init_historical_company(name : str, previous_emissions):
        return Company(name, 0, previous_emissions)

    @staticmethod
    def change_carbon_tax(new_tax):
        Company.TAX_GTC = new_tax

    # returns the net profit/loss
    def emit(self, emission_quantity : int) -> int:
        amount_taxed = Company.TAX_GTC * emission_quantity
        credit = Company.TAX_GTC * self.previous_emissions
        self.net_profit += credit - amount_taxed
        self.previous_emissions = emission_quantity
        return self.net_profit
def average(lst : list[int]):
    return sum(lst) // len(lst)
if __name__ == '__main__':
    previous_emission = 10
    companies = []
    abc = Company.init_historical_company('abc', previous_emission)
    xyz = Company.init_new_company('xyz')
    companies.append(abc)
    companies.append(xyz)

    emission_history = [15, 9, 13, 9]
    for c in companies:
        for e in emission_history:
            res = c.emit(e)
            form__ = 'gains' if res >= 0 else 'loses'
            print(f'{c.name} {form__} {res} from emitting {e} GtC')
    print(f'average emission: {average(emission_history + [previous_emission])}')




