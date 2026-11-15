# ^^^ИМПОРТЫ^^^
import pyglet
from functions import get_quarks_center
import random
import math
import numpy as np

# ^^^ОСНОВНОЕ ОКНО^^^
window = pyglet.window.Window(width=1720, height=920, caption="Кварки")
batch = pyglet.graphics.Batch()

# ^^^СЛОИ^^^

quarks = pyglet.graphics.Group(order=1)
gluons = pyglet.graphics.Group(order=0)

# ^^^СПИСКИ ФИГУР^^^

circles = []

# ^^^ФИГУРЫ, ТЕКСТ И ПЕРЕМЕННЫЕ^^^

attraction_strength = 0.03
min_distance = 95

up_quark_r = pyglet.shapes.Circle(x=window.width // 2, y=220, radius=40, color=(255, 0, 0), batch=batch, group=quarks)
up_quark_g = pyglet.shapes.Circle(x=520, y=270, radius=40, color=(0, 255, 0), batch=batch, group=quarks)
down_quark_b = pyglet.shapes.Circle(x=680, y=450, radius=40, color=(0, 0, 255), batch=batch, group=quarks)



circles.append(up_quark_r)
circles.append(up_quark_g)
circles.append(down_quark_b)

point_x, point_y = get_quarks_center(circles)

center_point = pyglet.shapes.Circle(point_x, point_y, 2, color=(255, 255, 255), batch=batch, group=gluons)

line1 = pyglet.shapes.Line(center_point.x, center_point.y, thickness=3, x2=down_quark_b.x, y2=down_quark_b.y, color=(255, 255, 255), batch=batch, group=gluons)
line2 = pyglet.shapes.Line(center_point.x, center_point.y, thickness=3, x2=up_quark_r.x, y2=up_quark_r.y, color=(255, 255, 255), batch=batch, group=gluons)
line3 = pyglet.shapes.Line(center_point.x, center_point.y, thickness=3, x2=up_quark_g.x, y2=up_quark_g.y, color=(255, 255, 255), batch=batch, group=gluons)

label_u1 = pyglet.text.Label(
    "u", font_size=20, x=up_quark_r.x, y=up_quark_r.y,
    anchor_x="center", anchor_y="center", color=(255, 255, 255, 255), batch=batch
)
label_u2 = pyglet.text.Label(
    "u", font_size=20, x=up_quark_g.x, y=up_quark_g.y,
    anchor_x="center", anchor_y="center", color=(0, 0, 0, 255), batch=batch
)
label_d = pyglet.text.Label(
    "d", font_size=24, x=down_quark_b.x, y=down_quark_b.y,
    anchor_x="center", anchor_y="center", color=(255, 255, 255, 255), batch=batch
)
# ^^^ФИЗИКА^^^

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & pyglet.window.mouse.LEFT:
        for quark in circles:
            # Считаем расстояние только один раз
            distance = math.hypot(x - quark.x, y - quark.y)
            if distance <= quark.radius:
                # Сдвигаем сам кварк на величину сдвига мыши
                quark.x += dx
                quark.y += dy
                break  # Выходим из цикла, чтобы не захватить второй кварк, если они рядом


def update(dt):
    px, py = point_x, point_y

    for quark in circles:
        quark.vx = random.uniform(-2, 2)
        quark.vy = random.uniform(-2, 2)

        dx = px - quark.x
        dy = py - quark.y
        distance_to_point = math.hypot(dx, dy)

        if distance_to_point > min_distance:
            quark.vx += dx * attraction_strength
            quark.vy += dy * attraction_strength

        quark.x += quark.vx
        quark.y += quark.vy
        

    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            q1 = circles[i]
            q2 = circles[j]
            
            dx = q2.x - q1.x
            dy = q2.y - q1.y
            dist = math.hypot(dx, dy)
            min_dist = q1.radius + q2.radius  # Минимально допустимое расстояние (сумма радиусов)
            
            # Если кварки пересеклись
            if dist < min_dist:
                if dist == 0:
                    # Защита от деления на ноль, если центры совпали идеально
                    dx, dy, dist = 1.0, 0.0, 1.0
                
                # На сколько пикселей они зашли друг в друга
                overlap = min_dist - dist
                
                # Нормализуем вектор направления и раздвигаем каждый кварк на половину перекрытия
                nx = dx / dist
                ny = dy / dist
                
                q1.x -= nx * (overlap / 2)
                q1.y -= ny * (overlap / 2)
                q2.x += nx * (overlap / 2)
                q2.y += ny * (overlap / 2)

    for quark in circles:
        quark.x = max(quark.radius, min(window.width - quark.radius, quark.x))
        quark.y = max(quark.radius, min(window.height - quark.radius, quark.y))

    px, py = get_quarks_center(circles)
    center_point.x, center_point.y = px, py

    # линия к синему даун-кварку 
    line1.x, line1.y = px, py
    line1.x2, line1.y2 = down_quark_b.x, down_quark_b.y

    # линия к красному ап-кварку  
    line2.x, line2.y = px, py
    line2.x2, line2.y2 = up_quark_r.x, up_quark_r.y

    # линия к зеленому ап-кварку
    line3.x, line3.y = px, py
    line3.x2, line3.y2 = up_quark_g.x, up_quark_g.y

    # тексты
    label_u1.x, label_u1.y = up_quark_r.x, up_quark_r.y
    label_u2.x, label_u2.y = up_quark_g.x, up_quark_g.y
    label_d.x, label_d.y = down_quark_b.x, down_quark_b.y


# ^^^ЗАПУСК КАДРОВ^^^
pyglet.clock.schedule_interval(update, 1 / 60.0)

# ^^^ОТРИСОВКА^^^
@window.event
def on_draw():
    window.clear()
    batch.draw()

# ^^^КОНСОЛЬНЫЙ ВЫВОД И ТЕСТ^^^


# ^^^ЗАПУСК^^^
if __name__ == '__main__':
    pyglet.app.run()