import Errors

def __parse_config(line):

    if line == '':
        return None
    
    components = line.split(",")
    if len(components) != 3:
        return 3, 'Incorrect number of arguments: ' + line

    try:

        s_freq = int(components[0])
        if (s_freq > int(components[1])):
            e_freq = s_freq
            s_freq = int(components[1])
        else:
            e_freq = int(components[1])

        scale = float(components[2])

    except:
        return 3, 'Incorrect filter input format: ' + line + '.'
    
    compilation = [[s_freq, e_freq], scale]

    return compilation, ''


def import_config(filepath):

    config_file = open(filepath, 'r')

    filter_list = []

    count = 1
    for line in config_file:

        parameter, err_message = __parse_config(line)


        if isinstance(parameter, int):
                Errors.error_check(1, parameter, 'Line ' + count + ': ' + err_message)
        elif isinstance(parameter, list):
                filter_list.append(parameter)


    if len(filter_list):
        return filter_list
    
    Errors.error_check(1, 4)
            