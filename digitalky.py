import tkinter as tk
from datetime import datetime

win = tk.Tk()

W = 1800
H = 400
canvas = tk.Canvas(win, width=W, height=H, background="black")
canvas.pack()

class Line:
    def __init__(self, point: tuple, dx: int, dy: int, colour: str, canvas):
        self.coords = point
        self.dx = dx
        self.dy = dy
        self.colour = colour
        self.canvas = canvas
        self.id = None
        if dx < dy:
            self.id = canvas.create_polygon(point[0], point[1], point[0] + dx // 2, point[1] - dx // 2, point[0] + dx,
                                            point[1], point[0] + dx, point[1] + dy, point[0] + dx // 2,
                                            point[1] + dy + dx // 2, point[0], point[1] + dy, fill=colour,
                                            outline="black", width="4")
        elif dx > dy:
            self.id = canvas.create_polygon(point[0], point[1], point[0] + dx, point[1], point[0] + dx + dy // 2,
                                            point[1] + dy // 2, point[0] + dx, point[1] + dy, point[0],
                                            point[1] + dy, point[0] - dy // 2, point[1] + dy // 2, fill=colour,
                                            outline="black", width="4")
        else:
            self.id = canvas.create_rectangle(point[0], point[1], point[0] + dx, point[1] + dy, fill=colour,
                                                outline="")

    def change_color(self, new_color):
        canvas.itemconfig(self.id, fill=new_color)


class Segment:
    def __init__(self, point: tuple, dx: int, dy: int, small: int, big: int, colour: str, canvas):
        self.parts = []
        self.coords = point
        self.colour = colour
        x, y = point[0], point[1]
        self.parts.append(Line((x + small, y), big, small, colour, canvas))
        self.parts.append(Line((x + small + big, y + small), small, big, colour, canvas))
        self.parts.append(Line((x + small, y + big + small), big, small, colour, canvas))
        self.parts.append(Line((x, y + small), small, big, colour, canvas))
        self.parts.append(Line((x + small + big, y + small * 2 + big), small, big, colour, canvas))
        self.parts.append(Line((x + small, y + big * 2 + small * 2), big, small, colour, canvas))
        self.parts.append(Line((x, y + small * 2 + big), small, big, colour, canvas))

    def reset(self):
        for part in self.parts:
            part.change_color("red")

    def display(self, number: int):
        self.reset()
        if number == 0:
            self.parts[2].change_color("black")
        elif number == 1:
            self.parts[2].change_color("black")
            self.parts[3].change_color("black")
            self.parts[6].change_color("black")
            self.parts[5].change_color("black")
            self.parts[0].change_color("black")
        elif number == 2:
            self.parts[3].change_color("black")
            self.parts[4].change_color("black")
        elif number == 3:
            self.parts[3].change_color("black")
            self.parts[6].change_color("black")
        elif number == 4:
            self.parts[0].change_color("black")
            self.parts[5].change_color("black")
            self.parts[6].change_color("black")
        elif number == 5:
            self.parts[1].change_color("black")
            self.parts[6].change_color("black")
        elif number == 6:
            self.parts[1].change_color("black")
        elif number == 7:
            self.parts[2].change_color("black")
            self.parts[3].change_color("black")
            self.parts[6].change_color("black")
            self.parts[5].change_color("black")
        elif number == 8:
            pass
        elif number == 9:
            self.parts[6].change_color("black")


class Clock:
    def __init__(self, canvas):
        self.segments = []
        self.canvas = canvas
        spacing = 0.4
        for i in range(7):
            if i > 3:
                if i > 4:
                    spacing = 0.23
                x = i * (140 + spacing * 140)
                y = 200
                segment = Segment((x, y), 10, 50, 10, 50, "red", canvas)
                self.segments.append(segment)
            else:
                if i == 0 or i == 2 or i == 4:
                    x = i * (140 + spacing * 140) + 45
                else:
                    x = i * (140 + spacing * 140)
                y = 100
                segment = Segment((x, y), 20, 100, 20, 100, "red", canvas)
                self.segments.append(segment)
                if i == 3 or i == 1:
                    col_1 = Line((x + 160, y + 140), 20, 20, "red", canvas)
                    col_2 = Line((x + 160, y + 100), 20, 20, "red", canvas)
                    col_1.change_color("red")
                    col_2.change_color("red")

    def current_time(self):
        current_time = datetime.now().strftime("%H%M%S%f")

        for i in range(7):
            digit = int(current_time[i])
            self.segments[i].display(digit)

        win.after(1, self.current_time)

def current_time(self):
        current_time = datetime.now().strftime("%H%M%S%f")
        hours = current_time[:2]
        minutes = current_time[2:4]
        seconds = current_time[4:6]
        milliseconds = current_time[6:]

        display_time = f"{hours}:{minutes}:{seconds}:{milliseconds}"  #mls NEFUGUJU

        for i in range(8): #2hod, 2min, 2sec, 2 mls
            if i < 7:
                digit = int(display_time[i])
                self.segments[i].display(digit)
            else: #vzdavam, logika je neni
                if display_time[i] == ':':
                    self.segments[i].display(10)
        win.after(1, self.current_time)

clock = Clock(canvas)
clock.current_time()
win.mainloop()
