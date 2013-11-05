#coding:utf-8

from entity import Entity
from component.world import WorldComponent
from component.display import DisplayComponent
from component.data import DataComponent
from component.camera import CameraComponent
from component.utility import tickall, QuitRequestFromFrontend

if __name__ == '__main__':        
    # Create the world
    world = Entity()\
    .attach(WorldComponent())\
    .channel

    # Create the player
    player = Entity()\
    .attach(DataComponent('player', (50,100), 'mario.png'))\
    .channel

    # Create an enemy
    enemy = Entity()\
    .attach(DataComponent('goomba', (200,100), 'goomba.png'))\
    .channel
    
    enemy2 = Entity()\
    .attach(DataComponent('flower', (300,100), 'flower.png'))\
    .channel
    
    # Create a camera
    camera = Entity()\
    .attach(CameraComponent())\
    .channel
    
    # Create the display
    display = Entity()\
    .attach(DisplayComponent())\
    .channel

    '''
    # Create a tree
    tree = Entity()\
    .attach(DataComponent('i \'m tree!', (150,0)))\
    .channel
    '''
    
    # Display subsystem
    display.sendto(world, 'set_frontend')
    #camera.sendto(world, 'set_camera')
    
    # Logic subsystem
    player.sendto(world, 'spawn_me')
    enemy.sendto(world, 'spawn_me')
    enemy2.sendto(world, 'spawn_me')
    
    # Tick all components
    try:
        while True:
            tickall()
    except QuitRequestFromFrontend:
        pass
