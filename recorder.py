import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import pyaudio
import wave
import time

CHUNK = 1024

if len(sys.argv) < 2:
      print("playing a wave file" % sys.argv[0])
      sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')
audio = pyaudio.PyAudio()

class Record():
      # count_changed = pyqtSignal(int)
      # print("Count changing", count_changed)

      def callback(self, in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return(data, pyaudio.paContinue)
            
      def stream_audio(self):
            self.stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=self.callback)
            print("Starting Recording!!")
            self.stream.start_stream()
            print(self.stream)
            # return self.stream
            # print("testing:", self.stream.start_stream())
            # self.count_changed.emit(self.stream.start_stream())
            if self.stream.is_active():
                  return time.sleep(0.01)
            return time.sleep(0.05)
            
      def stop_stream(self):
            print("Stopping Recording!!")
            print(self.stream)
            self.stream.stop_stream()
            self.stream.close()
            wf.close()
            audio.terminate()

class Test(QWidget):
      
      def __init__(self):
            super().__init__()
            self.initUI()

      def start(self):
            print("printing start button!")
      def stop(self):
            print("printing stop button!")

      def initUI(self):
            start_button = QPushButton('Start', self)
            self.recorder = Record()
            start_button.clicked.connect(self.recorder.stream_audio)
            start_button.resize(start_button.sizeHint())
            start_button.move(25, 50)
            
            stop_button = QPushButton('Stop', self)
            stop_button.clicked.connect(self.recorder.stop_stream)
            stop_button.resize(stop_button.sizeHint())
            stop_button.move(165, 50)

            quit_button = QPushButton('Quit', self)
            quit_button.clicked.connect(QApplication.instance().quit)
            quit_button.resize(quit_button.sizeHint())
            quit_button.move(95, 100)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('RECORDER')
            self.show()
            
if __name__ == '__main__':
#   # create application object
  app = QApplication(sys.argv)
  ex = Test()
  sys.exit(app.exec_())
#   # create the widget : default constructor
#   window = QWidget()
#   # the size of the window
#   window.resize(500, 300)
#   # set the position of the window on the screen
#   window.move(500, 500)
#   # set the window title
#   window.setWindowTitle('Chat BOT')
#   # display the window on the screen
#   window.show()
#   # ensures the clean exit
#   sys.exit(app.exec_())
