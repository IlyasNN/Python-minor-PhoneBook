from datetime import datetime, date, timedelta

from Other import cls
from Show import showBirthday


def birthdayList(phoneBook):
    cls()
    searchBook = phoneBook.copy()

    for key in list(searchBook):
        if searchBook[key].birthday is None:
            del searchBook[key]
        else:
            today = datetime.now().date()
            soon = datetime.now() + timedelta(days=31)
            soon = soon.date()
            day = searchBook[key].birthday.day
            month = searchBook[key].birthday.month
            year = today.year
            birthday = date(year, month, day)

            if not (today < birthday and birthday < soon):
                del searchBook[key]

    showBirthday(searchBook)

    print('\tDon\'t forget to congratulate them!!!\n')
