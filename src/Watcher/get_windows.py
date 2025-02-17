import os
import time

class window:
    def __init__(self, class_name, title_name):
        self.class_name = class_name
        self.title_name = title_name

# get classname of app that user working on
def active_window():
    # running bash command and storing result as a string
    active_window = os.popen("xdotool getwindowfocus getwindowclassname").read()
    active_window = active_window[0:-1]
    return active_window

# get title name of app that user working on
def active_window_title():
    active_window_title = os.popen("xdotool getwindowfocus getwindowname").read()
    active_window_title = active_window_title[0:-1]
    return active_window_title

# get list of opened apps in background as well as in foreground
def opened_windows_list():
    raw_data = os.popen('''wmctrl -lx | awk '{print $3}' ''').read()
    raw_data_ls = raw_data.split('\n')
    windows_list = []
    for x in raw_data_ls:
        last = x.rfind(".")
        windows_list.append(x[last+1::])
    windows_list.remove('')
    windows_list = list(set(windows_list))
    return windows_list

# returns true if user has move to next app which is not the same as previous
def is_window_changed(a):
    result = False
    while not(result):
        time.sleep(1)
        b = active_window()
        if a != b :
            result = True
        else:
            result = False
    return result


### what to do after window get change I've to append one line in csv data file in following format
### opened-time      closed-time      time-spent     window_class_name      window_title_name

### and whenever the user puts particular command it will make report till the time for that day and shows that report in terminal
