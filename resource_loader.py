import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

player_image = pyglet.resource.image("car.png")
background_image = pyglet.resource.image("bg.png")

