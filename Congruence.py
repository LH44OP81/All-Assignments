class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.day = day

        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def calculate_weekday(self):
        q = self.day
        m = self.month
        Y = self.year
        K = Y % 100
        J = Y // 100

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        weekday_names = [
            "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
        ]
        return weekday_names[h]

date = DateCalculator(1589, 9, 15)
print("September 15, 1589 was a", date.calculate_weekday())
