#coding:utf-8

from entity import Entity
from component.world import WorldComponent
from component.display import DisplayComponent
from component.data import DataComponent
from component.sprite import SpriteComponent
from component.camera import CameraComponent
from component.utility import tickall, QuitRequestFromFrontend

if __name__ == '__main__':        
    # Create the world
    world = Entity()\
    .attach(WorldComponent())\
    .channel

    # Create the display
    display = Entity()\
    .attach(DisplayComponent())\
    .channel

    # Create the player
    player = Entity()\
    .attach(DataComponent('player', (0,0)))\
    .attach(SpriteComponent())\
    .channel

    # Create an enemy
    enemy = Entity()\
    .attach(DataComponent('goomba', (100,0)))\
    .attach(SpriteComponent())\
    .channel

    # Create a camera
    camera = Entity()\
    .attach(DataComponent('camera', (0,0)))\
    .attach(CameraComponent())\
    .channel

    # Create a tree
    tree = Entity()\
    .attach(DataComponent('i \'m tree!', (150,0)))\
    .attach(SpriteComponent())\
    .channel

    # Logic subsystem
    player.sendto(world, 'spawn_me')
    enemy.sendto(world, 'spawn_me')

    # Display subsystem
    display.sendto(world, 'set_frontend')
    camera.sendto(world, 'set_camera')
    
    # Tick all components
    try:
        while True:
            tickall()
    except QuitRequestFromFrontend:
        pass
