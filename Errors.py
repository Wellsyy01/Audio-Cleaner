import logging

def __handle_error(error_code):

    match error_code:
        case 0:
            logging.error(' Invalid command call structure. ' +
                      'Please run \'python PLACEHOLDER.py -h\' for help')
            
    return 1


def error_check(error_status, error_code):

    if error_status and __handle_error(error_code):
        exit()