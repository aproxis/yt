from pydub import AudioSegment
from pydub.effects import AudioEffectsChain

mono_audio = AudioSegment.from_file("mono.wav", format="wav")

# noise reduction, equalization, normalization
effects = (AudioEffectsChain()
           .lowshelf()
           .equalizer(frequency=100, gain=-3.0)
           .normalize())

processed_audio = effects(mono_audio)

# mono to stereo
stereo_audio = processed_audio.repeat(2)
stereo_audio.export("stereo.wav", format="wav")
