from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# получение координат игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# установка одного блока по координатам
# mc.setBlock(x, y, z, block_id) 
# x, y, z - координаты
# block_id - id блока

# mc.setBlock(x+2, y, z, 14)


# установка сразу большого количества блоков
# mc.setBlocks(x1, y1, z1, x2, y2, z2, block_id)
# команда строит параллелепипед по крайним диагональным точкам
width = 4
height = 3
length = 7
mc.setBlocks(x, y, z, x+width, y+height, z+length, 133)
# строим внутри воздух
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, 0)

# строим пушку
mc.setBlocks(x+1, y+height, z+2, x+1+2, y+height+2, z+2+1, 49)

gun_length = 9
for i in range(gun_length+1):
    mc.setBlock(x+2, y+height+2, z+4+i, 49)
mc.setBlock(x+2, y+height+2, z+4+i, 46)
