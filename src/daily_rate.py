import csv

def main():
    ECB_rates_file_path = '../data/eurofxref.csv'

    with open(ECB_rates_file_path, mode='r') as file:
        csvFile = csv.reader(file)

        listHeader = []   
        for lines in csvFile:
            removed_date = lines[1:]
            listHeader.append(removed_date)

        currencies = listHeader[0]
        exchange_rates = listHeader[1:]
        
        result = {}

        index_currency = ''
        for index, value in enumerate(currencies):
            if value == ' JPY':
                rate = exchange_rates[0][index]
                result[value] = rate
                print('JPY added')
            elif value == ' GBP':
                rate = exchange_rates[0][index]
                result[value] = rate
                print('GBP added')
            elif value == ' SEK':
                rate = exchange_rates[0][index]
                result[value] = rate
                print('SEK added')
            elif value == ' USD':
                rate = exchange_rates[0][index]
                result[value] = rate
                print('USD added')

if __name__=="__main__":
    main()