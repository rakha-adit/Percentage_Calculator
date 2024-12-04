class Percentage:
    def __init__(self):
        # self.number_1 = number_1
        # self.number_2 = number_2
        # self.operation = operation
        pass


    def what_percent_of(self, value, divisor):
        '''
        Function to calculate what percentage one number is of another.

        Inputs:
            - value : Number will find the percentage (int, float)
            - divisor : Divisor number (int, float)
        '''
        return value / divisor * 100
    
    def percentage_change(self, new_value, old_value):
        '''
        Function to calculate the percentage increase or decrease between two values.
        
        Inputs:
            - new_value : New Value Number (int, float)
            - old_value : Old Value Number (int, float)
        '''
        return ((new_value - old_value) / old_value) * 100
    
    def reverse_percentage(self, final_value, percent_change):
        '''
        Function to calculate the original value before a percentage increase or decrease.
        
        Inputs: 
            - final_value : Final Value Number (int, float)
            - percent_change : Percentage Change Number (float) 
        '''
        return final_value / (1 + (percent_change / 100))
    
    def percent_number(self, number, percent_change):
        '''
        Function to calculate a certain percentage of a given number.
        
        Inputs:
            - Number: Number will find percentage (int, float)
            - percent_change: Percentage Change Number (float)
        '''
        return number * (percent_change / 100)
    
    def compound_percentage_growth(self, initial_value, rate, periods):
        '''
        Function to calculate the growth or decay over multiple periods.

        Inputs:
            - initial_value: Initial Value Number (int, float)
            - rate: Percentage growth (float)
            - periods: Time duration (year) (int, float)
        '''
        return initial_value * (1 + rate/100) ** periods
    
    def weighted_percentage(self, value, weight):
        pass
    
    def percentage_distribution(self, part, total):
        '''Function to calculate the percentage distribution among multiple parts.'''
        return part / total * 100
    
    def percentage_difference(self, value_1, value_2):
        '''Function to calculate the absolute difference in percentages between two values.'''
        return abs(value_1-value_2) / ((value_1 + value_2) / 2) * 100