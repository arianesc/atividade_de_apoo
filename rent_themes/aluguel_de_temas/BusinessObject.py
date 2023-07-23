from datetime import datetime

class BusinessObject:
    def discountCalc(data):
        data = datetime.strptime(data, '%Y-%m-%d')
        weekday = data.weekday()
        if weekday < 4:
            return 10
        return 0

