class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        current_bracket_index = 0
        last_bracket_upper = 0
        total_tax = 0

        while income > 0:
            taxable_money_band = brackets[current_bracket_index][0] - last_bracket_upper
            taxable_income = income if taxable_money_band > income else taxable_money_band
            total_tax += (brackets[current_bracket_index][1] / 100) * taxable_income
            last_bracket_upper = brackets[current_bracket_index][0]
            current_bracket_index += 1
            income -= taxable_income

        return total_tax