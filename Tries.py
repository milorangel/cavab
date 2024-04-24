class Obj():
    objs = []
    pos = []

    def __init__(self):
        print('init')
        Obj.objs.append(self)

    def act(self, pos):
        Obj.pos.append(pos)
        print(Obj.pos)
        print(pos)

o1 = Obj()
o2 = Obj()


for i in range(5):
    for o in Obj.objs:
        o.act(i)
