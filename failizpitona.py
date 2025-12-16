import turtle as t
import time
import tkinter as tk

screen = t.Screen()
screen.setup(width=1.0, height=1.0)
screen.screensize(canvwidth=1.0, canvheight=1.0)

# Используем update() для принудительной инициализации
screen.update()

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

# Убираем всю рамку окна - нельзя закрыть/свернуть
root.overrideredirect(True)

# Размещаем на весь экран
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

# Всегда поверх других окон
root.attributes('-topmost', True)

# Блокируем стандартное закрытие
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Переменные для отслеживания тройного клика
click_count = 0
last_click_time = 0
window_locked = True  # Флаг блокировки окна
program_running = True  # Флаг работы программы
animation_completed = False  # Флаг завершения анимации


def unlock_window():
    """Разблокирует окно (восстанавливает рамку)"""
    global window_locked
    window_locked = False
    root.overrideredirect(False)
    root.attributes('-topmost', False)
    root.protocol("WM_DELETE_WINDOW", root.destroy)


def exit_program():
    """Завершает программу"""
    global program_running
    program_running = False
    try:
        root.quit()
        root.destroy()
    except:
        pass
    try:
        t.bye()
    except:
        pass


def secret_combo_exit(event=None):
    """Секретный выход по комбинации клавиш Ctrl+Alt+X"""
    exit_program()


def check_triple_click(x, y):
    """Проверяет тройной клик в левом нижнем углу"""
    global click_count, last_click_time

    # ЕСЛИ АНИМАЦИЯ ЗАВЕРШЕНА - НЕ ОБРАБАТЫВАЕМ КЛИКИ
    if animation_completed:
        return

    if not program_running:
        return

    # Область в левом нижнем углу (100x100 пикселей)
    screen_width = screen.window_width() // 2
    screen_height = screen.window_height() // 2
    corner_area = 100

    # Проверяем, что клик в целевой области (левый нижний угол)
    left_bound = -screen_width
    bottom_bound = -screen_height

    if (left_bound <= x <= left_bound + corner_area and
            bottom_bound <= y <= bottom_bound + corner_area):

        current_time = time.time()

        # Если прошло больше 2 секунд - сбрасываем счетчик
        if current_time - last_click_time > 2.0:
            click_count = 1
        else:
            click_count += 1

        last_click_time = current_time

        if click_count >= 3:
            exit_program()
    else:
        # Клик вне целевой области - сбрасываем счетчик
        click_count = 0


# ПРАВИЛЬНАЯ РЕГИСТРАЦИЯ КОМБИНАЦИИ КЛАВИШ
def setup_key_bindings():
    """Настраивает привязки клавиш"""
    # Привязываем комбинацию Ctrl+Alt+X к корневому окну
    root.bind('<Control-Alt-KeyPress-x>', secret_combo_exit)
    root.bind('<Control-Alt-KeyPress-X>', secret_combo_exit)  # Для Caps Lock

    # Также привязываем к canvas на всякий случай
    canvas.bind('<Control-Alt-KeyPress-x>', secret_combo_exit)
    canvas.bind('<Control-Alt-KeyPress-X>', secret_combo_exit)

    # Фокусируем окно, чтобы оно получало события клавиатуры
    root.focus_force()


def draw_house():
    t.penup()
    t.goto(-200, -150)
    t.pendown()

    # Основание дома
    t.fillcolor("#F5DEB3")
    t.begin_fill()
    for _ in range(4):
        t.forward(150)
        t.left(90)
    t.end_fill()

    # Крыша
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.fillcolor("#8B4513")
    t.begin_fill()
    t.goto(-125, 80)
    t.goto(-50, 0)
    t.goto(-200, 0)
    t.end_fill()

    # Окно
    t.penup()
    t.goto(-170, -80)
    t.pendown()
    t.fillcolor("#87CEEB")
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

    # Рама окна
    t.color("#8B4513")
    t.penup()
    t.goto(-145, -80)
    t.pendown()
    t.goto(-145, -30)
    t.penup()
    t.goto(-170, -55)
    t.pendown()
    t.goto(-120, -55)

    # Дверь
    t.penup()
    t.goto(-110, -150)
    t.pendown()
    t.fillcolor("#654321")
    t.begin_fill()
    t.goto(-110, -60)
    t.goto(-80, -60)
    t.goto(-80, -150)
    t.end_fill()

    # Ручка двери
    t.penup()
    t.goto(-105, -105)
    t.pendown()
    t.dot(8, "gold")


def draw_tree():
    # Ствол
    t.penup()
    t.goto(150, -150)
    t.pendown()
    t.fillcolor("#8B4513")
    t.begin_fill()
    t.goto(150, -30)
    t.goto(175, -30)
    t.goto(175, -150)
    t.goto(150, -150)
    t.end_fill()

    # Крона - симметричная вокруг ствола
    t.penup()
    t.goto(162.5, -30)
    t.pendown()
    t.fillcolor("#228B22")
    t.begin_fill()
    t.circle(62.5)
    t.end_fill()

    # Второй уровень кроны
    t.penup()
    t.goto(175, 10)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Третий уровень кроны
    t.penup()
    t.goto(187.5, 40)
    t.pendown()
    t.begin_fill()
    t.circle(37.5)
    t.end_fill()


def draw_sun():
    t.penup()
    t.goto(250, 160)
    t.pendown()

    # Основной круг солнца
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(45)
    t.end_fill()

    # Лучи солнца
    t.color("orange")
    t.pensize(3)
    for angle in range(0, 360, 30):
        t.penup()
        t.goto(250, 200)
        t.pendown()
        t.setheading(angle)
        t.forward(70)

    t.color("black")
    t.pensize(1)


def clear_screen():
    t.clear()
    screen.bgcolor("lightblue")
    t.penup()
    t.goto(0, 0)
    t.pendown()


def draw_plus_sign():
    t.pensize(15)
    t.color("black")
    t.speed(0)

    # Вертикальная линия
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.goto(0, -200)

    # Горизонтальная линия
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.goto(200, 0)

    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.goto(-200, 200)

    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.goto(200, 200)

    t.penup()
    t.goto(200, 0)
    t.pendown()
    t.goto(200, -200)

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(-200, -200)

    t.pensize(1)


def safe_sleep(seconds):
    """Безопасная пауза с проверкой флага программы"""
    end_time = time.time() + seconds
    while time.time() < end_time and program_running:
        root.update()
        time.sleep(0.1)


def disable_turtle_clicks():
    """Отключает обработку кликов черепахой после завершения анимации"""
    global animation_completed
    animation_completed = True
    # Отключаем все обработчики кликов
    t.onscreenclick(None, btn=1)
    t.onscreenclick(None, btn=2)
    t.onscreenclick(None, btn=3)


def main():
    global program_running

    try:
        # Регистрируем секретные лазейки
        t.onscreenclick(check_triple_click, btn=1)
        setup_key_bindings()
        t.listen()
        t.speed(0)

        # Перефокусируем окно для гарантии работы клавиатуры
        root.focus_force()

        # Рисуем улучшенный пейзаж
        draw_house()
        draw_tree()
        draw_sun()

        # Ждем 3 секунды (с проверкой выхода)
        safe_sleep(3)

        if not program_running:
            return

        # Очищаем экран
        clear_screen()

        # Рисуем знак +
        draw_plus_sign()

        # Ждем 10 секунд после завершения рисования
        safe_sleep(10)

        if not program_running:
            return

        # ОТКЛЮЧАЕМ ОБРАБОТКУ КЛИКОВ ПЕРЕД РАЗБЛОКИРОВКОЙ
        disable_turtle_clicks()

        # После завершения всей анимации разблокируем окно
        unlock_window()

        print("Рисование завершено! Окно разблокировано.")
        print("Обработка кликов отключена - программа не будет вылетать.")

        # Запускаем основной цикл Tkinter вместо Turtle
        while program_running:
            root.update()
            time.sleep(0.1)

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        exit_program()


# Запускаем программу
if __name__ == "__main__":
    main()
