import random

ball_list=list(range(1,34));
red_ball_list=random.sample(ball_list,6)
red_ball_list.sort()
ball_all =""
red_ball_str=""
blue_ball=random.randint(1,16)
for i in red_ball_list:
    red_ball_str += ' %02d '%i;
ball_all += '%s + %02d' %(red_ball_str, blue_ball)
print(ball_all)