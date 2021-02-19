import mcpi.minecraft as minecraft
import mcpi.block as block

mc= minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for a in range(1):
    mc.setBlocks(pos.x,pos.y,pos.z,pos.x+400,pos.y+400,pos.z+400,block.AIR.id)