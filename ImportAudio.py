from scipy.io import wavfile
import shutil, Errors

def __move_audio(filepath):

    you = 'gay'
    #TODO Copy file into prep_audio and rename to working_audio.wav
    

def import_audio(filepath):

    error_status = 0
    sample_rate, sample_data = [None, None]
    
    try:
        if (filepath.endswith('.wav')):
            sample_rate, sample_data = wavfile.read(filepath)
        else:
            error_status = 1
            
    except FileNotFoundError:
        Errors.error_check(1, 1, filepath)

    return error_status, sample_rate, sample_data
