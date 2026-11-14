"""מצייר לב צבעוני בטרמינל בעזרת משוואה מתמטית 💖"""
import time

COLORS = [31, 33, 32, 36, 34, 35]  # אדום, צהוב, ירוק, תכלת, כחול, סגול
MESSAGE = "I LOVE PYTHON "


def draw_heart():
    i = 0
    for y in range(15, -15, -1):
        line = ""
        for x in range(-30, 30):
            # משוואת הלב: (x^2 + y^2 - 1)^3 - x^2 * y^3 <= 0
            fx, fy = x * 0.05, y * 0.1
            if (fx**2 + fy**2 - 1) ** 3 - fx**2 * fy**3 <= 0:
                color = COLORS[(x + y) // 4 % len(COLORS)]
                line += f"\033[{color}m{MESSAGE[i % len(MESSAGE)]}\033[0m"
                i += 1
            else:
                line += " "
        print(line)
        time.sleep(0.05)  # אנימציה קטנה - שורה אחרי שורה


if __name__ == "__main__":
    draw_heart()
