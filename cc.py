import sys
import getopt
import cryptocompare

def main(source, amount, destination):
    rate = cryptocompare.get_price(source, currency=destination, full=True)
    rate_at_amount = rate * amount
    print(rate_at_amount)


if __name__ == "__main__":

    cryptocompare.cryptocompare._set_api_key_parameter("KEY_HERE")

    try:
      opts, args = getopt.getopt(argv,"hs:a:d:",["source=","destination="])
    except getopt.GetoptError:
      print 'cc.py -s <source> -a <amount> -d <destination>'
      print 'See supported currencies in currencies.json'
      sys.exit(2)

    source = None
    amount = None
    destination = None
    for opt, arg in opts:
        if opt == '-h':
            print 'cc.py -s <sourceCurrency> -a <amount> -d <destinationCurrency>'
            print 'See supported currencies in currencies.json'
            sys.exit()
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-a", "--amount"):
            amount = arg
        elif opt in ("-d", "--destination"):
             destination = arg

    main(souce, amount, destination)