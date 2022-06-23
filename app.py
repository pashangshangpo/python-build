from pydub import AudioSegment

print('start')

audio = AudioSegment.silent(3000)

audio.export(f'./S01E06.mp3', format='mp3')

print('end')

print('test')
