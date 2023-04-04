'''
from game.sound.echo import echo_test
from game.graphic.render import render_test

echo_test()
render_test()
'''

from game.sound import echo
from game.graphic import render
from myerror import myerror

a = echo
b = render

a.echo_test()
b.render_test()

try:
    raise myerror.MyError()
except myerror.MyError as e:    
    print(e)
finally:
    print("작업을 종료하였습니다.")    



