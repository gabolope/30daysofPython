print('\n### Level 1 ###')
# Exercises: Level 1
# 1 Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
import statistics

class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers
    def describe(self):
        mn = min(self.numbers)
        mx = max(self.numbers)
        me = statistics.mean(self.numbers)
        md = statistics.median(self.numbers)
        sd = statistics.stdev(self.numbers)
        mo = statistics.mode(self.numbers)
        return {
            'Min': mn,
            'Max': mx,
            'Mean': me,
            'Median': md,
            'Standard deviation': sd,
            'Mode': mo
        }
        

nums = list(range(10))

st = Statistics(nums)
print(st.describe())

print('\n### Level 2 ###')
# Exercises: Level 2
# 2 Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
        def __init__ (self, firstname, lastname, incomes, expenses):
            self.firstname = firstname
            self.lastname = lastname
            self.incomes = incomes
            self.expenses = expenses

        def account_info(self):
            return self.firstname, self.lastname
        
        def total_income(self): 
            self.income_total = 0
            for income in self.incomes.items():
                self.income_total += income[1] # ESTO ESTA MAL. NO ES NECESARIO GUARDAR LOS TOTALES COMO ATRIBUTOS
            return self.income_total
        
        def total_expense(self):
            return sum(self.expenses.values()) # FORMA MAS EFICIENTE DE HACERLO
        
        def add_income(self, new_income_name, new_income_value):
            self.incomes[new_income_name] = new_income_value
            return self.incomes
        
        def add_expense(self, new_expense_name, new_expense_value):
            self.expenses[new_expense_name] = new_expense_value
            return self.expenses
        
        def account_balance(self):
            income_total = sum(self.incomes.values())
            expense_total = sum(self.expenses.values())
            return income_total - expense_total
        

user_incomes = {'sueldo': 600,
                'changas': 200,
                'inversiones': 200
                }

user_expenses = {'alquiler': 200,
                'seguro': 100,
                'servicios': 100,
                'obra social': 100
                }

user_account = PersonAccount('Gabo', 'Lope', user_incomes, user_expenses)

print('Usuario:', user_account.account_info())
print('Entradas totales:', user_account.total_income())
print('Gastos totales:', user_account.total_expense())
print('Balance de la cuenta:', user_account.account_balance())
print('Entradas actualizados:', user_account.add_income('Pintar casas', 400))
print('Gastos actualizados:', user_account.add_expense('cuota social', 100))
print('Balance de la cuenta:', user_account.account_balance())