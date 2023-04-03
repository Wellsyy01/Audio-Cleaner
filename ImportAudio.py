from scipy.io import wavfile

def import_audio(filepath) {

    if (filepath.endswith('.wav')) {
        samplerate, sampledata = wavfile.read('./prep_audio/working_audio.wav')
    }
    // TODO Alternate file inputs
    else {
        return 0
    }

    // TODO Sanitise Inputs

    return samplerate, sampledata

}