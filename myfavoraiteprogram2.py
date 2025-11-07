import turtle,colorsys
turtle.bgcolor("black");t=turtle.Turtle();t.speed(0);turtle.colormode(255)
n=36
h=0
for _ in range(10000):
    col=colorsys.hsv_to_rgb(h,1,1);t.pencolor(int(col[0]*255),int(col[1]*255),int(col[2]*255))
    for _ in range(6): t.circle(60); t.right(60)
    t.right(5)
    h+=1/n
    h%=1
turtle.done()