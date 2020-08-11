import datetime
import re

BSMonths = [
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],  #2000
    [ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],  #2001
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
	[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],  #2071
	[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],  #2072
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],  #2073
	[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
	[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
	[ 31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
	[ 30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],  #2090
	[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
	[ 30, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30 ],
	[ 30, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
	[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
	[ 31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31 ],
	[ 31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30 ]   #2099
]


class DateBS:
    """
    Assist in conversion of Date in BS to AD and vice versa
    """
    year: int = 2000
    month: int = 9
    day: int = 17

    def __init__(self,year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def from_string(datestring: str):
        """
        create the DateBS object from string

        :param datestring: BS date in string
        :type datestring: str

        :returns: DateBS object
        :rtype: DateBS
        """
        date = re.findall("(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)", datestring)
        return DateBS(int(date[0][0]), int(date[0][1]), int(date[0][2]))

    @staticmethod
    def from_AD(date: datetime.datetime):
        """
        create DateBS from AD

        :param date: python datetime object in AD
        :rtype date: datetime

        :returns: date in BS
        :rtype: DateBS
        """
        starting_date_AD = datetime.datetime(year=1944, month=1, day=1)
        diff_day = (date - starting_date_AD).days
        starting_date_BS = DateBS(2000,9,17)
        return starting_date_BS.add(day=diff_day)

    def __str__(self):
        """
        converts to DateBS to string
        """
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)

    def day_of_year(self) -> int:
        """
        gets the day of the year

        :returns: day of the year in integer
        :rtype: int
        """
        months = DateBS.months_in_year(self.year)
        return sum(months[0:self.month-1]) + self.day

    @staticmethod
    def days_in_year(year: int) -> int:
        """
        gets the no of day in a year

        :returns: no of day in a year
        :rtype: int
        """
        return sum(DateBS.months_in_year(year))

    def day_since(self, date : any = None )  -> int:
        """
        returns no of day since the date

        :param date: date in BS

        :returns: int
        :rtype: int
        """
        if (date == None):
            date = DateBS(2000,9,17)
        days: int = 0 
        for year in range(date.year, self.year):
            day_in_year = DateBS.days_in_year(year)
            days += day_in_year
        days = days + self.day_of_year() - date.day_of_year()
        return days

    def add(self, day:int, month:int = 0, year:int = 0 ):
        """
        add date time to dateBS

        :param day: day in int
        :rtype day: int
        :param month: month in int
        :rtype month: int
        :param year: year in int
        :rtype year: int

        :returns: datebs
        :rtype: DateBS
        """
        self.month += month
        self.year += (year + int(self.month / 12))
        self.month = int(self.month%12)
        diff: int = day
        while (diff > 0):
            #import ipdb;ipdb.set_trace()
            days_in_month: int = DateBS.days_in_month(self.year, self.month)
            days_left_in_month: int = days_in_month - self.day + 1
            if (diff >= days_left_in_month):
                if (self.month == 12):
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
                self.day = 1
                diff -= days_left_in_month
            else:
                self.day += diff
                diff -= diff
        return self

    def to_AD(self):
        """
        change the date to AD

        :returns: datetime in AD
        :rtype: datetime
        """
        starting_date_AD = datetime.datetime(year=1944, month=1, day=1)
        day_since = self.day_since()
        return starting_date_AD + datetime.timedelta(days=day_since)

    @staticmethod
    def months_in_year(year: int):
        """
        get no of months in year

        :param year: year

        :return: no of months in year
        :rtype: int
        """
        year_index = year - 2000
        return BSMonths[year_index]

    @staticmethod
    def days_in_month(year:int, month:int):
        """
        get days of the months

        :param year: year
        :type year: int
        :param month: months
        :type month: int

        :returns: days in the month
        :rtype: int
        """
        return DateBS.months_in_year(year)[month-1]

    def month_in_string(self):
        """
        converts month in string

        :returns: month in string
        :rtype: str
        """
        monthBS = [ "Baishakh",
                    "Jestha",
                    "Ashadh",
                    "Shrawan",
                    "Bhadra",
                    "Ashwin",
                    "Kartik",
                    "Mangsir",
                    "Poush",
                    "Magh",
                    "Falgun",
                    "Chaitra"
        ]
        return monthBS[self.month-1]

    def month_in_string_nepali(self):
        """
        convertes month in string nepali

        :returns: month in nepali stirng
        :rtype: str
        """
        monthBS = [ "वैशाख",
                    "ज्येष्ठ",
                    "असार",
                    "साउन",
                    "भदौ",
                    "असोज",
                    "कात्तिक",
                    "मंसिर",
                    "पुष",
                    "माघ",
                    "फागुन",
                    "चैत"
        ]
        return monthBS[self.month-1]

    def get_financial_year(self):
        """
        gets the financial year

        :returns: financial year in string
        :rtype: str 
        """
        if self.month > 3:
            return str(self.year) + "/" + str(self.year % 100+1)
        else:
            return str(self.year-1) + "/" + str(self.year % 100)
