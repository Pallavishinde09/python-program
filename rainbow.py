import turtle as t

colors =[" red", "blue", " pink"," black","grey","peacock"," orange"," yellow"]
t.tracer( 0 ,0)

for i in range(45):

    t.color(colors[i%6])
    t.pendown()
    t.forward(2+i*5)
    t.left(45)
    t.width(i)
    t.penyp()
    t.update()
