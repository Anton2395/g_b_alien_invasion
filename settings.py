class Settings:
    """Класс хранение всех настроек игры"""

    def __init__(self):
        """Инициализация ностройки игры"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (65, 105, 225)

        # Настройки корабля
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60
        self.bullet_allowed = 4