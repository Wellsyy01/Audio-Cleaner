import sys, getopt, logging
import ImportAudio as IAudio
import PrepareAudio as PAudio
import ArgumentHandler as AHandler



options, arguments = getopt.getopt(sys.argv[1:], short_options, long_options)
error_status, audio_location, config_location = AHandler.handle(options, arguments)

if (error_status) {

    logging.error('Error')

}


def handle(options, arguments) {

    t_arguments = [None, None]
    error = 0
    if arguments.length == 2:
        t_arguments[0] = arguments[0]
        t_arguments[1] = arguments[1]
    elif arguments.length != 2
        error = 1
        
    for opt in options:
        
        if (opt == '-h'):
            print(       'To run program for a given input audio file and configuration, input:' +
                    '\n\n     python PLACEHOLDER.py <audio file> <configuration file>' +
                    '\n\n Acceptable audio file extensions include:' +
                    '\n\n     *.wav' +
                      '\n     (include more file extensions here' +
                    '\n\n The configuration file should be a text file. For the correct format please check the (path)/config_format_help.txt' +
                    '\n   Acceptable frequency ranges will be from (x)Hz to (y)Hz'
                )

    return error, t_arguments[0], t_arguments[1]

}