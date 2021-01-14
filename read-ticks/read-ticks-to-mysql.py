import ccxt 
import pprint
import mysql.connector

from termcolor import cprint , colored
from pyfiglet import figlet_format,Figlet
cprint(figlet_format('bitmex', font='starwars'),'blue', attrs=['bold'])

exchange = ccxt.bitmex({
    'enableRateLimit': True
})

markets = exchange.load_markets()
symbol = 'XTZUSDTH21'
market = exchange.market(symbol)

# the following calculation depends on contract specifications
num_contracts = 1

while True:
    try:
        ticker = exchange.fetch_ticker(symbol)
        cprint('TICKS','blue', attrs=['blink'])
        print('---------------------------------------------------------------')
        pprint.pprint(ticker)

        #mysql inserting tick as json 
        try:
                    
            mydb = mysql.connector.connect(
                host="your_host",
                user="your_user",
                password="your_pwd",
                database="your_db"
            )
            mycursor = mydb.cursor()

            sql = "INSERT INTO bitmex_XTZUSDTH21 (data) VALUES (%s)"
            val = (ticker)
            mycursor.execute(sql,val)

            mydb.commit()
        except:
            pass

        last_price = ticker['last']
        print("Last Price: ",last_price)

        print(exchange.iso8601(exchange.milliseconds()))
        print('---------------------------------------------------------------\n')
    except Exception as e:
        pass
