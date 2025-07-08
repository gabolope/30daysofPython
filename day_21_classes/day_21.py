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
        def total_income(self):
            t_i = 0
            for i in self.incomes.items():
                t_i += i[1]
                return t_i
        def account_info():
            pass
        def total_expense():
            pass
        def add_income():
            pass
        def add_expense():
            pass
        def account_balance():
            pass

user_incomes = {'sueldo': 600,
                'changas': 200,
                'inversiones': 100
                }

user_expenses = {'alquiler': 200,
                'seguro': 50,
                'servicios': 100,
                'obra social': 50
                }

user_account = PersonAccount('Gabo', 'Lope', user_incomes, user_expenses)

print(user_account.total_income())