# from pydub import AudioSegment
#
# sound = AudioSegment.from_mp3('yssa.mp3')
# sound.export('yssa.wav', format='wav')
#
# sound = AudioSegment.from_wav('yssa.wav')
# sound.export('lll.mp3', format='mp3')

from tkinter import *
root = Tk()
theLabel = Label(root, text='文本文件，这是一个可视化的文本文件', justify=LEFT, font=('楷体', 20), fg='red')
theLabel.pack()
mainloop()