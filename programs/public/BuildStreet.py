import random
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

SIZE = 10

def house():
    mid_x = x + SIZE/2
    mid_y = y + SIZE/2

    # Строим каменный куб
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE,z+SIZE,block.COBBLESTONE.id)
    # Очищаем пространство внутри дома
    mc.setBlocks(x+1, y+1, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.AIR.id)
    
    mc.setBlocks(x+3, y+SIZE-3, z, mid_x - 3, mid_y + 3, z, block.GLASS.id)
    mc.setBlocks(mid_x + 3, y + SIZE - 3, z, x+SIZE-3, mid_y + 3, z, block.GLASS.id)
    # Добавляем крышу
    mc.setBlocks(x,y+SIZE-1, z, x+SIZE, y+SIZE-1, z+SIZE,block.WOOD.id)
    # Добавим ковер
    mc.setBlocks(x+1,y+1,z+1, x+SIZE-1, y+1, z+SIZE-1, block.WOOL.id, c)
    # Вырежем проем для дверей
    mc.setBlocks(mid_x-1, y, z, mid_x+1, y+3, z, block.AIR.id)

    
    

    mc.setBlocks(x+1,y+1,z+1, x+SIZE-1, y+1, z+SIZE-1, block.WOOL.id, c)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
for i in range(5):
    c = random.randint(1,15)
    house()
    x = x + SIZE
