"""
1 Задача
Формат ввода
В первой строке содержатся 6 целых чисел year1, month1, day1, hour1, min1, sec1 (1≤year1≤9999, 1≤month1≤12, 1≤day1≤31, 0≤hour1≤23, 0≤min1≤59, 0≤sec1≤59)— дата начала существования ящеров.
Во второй строке содержатся 6 целых чисел year2, month2, day2, hour2, min2, sec2 (1≤year2≤9999, 1≤month2≤12, 1≤day2≤31, 0≤hour2≤23, 0≤min2≤59, 0≤sec2≤59)— дата окончания существования ящеров.
Гарантируется, что дата начала меньше, чем дата конца.
Формат вывода
В первой и единственной строке выведите 2 числа: количество дней, сколько существовали ящеры, а также количество секунд в неполном дне.

"""


class Raptors:
    DAYS_IN_YEAR = 365
    MONTHS_IN_YEAR = 12
    DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    HOURS_IN_DAY = 24
    MINUTES_IN_HOURS = 60
    SECONDS_IN_MINUTE = 60

    @classmethod
    def get_seconds_in_hour(cls, hours):
        return hours * cls.MINUTES_IN_HOURS * cls.SECONDS_IN_MINUTE

    @classmethod
    def get_seconds_in_days(cls, days):
        return days * cls.get_seconds_in_hour(cls.HOURS_IN_DAY)

    @classmethod
    def get_seconds_in_year(cls, years):
        return years * cls.get_seconds_in_days(cls.DAYS_IN_YEAR)

    @classmethod
    def get_days_in_months(cls, start, end):
        result = 0
        if start < end:
            for days in cls.DAYS_IN_MONTH[start+1: end]:
                result += days
        else:
            for days in cls.DAYS_IN_MONTH[(end+1):cls.MONTHS_IN_YEAR]:
                result += days
            for days in cls.DAYS_IN_MONTH[0:start]:
                result += days
        return result

    @classmethod
    def run(cls):
        start_date = list(map(lambda number: int(number), input().split(' ')))
        end_date = list(map(lambda number: int(number), input().split(' ')))


        #years
        if start_date[1] < end_date[1]:
            years = end_date[0] - start_date[0]
            seconds = cls.get_seconds_in_year(years)
        else:
            years = end_date[0] - start_date[0] - 1
            seconds = cls.get_seconds_in_year(years)

        #months and days seconds
        days_in_months = cls.get_days_in_months(start_date[1]-1, end_date[1]-1)
        seconds += cls.get_seconds_in_days(days_in_months)

        #days in seconds
        seconds += cls.get_seconds_in_days(cls.DAYS_IN_MONTH[start_date[1]-1]-start_date[2])
        seconds += cls.get_seconds_in_days(end_date[2]-1)

        #hours
        if start_date[3] < end_date[3]:
            hours = cls.HOURS_IN_DAY - start_date[3]
            seconds += cls.get_seconds_in_hour(hours)
        else:
            hours = cls.HOURS_IN_DAY - start_date[3] + end_date[3]
            # if start_date[4] > end_date[4] or start_date[5] < end_date[5]:
            #     hours -= 1
            seconds += cls.get_seconds_in_hour(hours)

        seconds += cls.get_seconds_in_hour(end_date[3])

        #mitutes
        if start_date[4] < end_date[4]:
            minutes = end_date[4] - start_date[4]
            seconds += minutes * cls.SECONDS_IN_MINUTE
        else:
            minutes = (cls.MINUTES_IN_HOURS - start_date[4]) + end_date[4]
            seconds += minutes * cls.SECONDS_IN_MINUTE
        if start_date[5] < end_date[5]:
            seconds += (end_date[5] - start_date[5])
        else:
            seconds += ((cls.SECONDS_IN_MINUTE - 1 - start_date[5]) + end_date[5])
            # seconds += end_date[5]
        result_days = seconds // (cls.HOURS_IN_DAY * cls.MINUTES_IN_HOURS * cls.SECONDS_IN_MINUTE)
        result_seconds = seconds % result_days

        print(result_days, result_seconds)





"""
Задача 2. 
Два друга A и B постоянно играют в коллекционную карточную игру (ККИ), поэтому у каждого игрока скопилась довольно большая коллекция карт.
Каждая карта в данной игре задаётся целым числом (одинаковые карты — одинаковыми числами, разные карты — разными).
Таким образом коллекцию можно представить как неупорядоченный набор целых чисел (с возможными повторениями).
После каждого изменения коллекций друзья вычисляют показатель разнообразия следующим образом:
•	A и B выкладывают на стол все карты из своей коллекции в два раздельных ряда;
•	Далее друзья итеративно делают следующее:
1.	Если среди лежащих на столе карт игрока A есть такая же карта, как и среди лежащих карт игрока B — каждый игрок убирает данную карту со стола;
2.	Если таковых совпадений нет — процесс заканчивается.
•	Разнообразием коллекций друзья называют суммарное количество оставшихся карт на столе.
Обратите внимание: друзья убирают карты только со стола, карты не удаляются из коллекций при вычислении разнообразия.
Даны начальные состояния коллекций игроков, а также Q изменений их коллекций. После каждого изменения необходимо вычислить разнообразие коллекций друзей.
"""


class Collections:
    ACollection = []
    BCollection = []
    ADiff = []
    BDiff = []
    QResult = []

    @classmethod
    def change_collection(cls, collection, oper, val):
        if oper == -1:
            collection.remove(val)
        else:
            collection.append(val)

    @classmethod
    def compare_collections(cls, collection1, collection2):
        if len(collection1) > len(collection2):
            collectionI = collection1
            collectionJ = collection2
        else:
            collectionI = collection2
            collectionJ = collection1
        i = 0
        while i < len(collectionI):
            j = 0
            while j < len(collectionJ):
                if i >= len(collectionI):
                    break
                if collectionI[i] == collectionJ[j]:
                    collectionI.remove(collectionI[i])
                    collectionJ.remove(collectionJ[j])
                    j = 0
                else:
                    j += 1
            i += 1
        cls.QResult.append(len(collectionI) + len(collectionJ))

    @classmethod
    def run(cls):
        ACount, BCount, QCount = list(map(lambda number: int(number), input().split(' ')))
        cls.ACollection = list(map(lambda number: int(number), input().split(' ')))
        cls.BCollection = list(map(lambda number: int(number), input().split(' ')))

        for i in range(0, QCount):
            oper, player, index = input().split(' ')
            oper = int(oper)
            index = int(index)

            if player == 'A':
                cls.change_collection(cls.ACollection, oper, index)
            else:
                cls.change_collection(cls.BCollection, oper, index)
            cls.ADiff = cls.ACollection[:]
            cls.BDiff = cls.BCollection[:]
            cls.compare_collections(cls.ADiff, cls.BDiff)
        print(cls.QResult)


"""
Задача 4.
Межпланетная организация имеет иерархическую древовидную структуру:
•	Корнем иерархии является генеральный директор;
•	У каждого сотрудника 0 или более непосредственных подчиненных;
•	Каждый сотрудник, кроме генерального директора, является непосредственным подчиненным ровно одному сотруднику.
Каждый сотрудник, кроме генерального директора, говорит либо на языке A, либо на языке B. Директор говорит на двух языках для управления всей организацией.
Структура всей организации хранится в текстовом документе. Каждый сотрудник представлен уникальным идентификатором - целым числом от 0 до N включительно, где 0 - идентификатор генерального директора.
Каждый сотрудник представлен в документе ровно два раза. Между первым и вторым вхождением идентификатора сотрудника в аналогичном формате представлены все его подчиненные.
Если у сотрудника нет подчиненных, то два его идентификатора расположены один за другим.
Например, если
•	генеральный директор имеет в прямом подчинении сотрудника 1;
•	сотрудник 1 имеет в прямом подчинении сотрудника 2;
•	сотрудник 2 имеет в прямом подчинении сотрудников 3 и 4;
то документ будет представлен в виде строки:
0123344210
"""

class Employee:
    stack = []
    bariers = []

    @classmethod
    def run(cls):
        employee_count = int(input())
        langs = input().split(' ')
        hierarchy = list(map(lambda number: int(number), input().split(' ')))

        for item in hierarchy:
            if not cls.stack:
                cls.stack.append(item)
                cls.bariers.append(0)
            else:
                if item != cls.stack[-1]:

                    if langs[item-1] == langs[cls.stack[-1]-1] or cls.stack[-1] == 0:
                        cls.bariers.append(0)
                    else:
                        i = len(cls.stack) - 1
                        bar_count = 0
                        while i > 0:
                            if langs[item-1] != langs[cls.bariers[i]-1]:
                                bar_count += 1
                            else:
                                break
                            i -= 1
                        cls.bariers.append(cls.bariers[-1]+bar_count)
                    cls.stack.append(item)
                    if langs[item - 1] == 0:
                        continue
                else:
                    cls.stack.pop(-1)
        print(cls.bariers[1:])


if __name__ == '__main__':
    Raptors.run()
    # Collections.run()
    # Employee.run()
