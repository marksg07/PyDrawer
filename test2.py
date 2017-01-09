import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('yo sup', font_name='Times New Roman', font_size=48, x=200, y=100, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

def draw_rect(x, y, width, height, color):
    width = int(round(width))
    height = int(round(height))
    image_pattern = pyglet.image.SolidColorImagePattern(color=color)
    image = image_pattern.create_image(width, height)
    image.blit(x, y)

draw_rect(200, 200, 200, 200, (255, 255, 255, 128))
pyglet.app.run()
