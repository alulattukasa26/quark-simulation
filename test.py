import random
import math
import pyglet

window = pyglet.window.Window(800, 600, "Хаотичный кружок")

# Создаем кружок в центре экрана
circle = pyglet.shapes.Circle(x=400, y=300, radius=25, color=(50, 200, 255))

speed = 250  # скорость (пикселей в секунду)
angle = random.uniform(0, 2 * math.pi)  # случайный начальный угол движения

def update(dt):
    global angle

    # 1. Добавляем случайное отклонение к текущему углу (эффект блуждания)
    angle += random.uniform(-4.0, 4.0) * dt

    # 2. Вычисляем новые координаты
    circle.x += math.cos(angle) * speed * dt
    circle.y += math.sin(angle) * speed * dt

    # 3. Не даем кружку улететь за границы окна (отскок)
    if circle.x < circle.radius:
        circle.x = circle.radius
        angle = math.pi - angle
    elif circle.x > window.width - circle.radius:
        circle.x = window.width - circle.radius
        angle = math.pi - angle

    if circle.y < circle.radius:
        circle.y = circle.radius
        angle = -angle
    elif circle.y > window.height - circle.radius:
        circle.y = window.height - circle.radius
        angle = -angle

@window.event
def on_draw():
    window.clear()
    circle.draw()

# Запускаем update 60 раз в секунду
pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
