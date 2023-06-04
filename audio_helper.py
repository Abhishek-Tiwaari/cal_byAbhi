import pyttsx3



engine = pyttsx3.init()
engine.say("Hey ABHISHEK!! "
           "YOUR CALCULATOR IS READY TO HELP YOU")
engine.runAndWait()

class PlayAudio:
    def __init__(self, voice='female', speakstatus=True):
        self.voice = 'female'
        self.speakstatus = speakstatus
        self.speakWords = {
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'Seven',
            '8': 'eight',
            '9': 'nine',
            '+': 'plus',
            '=': 'equal to, your answer is...',
            '-': 'minus',
            'x': 'multiply By',
            '/': 'divide By',
            '<--': 'clear',
            'AC': 'all clear',
            '.': 'dot',
            ',': 'for power',
            '√': 'square root',
            '^': 'calculate power',
            'x!': 'calculate factorial',
            'toRad': 'calculate Radian',
            'toDeg': 'calculate degree',
            'sinθ': 'calculate sinθ',
            'cosθ': 'calculate cosθ',
            'tanθ': 'calculate tanθ',
            'mode': 'you can select scientific calculator',
            '0': 'Zero'

        }
        self.engine = pyttsx3.init()
        v = self.engine.getProperty('voices')
        self.engine.setProperty('voice', v[1].id)

    def speak(self, content):
        engine = pyttsx3.init()
        if self.speakstatus == True:
            self.engine.say(self.speakWords[content])
            self.engine.runAndWait()



if __name__ == '__main__':
    ob = PlayAudio()
    ob.speak('=')
