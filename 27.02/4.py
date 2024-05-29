transactions = {}


def get_transactions(t):
    if t == 'print_it':
        for transaction_type, data in transactions.items():
            print(f"{data['count']} {transaction_type} {data['total_amount']}")
    else:
        phone_number, transaction_info = t.split('-')
        transaction_type, amount = transaction_info.split(':')
        amount = int(amount)

        if transaction_type in transactions:
            transactions[transaction_type]['count'] += 1
            transactions[transaction_type]['total_amount'] += amount
        else:
            transactions[transaction_type] = {'count': 1, 'total_amount': amount}


# Example usage
get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')
