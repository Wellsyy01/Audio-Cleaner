import logging

def __handle_error(error_code, message = ''):

    match error_code:
        case 0:
            logging.error(' Invalid command call structure. ' +
                      'Please run \'python PLACEHOLDER.py -h\' for help')
        case 1:
            logging.error(' Could not find file ' + message)
        case 2:
            logging.error(' Audio file is of an incorrect type. Audio formats supported: ' +
                          '\n     *.wav' + '\n')
            
    return 1


def error_check(error_status, error_code, message = ''):

    if error_status and __handle_error(error_code, message):
        exit()