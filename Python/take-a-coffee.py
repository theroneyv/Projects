from datetime import datetime
import platform
import getpass
from style import style, colors

now = datetime.now()

strtime = now.strftime('%I:%M:%P') 
strdate = now.strftime('%d/%m/%Y')

os_info = platform.uname()
os_name = os_info.system
os_release = os_info.release
os_version = os_info.version

username = getpass.getuser()
hostname = platform.node()

cpu_info = platform.processor()

greet = '' 

if now.hour < 12: 
    greet = 'Good morning'
elif now.hour < 19:
    greet = 'Good afternoon'
else:
    greet = 'Good evening'

strgreet = f'{greet}, take a coffe!'
strheader = f'{username}@{hostname}'
strheaderline = '-' * len(strheader)

strcolors = style('    ', 7, colors['yellow']) + style('    ', 7, colors['blue']) + style('    ', 7, colors['red'])

strshow = f'''
{strheader}
{strheaderline}
OS: {os_name} {os_release}
CPU: {cpu_info}
  
  ~   {strdate}
C|_|  {strtime}
 ---  {strgreet}

{strcolors}
'''

def show():
    return strshow

def main():
    print(show())

if __name__ == '__main__':
    main()