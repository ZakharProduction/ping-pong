from pygame import *

# базовый класс для спрайтов
class GameSprite(sprite.Sprite):
    """
    image_file - имя файла с картинкой для спрайта
    x - координата x спрайта
    y - координата y спрайта
    speed - скорость спрайта
    size_x - размер спрайта по горизонтали
    size_y - размер спрайта по вертикали
    """

    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()  # конструктор суперкласса
        self.image = transform.scale(
            image.load(image_file), (size_x, size_y)
        )  # создание внешнего вида спрайта - картинки
        self.speed = speed  # скорость
        self.rect = (
            self.image.get_rect()
        )  # прозрачная подложка спрайта - физическая модель
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        # отобразить картинку спрайта в тех же координатах, что и его физическая модель
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс для игрока
class Player(GameSprite):
    # метод для управления игрока стрелками клавиатуры
    def update_r(self):
        # получаем словарь состояний клавиш
        keys = key.get_pressed()

        # если нажата клавиша влево и физическая модель не ушла за левую границу игры
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        # если нажата клавиша вправо и физическая модель не ушла за правую границу игры
        if keys[K_DOWN] and self.rect.y < width - 70:
            self.rect.y += self.speed

    def update_l(self): 
                # получаем словарь состояний клавиш
        keys = key.get_pressed()

        # если нажата клавиша влево и физическая модель не ушла за левую границу игры
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        # если нажата клавиша вправо и физическая модель не ушла за правую границу игры
        if keys[K_s] and self.rect.y < width - 70:
            self.rect.y += self.speed

# переменная окончания игры
finish = False  # когда True, то спрайты перестают работать
# переменная завершения программы
game = True  # завершается при нажатии кнопки закрыть окно

# размеры окна
width = 700
height = 500

# создание окна
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
back = (200, 255, 255)
window.fill(back)
clock = time.Clock()
FPS = 60

# шрифт
font.init()
font1 = font.SysFont("Times New Roman", 36)
lose1 = font1.render('Player 1 Lose!', True, (180, 0 ,0))
lose2 = font1.render('Player 2 Lose!', True, (180, 0 ,0))

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = Player('tenis_ball.png', 200, 200, 4, 50, 50)
ball_x = 3
ball_y = 3
# игровой цикл
while game:
    # обработка нажатия кнопки Закрыть окно
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += ball_x
        ball.rect.y += ball_y

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)