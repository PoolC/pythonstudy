#coding:utf-8

from entity import Entity
from component.world import WorldComponent
from component.display import DisplayComponent
from component.data import DataComponent
from component.fall import FallComponent
from component.camera import CameraComponent
from component.utility import tickall, QuitRequestFromFrontend

if __name__ == '__main__':        
    # Create the world
    world = Entity()\
    .attach(WorldComponent('mapdata.txt'))\
    .channel

    # Create the player
    player = Entity()\
    .attach(DataComponent('player', (40*1,40*8), 'mario.png'))\
    .attach(FallComponent())\
    .channel

    # Create an enemy
    enemy = Entity()\
    .attach(DataComponent('goomba', (40*5,40*5), 'goomba.png'))\
    .attach(FallComponent())\
    .channel
    
    enemy2 = Entity()\
    .attach(DataComponent('flower', (40*8,40*14), 'flower.png'))\
    .attach(FallComponent())\
    .channel
    
    # Create a camera
    camera = Entity()\
    .attach(CameraComponent())\
    .channel
    
    # Create the display
    display = Entity()\
    .attach(DisplayComponent())\
    .channel
    
    # Display subsystem
    display.sendto(world, 'set_frontend')
    #camera.sendto(world, 'set_camera')
    
    # Logic subsystem
    player.sendto(world, 'spawn_me')
    player.sendto(world, 'i_am_player')
    enemy.sendto(world, 'spawn_me')
    enemy2.sendto(world, 'spawn_me')
    
    # Tick all components
    try:
        while True:
            tickall()
    except QuitRequestFromFrontend:
        pass
