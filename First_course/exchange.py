from helpers import reader_from_data_storage, exchange, initialization

initialization()

while True:
    print('AVAILABLE COMMANDS: COURSE USD, COURSE UAH, EXCHANGE USD (amount), EXCHANGE UAH (amount)')
    choice = (input('Enter your command: '))
    if choice == 'STOP':
        break
    try:
        splitted_input = choice.split()
        if splitted_input[0] == 'COURSE' and splitted_input[1] == 'USD':
            print(f'RATE: {reader_from_data_storage().get("USD_current_rate"):.5};'
                  f' AVAILABLE: {float(reader_from_data_storage().get("USD")):.2f} USD')
        elif splitted_input[0] == 'COURSE' and splitted_input[1] == 'UAH':
            print(f'RATE: {reader_from_data_storage().get("UAH_current_rate"):.5};'
                  f' AVAILABLE: {float(reader_from_data_storage().get("UAH")):.2f} UAH')
        elif splitted_input[0] == 'EXCHANGE' and splitted_input[1] == 'USD':
            exchange(float(splitted_input[2]), splitted_input[1])
        elif splitted_input[0] == 'EXCHANGE' and splitted_input[1] == 'UAH':
            exchange(float(splitted_input[2]), splitted_input[1])
        else:
            print(f'INVALID CURRENCY {splitted_input[1]}')
    except Exception:
        print('Incorrect input')
