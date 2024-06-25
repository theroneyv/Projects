from datetime import datetime

now = datetime.now()

strtime = now.strftime('%I:%M:%P') 
strdate = now.strftime('%d/%m/%Y')

greet = '' 

if now.hour < 12: 
    greet = 'Good morning'
elif now.hour < 19:
    greet = 'Good afternoon'
else:
    greet = 'Good evening'

strgreet = f'{greet}, take a coffe!'

show = f'''
  ~   {strdate}
C|_|  {strtime}
 ---  {strgreet}
'''

def main():
    print(show)

if __name__ == '__main__':
    main()
