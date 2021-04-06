import sys
import getopt
import json
import cryptocompare

default_currency = 'USD'

def help():
    print('cc.py -s <source> -a <amount> -d <destination> -h <help> -l <list>')
    print('Example Usage: python3 cc.py -s BTC -a 1.01 -d USD')
    print('A sample of supported currencies are listed below.')
    print('To see them all, use the -l or --list flag.')
    print('[NANO, BTC, ETH, XRP, USD, GBP]')

def main(source, amount, destination):
    rate_at_amount = None
    if (source and amount and destination):
        rate = cryptocompare.get_price(source, currency=destination)
        rate_at_amount = float(rate[source][destination]) * float(amount)
    elif (source and amount):
        rate = cryptocompare.get_price(source, currency=default_currency)
        rate_at_amount = float(rate[source][destination]) * float(amount)
    print(rate_at_amount)

if __name__ == "__main__":

    f = open('super_secret.json',)
    data = json.load(f)
    secret_key = data['secret_key']
    cryptocompare.cryptocompare._set_api_key_parameter("secret_key")

    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hls:a:d:",["help","list","source=","amount=","destination=",])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    source = None
    amount = None
    destination = None
    list_of_currencies = cryptocompare.get_coin_list(format=True) + ['USD', 'GBP', 'EUR']
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        if opt == '-l':
            print('All supported currencies are:')
            print(list_of_currencies)
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-a", "--amount"):
            amount = arg
        elif opt in ("-d", "--destination"):
             destination = arg

    valid_source = source in list_of_currencies
    valid_amount = amount.isdigit()
    valid_destination = (destination is None) or (destination in list_of_currencies)
    if (valid_source and valid_amount and valid_destination):
        main(source, amount, destination)
    else:
        print('Your command line arguments are not valid.')
        help()