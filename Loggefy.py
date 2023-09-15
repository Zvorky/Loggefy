#   Loggefy
#   Simple Log and Notify


''' Enzo Zavorski Delevatti
||| @Zvorky
\\\          ___,
 \\\      .~´    `-,
  \\°    /  _    _ \.
   \°   ,\`|_|''|_|´\
    °    /          /)   °
        (\  ,    , .\`   |°
         `) ;`,; `,^,)   ||°
         ´,´  `,  `  `   |||
                          \\\
        September 2023     |||
                           '''


#   This code was taken from DropFilter project, you can check it on my Github :^)



import os, time
from gi.repository import Notify, GLib



#   Logger with Notify implementation
class Log:
    path = ''   # global path to the logs directory
    extension = '.txt'
    
    def __init__(self, title: str, version = None, console = False, notify = False):
        self.title = title
        self.subtitle = title
        self.version = version
        self.console = console
        self.notify = notify
        self.icon = ''
        self.file = Log.path + time.asctime() + Log.extension

        self.make()
    

    #   Set Notify Icon
    def setIcon(self, icon: str):
        try:
            with open(icon) as i:
                i.close()
                self.icon = icon
                return True
        except FileNotFoundError:
            return False


    def make(self):
        os.system('mkdir -p "' + Log.path + '"')
        os.system('touch "' + self.file + '"')

        text = '=| {} Log - {} |=\n'.format(self.title, time.asctime())
        if(self.version):
            text += 'Version {}'.format(self.version)
        text += '\n\n{}\nNotify: {}\n\n'.format(self.file, self.notify)

        self << text    #   Append

        if(self.notify):
            msg = ''
            if(self.version):
                msg += self.version + ' '
            msg += 'started!'

            Notify.init(self.title)
            self.notify = Notify.Notification.new(self.title, msg, self.icon)
            self.notify.show()

        if(self.console):
            os.system('clear')
            print(text)


    #   Append to log file
    def __lshift__(self, text: str):
        try:
            with open(self.file, 'a') as log:
                log.write(text + '\n')
                log.close()
        
        except FileNotFoundError:
            self.make()
            self << text
    

    #   Set Subtitle
    def __sub__(self, subtitle: str):        
        if(subtitle and self.subtitle != subtitle):
            self.subtitle = subtitle
            self << '\n -| ' + subtitle + ' |-'
            print  ('\n\033[0;1;30;47m -| ' + subtitle + ' |-\033[2;7;37m \033[0m ')


    #   Logs neutral message
    def log(self, message: str, newNotify = False):
        text = '       | ' + time.asctime() + ' |: ' + message

        self << text

        if(self.console):
            print(text)

        if(self.notify):
            if(newNotify):
                self.notify = Notify.Notification.new(self.subtitle, message, self.icon)
            else:
                self.notify.update(self.subtitle, message, self.icon)
            self.notify.show()


    #   Logs Informative message
    def info(self, message: str, subtitle = '', newNotify = True):
        self - subtitle
        self << 'info   | ' + time.asctime() + ' |: ' + message

        if(self.console):
            print('\033[0;1;30;47m ¡    \033[2;7;37m \033[0m| ' + time.asctime() + ' |: ' + message)

        if(self.notify):
            if(newNotify):
                self.notify = Notify.Notification.new(self.subtitle, message, self.icon)
            else:
                self.notify.update(self.subtitle, message, self.icon)
            self.notify.show()


    #   Logs Warning message
    def warn(self, message: str, subtitle = '', newNotify = True):
        self - subtitle
        self << 'warn   | ' + time.asctime() + ' |: ' + message

        if(self.console):
            print('\033[0;5;1;30;43m/!\\   \033[2;7;33m \033[0m| ' + time.asctime() + ' |: ' + message)

        if(self.notify):
            if(newNotify):
                self.notify = Notify.Notification.new('⚠️ ' + self.subtitle, message, self.icon)
            else:
                self.notify.update('⚠️ ' + self.subtitle, message, self.icon)
            self.notify.show()


    #   Logs Failure message
    def error(self, message: str, subtitle = '', newNotify = True):
        self - subtitle
        self << 'ERROR | ' + time.asctime() + ' |: ' + message

        if(self.console):
            print('\033[0;1;30;41m ERROR | ' + time.asctime() + ' |:\033[2;7;31m \033[0m' + message)

        if(self.notify):
            if(newNotify):
                self.notify = Notify.Notification.new(self.subtitle + ' ERROR', message, self.icon)
            else:
                self.notify.update(self.subtitle + ' ERROR', message, self.icon)
            self.notify.show()
    
    
    #   Move the log folder to trash
    def trash():
        os.system('gio trash ' + Log.path)
