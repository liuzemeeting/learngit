import random
nn=[]

while (len(nn)<6):
    aa=random.randint(0,9)
    if aa in nn:
        pass;
    else:
        nn.append(aa)
blue_ball = random.randint(1,19)
nn.sort()
ball_all = "";
for i in nn:
    ball_all += '%02d ' %i
ball_all += ' + %02d ' %blue_ball
print(ball_all)
