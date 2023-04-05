import sys, getopt, logging, math
import ImportAudio as IAudio
import PrepareAudio as PAudio
import Errors
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq, ifft
from scipy.io.wavfile import write

def __handle(options, arguments):

    if (not arguments):
        error = 1
        return error, None, None

    t_arguments = [None, None]
    error = 0
    if len(arguments) == 2:
        t_arguments[0] = arguments[0]
        t_arguments[1] = arguments[1]
    elif len(arguments) != 2:
        error = 1
        
    for opt in options:
        
        if opt in ('-h' , 'help'):
            print(       'To run program for a given input audio file and configuration, input:' +
                    '\n\n     python PLACEHOLDER.py <audio file> <configuration file>' +
                    '\n\n Acceptable audio file extensions include:' +
                    '\n\n     *.wav' +
                      '\n     (include more file extensions here' +
                    '\n\n The configuration file should be a text file. For the correct format please check the (path)/config_format_help.txt' +
                    '\n   Acceptable frequency ranges will be from (x)Hz to (y)Hz'
                )

    return error, t_arguments[0], t_arguments[1]


def main():

    short_options = 'h';
    long_options = 'help';

    options, arguments = getopt.getopt(sys.argv[1:], short_options, long_options)
    error_status, audio_location, config_location = __handle(options, arguments)

    Errors.error_check(error_status, 0)

    error_status, sample_rate, sample_data = IAudio.import_audio(audio_location)

    Errors.error_check(error_status, 2)

    filters = [

        [[0, 400], 0]

    ]
    

    N = len(sample_data)

    T = 1/sample_rate
    x = np.linspace(0.0, sample_rate * T, sample_rate, endpoint = False)
    y_freq = rfft(sample_data) 
    x_freq = rfftfreq(N, T)

    location = 0
    count = 0

    for x in range(len(x_freq)):

        for bucket in filters:
            if ((x_freq[x] >= bucket[0][0]) and (x_freq[x] < bucket[0][1])):
                y_freq[x] = y_freq[x] * bucket[1]



    plt.plot(x_freq, np.abs(y_freq))
    plt.grid()
    plt.show()

    new_data = ifft(y_freq)
    write("example.wav", sample_rate, new_data.astype(np.int16))


    
main()

