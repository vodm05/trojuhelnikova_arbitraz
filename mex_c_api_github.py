import re
from sqlite3 import Timestamp
import requests
import hashlib
import hmac
import datetime
import decimal
import mexc_spot_v3
import openpyxl
from datetime import datetime
import time

hosts = "https://api.mexc.com"

base_url = "https://api.mexc.com/api/v3/exchangeInfo?symbol="


account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
print(account_information)

"""place an order"""
trade = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)

"""params = {
    "symbol": "SOLUSDC",
    "side": "SELL",
    "type": "LIMIT_MAKER",
    "quantity": "5",
    "price": "3.1777",
    # 'quoteOrderQty': 5.1
    # "recvWindow": 60000
}
response = trade.post_order(params)
print(response)"""



"""capital = mexc_spot_v3.mexc_capital(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
response = capital.get_coinlist()
print(response)"""

"""url = base_url + "TRXBTC"
response = requests.get(url)
data = response.json()
symbols = data.get("symbols", [])
print(symbols)"""


url = """https://api.mexc.com/api/v3/exchangeInfo?symbols=BTCUSDC"""
response = requests.get(url)
data = response.json()
"""print(data)
for symbol in data['symbols']:
    if 'Market' in symbol['orderTypes']:
        print(symbol)
"""



data = mexc_spot_v3.mexc_market(mexc_hosts=hosts).get_defaultSymbols()

"""for x in data["data"]:
    if "ADABTC" in x:
        print(x)"""


list_men = ["BTCUSDC", "ADABTC", "ADAUSDC", "ETHBTC", "ETHUSDC", "TRXBTC", "TRXUSDC", "SOLBTC", "SOLUSDC", "LTCUSDC", "XRPBTC", "LTCBTC"]
#"LTCBTC" se může přidat

for x in list_men:
    url = """https://api.mexc.com/api/v3/exchangeInfo?symbols="""
    response = requests.get(url+x)
    data = response.json()
    #print(f"{x} jeho stav je {data}")
while True:
    """list_zaokrouhleni = []
    for symbol in list_men:
        url = base_url + symbol
        
        # Zaslání požadavku GET
        response = requests.get(url)

        # Zpracování odpovědi
        if response.status_code == 200:
            data = response.json()
            symbols = data.get('symbols', [])
            
            if symbols:
                symbol_info = symbols[0]
                symbol = symbol_info.get('symbol')
                baseAsset = symbol_info.get('baseAsset')
                quoteAsset = symbol_info.get('quoteAsset')
                baseAssetPrecision = symbol_info.get('baseAssetPrecision')
                serverTime = data.get('serverTime', 0) / 1000  # Převedení na sekundy
                serverTime = datetime.fromtimestamp(serverTime)
                formatted_time = serverTime.strftime('%S.%M.%H %d.%m.%Y')
                
                zaokrouhleni = {
                    'symbol': symbol,
                    'baseAsset': baseAsset,
                    'quoteAsset': quoteAsset,
                    'baseAssetPrecision': baseAssetPrecision,
                    'serverTime': formatted_time
                }
                
                list_zaokrouhleni.append(zaokrouhleni)"""
    list_zaokrouhleni = [
    {'symbol': 'BTCUSDC', 'baseAsset': 'BTC', 'quoteAsset': 'USDC', 'baseAssetPrecision': 6, 'serverTime': '30.01.23 08.06.2023'},
    {'symbol': 'ADABTC', 'baseAsset': 'ADA', 'quoteAsset': 'BTC', 'baseAssetPrecision': 3, 'serverTime': '30.01.23 08.06.2023'},
    {'symbol': 'ADAUSDC', 'baseAsset': 'ADA', 'quoteAsset': 'USDC', 'baseAssetPrecision': 2, 'serverTime': '31.01.23 08.06.2023'},
    {'symbol': 'ETHBTC', 'baseAsset': 'ETH', 'quoteAsset': 'BTC', 'baseAssetPrecision': 3, 'serverTime': '31.01.23 08.06.2023'},
    {'symbol': 'ETHUSDC', 'baseAsset': 'ETH', 'quoteAsset': 'USDC', 'baseAssetPrecision': 5, 'serverTime': '31.01.23 08.06.2023'},
    {'symbol': 'TRXBTC', 'baseAsset': 'TRX', 'quoteAsset': 'BTC', 'baseAssetPrecision': 3, 'serverTime': '32.01.23 08.06.2023'},
    {'symbol': 'TRXUSDC', 'baseAsset': 'TRX', 'quoteAsset': 'USDC', 'baseAssetPrecision': 2, 'serverTime': '32.01.23 08.06.2023'},
    {'symbol': 'SOLBTC', 'baseAsset': 'SOL', 'quoteAsset': 'BTC', 'baseAssetPrecision': 2, 'serverTime': '32.01.23 08.06.2023'},
    {'symbol': 'SOLUSDC', 'baseAsset': 'SOL', 'quoteAsset': 'USDC', 'baseAssetPrecision': 2, 'serverTime': '33.01.23 08.06.2023'},
    {'symbol': 'LTCUSDC', 'baseAsset': 'LTC', 'quoteAsset': 'USDC', 'baseAssetPrecision': 2, 'serverTime': '33.01.23 08.06.2023'},
    {'symbol': 'XRPBTC', 'baseAsset': 'XRP', 'quoteAsset': 'BTC', 'baseAssetPrecision': 2, 'serverTime': '34.01.23 08.06.2023'},
    {'symbol': 'LTCBTC', 'baseAsset': 'LTC', 'quoteAsset': 'BTC', 'baseAssetPrecision': 3, 'serverTime': '34.01.23 08.06.2023'}]
    
    ceny = []        
    for symbol in list_men:
        url = 'https://api.mexc.com/api/v3/ticker/price'

        params = {'symbol': symbol}

        response = requests.get(url, params=params)

        data = response.json()

        ceny.append(data)

            
    zaklad_usdc = 30
    zaklad_usdc = decimal.Decimal(zaklad_usdc)

    prvni_smeny=[]
    for x in ceny:
        if "USDC" in x["symbol"]:
            prevod_1_zaokrouhleny = 0.0
            prevod = zaklad_usdc/decimal.Decimal(str(x["price"]))
            prevod = decimal.Decimal(str(prevod))
            for l in list_zaokrouhleni:
                if l["symbol"] == x["symbol"]:
                    baseAssetPrecision = int(l["baseAssetPrecision"])
                    if baseAssetPrecision == 1:
                        decimal_places = decimal.Decimal("1")
                        prevod_1_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                    else:
                        decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                        prevod_1_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
            kolik_se_prevedlo_USDC = float(x["price"])*float(prevod_1_zaokrouhleny)
            prvni_smena={
            "symbol": x["symbol"],
            "prevedeno_USDC" : kolik_se_prevedlo_USDC,
            "price_1": x["price"],
            "prevedeno_do": x["symbol"][:3],
            "prevod": prevod_1_zaokrouhleny
            }
            prvni_smeny.append(prvni_smena)



    druhe_smeny = []
    for x in prvni_smeny:
        prevadim_z = x["prevedeno_do"]
        for z in ceny:
            if "USDC" in z["symbol"]:
                continue
            if prevadim_z in z["symbol"][:3]:
                prevod = x["prevod"]*decimal.Decimal(z["price"])
                prevod = decimal.Decimal(str(prevod))
                prevod_2_zaokrouhleny = 0.0
                for l in list_zaokrouhleni:
                    if l["symbol"] == z["symbol"]:
                                baseAssetPrecision = int(l["baseAssetPrecision"])
                                if baseAssetPrecision == 1.0:
                                    decimal_places = decimal.Decimal("1")
                                    prevod_2_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                else:
                                    decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                    prevod_2_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                druha_smena={
                "puvodni_symbol": x["symbol"],
                "prevedeno_USDC": x["prevedeno_USDC"],
                "price_1": x["price_1"],
                "prevedeno_do_1": x["prevedeno_do"],
                "prevod_1": x["prevod"],
                "price_2": z["price"],
                "prevedeno_do_2": z["symbol"][3:],
                "zkratka_druhe": z["symbol"],
                "prevod_2": prevod_2_zaokrouhleny
                }
                druhe_smeny.append(druha_smena) 
            elif prevadim_z in z["symbol"][3:]:
                prevod = x["prevod"]/decimal.Decimal(z["price"])
                prevod = decimal.Decimal(str(prevod))
                prevod_2_zaokrouhleny = 0.0
                for l in list_zaokrouhleni:
                    if l["symbol"] == z["symbol"]:
                                baseAssetPrecision = int(l["baseAssetPrecision"])
                                if baseAssetPrecision == 1.0:
                                    decimal_places = decimal.Decimal("1")
                                    prevod_2_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                else:
                                    decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                    prevod_2_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                druha_smena={
                "puvodni_symbol": x["symbol"],
                "prevedeno_USDC": x["prevedeno_USDC"],
                "price_1": x["price_1"],
                "prevedeno_do_1": x["prevedeno_do"],
                "prevod_1": x["prevod"],
                "price_2": z["price"],
                "prevedeno_do_2": z["symbol"][:3],
                "zkratka_druhe": z["symbol"],
                "prevod_2": prevod_2_zaokrouhleny
                }
                druhe_smeny.append(druha_smena)


    treti_smeny = []
    for x in druhe_smeny:
        prevadim_z = x["prevedeno_do_2"]
        for z in ceny:
            if "USDC" in z["symbol"]:
                if prevadim_z in z["symbol"][:3]:
                    prevod = x["prevod_2"]*decimal.Decimal(z["price"])
                    prevod_3_zaokrouhleny = 0.0
                    for l in list_zaokrouhleni:
                        if l["symbol"] == z["symbol"]:
                                    baseAssetPrecision = int(l["baseAssetPrecision"])
                                    if baseAssetPrecision == 1.0:
                                        decimal_places = decimal.Decimal("1")
                                        prevod_3_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                    else:
                                        decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                        prevod_3_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                    treti_smena={
                    "puvodni_symbol": x["puvodni_symbol"],
                    "prevedeno_USDC": x["prevedeno_USDC"],
                    "price_1": x["price_1"],
                    "prevedeno_do_1": x["prevedeno_do_1"],
                    "prevod_1": x["prevod_1"],
                    "price_2": x["price_2"],
                    "prevedeno_do_2": x["prevedeno_do_2"],
                    "zkratka_druhe": x["zkratka_druhe"],
                    "prevod_2": x["prevod_2"],
                    "price_3": z["price"],
                    "zpet": prevod_3_zaokrouhleny,
                    "vynos_v_%": ((float(prevod_3_zaokrouhleny)-x["prevedeno_USDC"])/x["prevedeno_USDC"])*100
                    }
                    treti_smeny.append(treti_smena) 
                elif prevadim_z in z["symbol"][4:]:
                    prevod = x["prevod_2"]/decimal.Decimal(z["price"])
                    prevod_3_zaokrouhleny = 0.0
                    for l in list_zaokrouhleni:
                        if l["symbol"] == z["symbol"]:
                                    baseAssetPrecision = int(l["baseAssetPrecision"])
                                    if baseAssetPrecision == 1.0:
                                        decimal_places = decimal.Decimal("1")
                                        prevod_3_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                    else:
                                        decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                        prevod_3_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                    treti_smena={
                    "puvodni_symbol": x["puvodni_symbol"],
                    "prevedeno_USDC": x["prevedeno_USDC"],
                    "price_1": x["price_1"],
                    "prevedeno_do_1": x["prevedeno_do_1"],
                    "prevod_1": x["prevod_1"],
                    "price_2": x["price_2"],
                    "prevedeno_do_2": x["prevedeno_do_2"],
                    "zkratka_druhe": x["zkratka_druhe"],
                    "prevod_2": x["prevod_2"],
                    "price_3": z["price"],
                    "zpet": prevod_3_zaokrouhleny,
                    "vynos_v_%": ((float(prevod_3_zaokrouhleny)-x["prevedeno_USDC"])/x["prevedeno_USDC"])*100
                    }
                    treti_smeny.append(treti_smena)


    sestupne_hodnoty = sorted(treti_smeny, key=lambda x: x["vynos_v_%"], reverse=True)
    prvni_sestupna_hodnota = sestupne_hodnoty[:1]

                
    """existing_file = "mex_c_api_zaznamy.xlsx"

    # Načtení existujícího souboru
    workbook = openpyxl.load_workbook(existing_file)

    # Vybrání aktivního listu
    sheet = workbook.active

    # Získání aktuálního času
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Uložení dat splňujících podmínku
    for x in prvni_sestupna_hodnota:
        if x["vynos_v_%"] > 0.035:
            row_data = [
                x["puvodni_symbol"],
                x["prevedeno_USDC"],
                x["price_1"],
                x["prevedeno_do_1"],
                x["prevod_1"],
                x["price_2"],
                x["prevedeno_do_2"],
                x["zkratka_druhe"],
                x["prevod_2"],
                x["price_3"],
                x["zpet"],
                x["vynos_v_%"],
                current_time  # Přidání aktuálního času
            ]
            sheet.append(row_data)

    # Uložení souboru
    workbook.save(existing_file)
    workbook.close()"""
    
    for x in prvni_sestupna_hodnota:
        if x["vynos_v_%"] < 0.03:
             print("Hledám příležitost") 
        elif x["vynos_v_%"] > 0.03:

            for z in account_information["balances"]:
                    if z["asset"]== "USDC":
                        zustatek = z["free"]
                        zustatek = round(float(zustatek), 2)
                        prvni_sestupna_hodnota[-1].update({"USDC_zustatek": zustatek})
                        print(prvni_sestupna_hodnota)

            

            def prvni_smena(puvodni_symbol, prevedeno_do_1):
                while True:
                    try:
                        cena = 0.0        
                        url = 'https://api.mexc.com/api/v3/ticker/price'
                        params = {'symbol': puvodni_symbol}
                        response = requests.get(url, params=params)
                        data = response.json()
                        cena = data["price"]
                        
                        
                        prevod = zaklad_usdc/decimal.Decimal(str(cena))
                        prevod = decimal.Decimal(str(prevod))
                        for l in list_zaokrouhleni:
                            if l["symbol"] == puvodni_symbol:
                                baseAssetPrecision = int(l["baseAssetPrecision"])
                                if baseAssetPrecision == 1:
                                    decimal_places = decimal.Decimal("1")
                                    prevod_1_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                else:
                                    decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                    prevod_1_zaokrouhleny = prevod.quantize(decimal_places, rounding=decimal.ROUND_DOWN)


                        trade = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
                        params = {
                            "symbol": puvodni_symbol,
                            "side": "BUY",
                            "type": "LIMIT",
                            "quantity": str(prevod_1_zaokrouhleny),
                            "price": cena,
                            # 'quoteOrderQty': 5.1
                            # "recvWindow": 60000
                        }

                        response = trade.post_order(params)
                        
                        time.sleep(3)
                        # Pokud je v odpovědi uveden kód chyby, opakujte kód
                        if 'code' in response:
                            error_code = response['code']
                            if error_code == 30004 or 700003:
                                continue
                        account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
                        found_balance = False  # Příznak pro označení nalezení podmínky
                        for x in account_information['balances']:
                            if prevedeno_do_1 in x["asset"] and prevod_1_zaokrouhleny >= decimal.Decimal(str(x["free"])):
                                order = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
                                params = {
                                    "symbol": puvodni_symbol
                                }

                                response = order.delete_openorders(params)
                                found_balance = True  # Nalezení podmínky
                                break
                        if found_balance:
                            continue  # Pokračovat zpět na začátek bloku "try"¨

                        if 'code' in response:
                            error_code = response['code']
                            if error_code == 30004 or 700003:
                                continue
                        break
                    except Exception as e:
                        print("An unexpected error occurred:", str(e))
        
                        
                            
            prvni_smena(x["puvodni_symbol"], x["prevedeno_do_1"])

            print("prevedlo se z USDT")

            def druha_smena(prevedeno_do_2, zkratka_druhe, prevedeno_do_1, prevod_2):
                while True:
                    try:
                        cena = 0.0        
                        url = 'https://api.mexc.com/api/v3/ticker/price'
                        params = {'symbol': zkratka_druhe}
                        response = requests.get(url, params=params)
                        data = response.json()
                        cena = data["price"]
                        print(f"toto je cena: {cena}")
                        
                        
                        prevod_1 = 0.0
                        account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
                        print(account_information)
                        for balance in account_information['balances']:
                            if balance['asset'] == prevedeno_do_1:
                                balance_oficialni_1 = decimal.Decimal(str(balance['free']))
                                print(f"toto je stav účtu první směny {balance_oficialni_1}")
                                for l in list_zaokrouhleni:
                                    if l["symbol"] == zkratka_druhe:
                                        baseAssetPrecision = int(l["baseAssetPrecision"])
                                        if baseAssetPrecision == 1:
                                            decimal_places = decimal.Decimal("1")
                                            prevod_1 = balance_oficialni_1.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                        else:
                                            decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                            prevod_1 = balance_oficialni_1.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                        

                        prevod_2 = 0.0
                        print(f"toto je prevod 1: {prevod_1}")
                        if float(prevod_1) > 0.0:
                            if prevadim_z in zkratka_druhe[3:]:
                                prevod_2 = float(prevod_1)/float(cena)
                                for l in list_zaokrouhleni:
                                    prevod_2 = decimal.Decimal(str(prevod_2))
                                    if l["symbol"] == zkratka_druhe:
                                        baseAssetPrecision = int(l["baseAssetPrecision"])
                                        if baseAssetPrecision == 1:
                                            decimal_places = decimal.Decimal("1")
                                            prevod_2 = prevod_2.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                        else:
                                            decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                            prevod_2 = prevod_2.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                            elif prevadim_z in zkratka_druhe[:3]:
                                prevod_2 = float(prevod_1)*float(cena)
                                for l in list_zaokrouhleni:
                                        prevod_2 = decimal.Decimal(str(prevod_2))
                                        if l["symbol"] == zkratka_druhe:
                                            baseAssetPrecision = int(l["baseAssetPrecision"])
                                            if baseAssetPrecision == 1:
                                                decimal_places = decimal.Decimal("1")
                                                prevod_2 = prevod_2.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                            else:
                                                decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                                prevod_2 = prevod_2.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                        print(prevod_2)
                        print(str(zkratka_druhe))
                        prevod_1 = decimal.Decimal(str(prevod_1))
                        #if prevedeno_do_2 == zkratka_druhe[:3]:
                
                        trade = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)

                        params = {
                            "symbol": str(zkratka_druhe),
                            "side": "BUY",
                            "type": "LIMIT",
                            "quantity": str(prevod_2),
                            "price": str(cena)
                            # 'quoteOrderQty': 5.1
                            # "recvWindow": 60000
                        }

                        trade.post_order(params)
                        print(response)
                        time.sleep(4)
                        account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
                        found_balance = False  # Příznak pro označení nalezení podmínky
                        for x in account_information['balances']:
                            if prevedeno_do_2 in x["asset"] and prevod_2 > decimal.Decimal(str(x["free"])):
                                order = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
                                params = {
                                    "symbol": zkratka_druhe
                                }

                                response = order.delete_openorders(params)
                                print(response)
                                found_balance = True  # Nalezení podmínky
                                break
                        if found_balance:
                            continue  # Pokračovat zpět na začátek bloku "try"

                        """if prevedeno_do_2 == zkratka_druhe[3:]:
                            trade = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
                        

                            params = {
                                "symbol": str(zkratka_druhe),
                                "side": "SELL",
                                "type": "LIMIT_MAKER",
                                "quantity": str(prevod_1),
                                "price": str(cena)
                                # 'quoteOrderQty': 5.1
                                # "recvWindow": 60000
                            }
                            
                            response = trade.post_order(params)
                            print(response)
                            time.sleep(3)

                            account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
                            found_balance = False  # Příznak pro označení nalezení podmínky
                            for x in account_information['balances']:
                                if prevedeno_do_2 in x["asset"] and prevod_2 >= decimal.Decimal(str(x["free"])):
                                    print(prevedeno_do_2, x["asset"], prevod_2, x["free"])
                                    order = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
                                    params = {
                                        "symbol": zkratka_druhe
                                    }

                                    response = order.delete_openorders(params)
                                    print(response)
                                    found_balance = True  # Nalezení podmínky
                                    break
                        if found_balance:
                            continue  # Pokračovat zpět na začátek bloku "try"""

                        if 'code' in response:
                            error_code = response['code']
                            if error_code == 30004 or 700003:
                                continue

                        break
                    except Exception as e:
                        print("An unexpected error occurred:", str(e))
                        

            druha_smena(x["prevedeno_do_2"], x["zkratka_druhe"], x["prevedeno_do_1"], x["prevod_2"])

            print("prevedlo se do druhe kryptomeny")

            account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
            for balance in account_information["balances"]:
                if balance["asset"] == x["zkratka_druhe"]:
                    print(x["asset"], x["free"])

            def treti_smena(prevedeno_do_2):
                while True:
                    try:
                        prevod_2 = 0.0
                        account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
                        zustatek_USDC = 0.0
                        for balance in  account_information['balances']:
                            if balance['asset'] == "USDC":
                                zustatek_USDC = balance["free"]
                                
                        for balance in account_information['balances']:
                            if balance['asset'] == prevedeno_do_2:
                                prevod_2 = decimal.Decimal(str(balance['free']))
                                for l in list_zaokrouhleni:
                                    if l["symbol"] == prevedeno_do_2+"USDC":
                                        baseAssetPrecision = int(l["baseAssetPrecision"])
                                        if baseAssetPrecision == 1:
                                            decimal_places = decimal.Decimal("1")
                                            prevod_2 = prevod_2.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                                        else:
                                            decimal_places = decimal.Decimal("0." + "0" * baseAssetPrecision)
                                            prevod_2 = prevod_2.quantize(decimal_places, rounding=decimal.ROUND_DOWN)
                    
                        url = 'https://api.mexc.com/api/v3/ticker/price'
                        params = {'symbol': str(prevedeno_do_2+"USDC")}
                        response = requests.get(url, params=params)
                        cena = response.json()

                        trade = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)

                        params = {
                            "symbol": str(prevedeno_do_2+"USDC"),
                            "side": "SELL",
                            "type": "LIMIT",
                            "quantity": str(prevod_2),
                            "price": str(cena)
                            # 'quoteOrderQty': 5.1
                            # "recvWindow": 60000
                        }

                        
                        response = trade.post_order(params)
                        print(response)
                        time.sleep(4)
                        account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
                        found_balance = False  # Příznak pro označení nalezení podmínky
                        for x in account_information['balances']:
                            if "USDC" in x["asset"] and decimal.Decimal(str(zustatek_USDC)) >= decimal.Decimal(str(x["free"])):
                                order = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
                                params = {
                                    "symbol": str(prevedeno_do_2+"USDC")
                                }

                                response = order.delete_openorders(params)
                                found_balance = True  # Nalezení podmínky
                                break
                        if found_balance:
                            continue  # Pokračovat zpět na začátek bloku "try"
                        if 'code' in response:
                            error_code = response['code']
                            if error_code == 30004 or 700003:
                                continue

                        break
                    except Exception as e:
                        print("An unexpected error occurred:", str(e))
                        

            treti_smena(x["prevedeno_do_2"])
            
            account_information = mexc_spot_v3.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret).get_account_info()
            konecny_stav = 0.0
            for x in account_information["balances"]:
                if "USDC" in x["asset"]:
                    print(x["free"])
            