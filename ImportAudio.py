from scipy.io import wavfile

def import_audio(filepath):

    if (filepath.endswith('.wav')):
        samplerate, sampledata = wavfile.read('./prep_audio/working_audio.wav')
    
    else:
        return 0

    return samplerate, sampledata
