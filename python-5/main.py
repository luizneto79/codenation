"""
Codenation - Acelera DEV - Desafio 1
Author: Luiz Marques Neto
Date: 2020-05-17
"""


from datetime import datetime, timedelta
from operator import itemgetter


FIXED_RATE = 0.36
DAY_TAX = 0.09


def get_index_source_bill(bill, record):

    resp = None

    for index, item in enumerate(bill):
        if item['source'] == record['source']:
            resp = index
            break

    return resp


def calculate_call(record):

    period_start = datetime.fromtimestamp(record.get('start'))
    period_end = datetime.fromtimestamp(record.get('end'))
    daytime_start = datetime.strptime('06:00:00', '%H:%M:%S')
    daytime_end = datetime.strptime('22:00:00', '%H:%M:%S')
    total = FIXED_RATE

    while (period_start < period_end
           and (period_end - period_start).total_seconds() >= 60):

        if daytime_start.time() <= period_start.time() <= daytime_end.time():
            total = total + DAY_TAX
        else:
            pass

        period_start = period_start + timedelta(seconds=60)

    return round(total, 2)


def order_by(registers=[], key='', reverse=False):
    return sorted(registers, key=itemgetter(key), reverse=reverse)


def classify_by_phone_number(records):

    bill = []

    if records:
        for record in records:
            total = calculate_call(record)
            index = get_index_source_bill(bill, record)

            if index is not None:
                bill[index]['total'] += total
                bill[index]['total'] = round(bill[index]['total'], 2)
            else:
                bill.append({'source': record['source'], 'total': total})

        return order_by(bill, 'total', reverse=True)
