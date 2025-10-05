from guizero import App, Text, Picture, Box

# Main app
window = App(title = "Gallery", layout = "grid")

# Introduction Text
text = Text(window, grid = [0, 0], text = "Family Album", size = 25, color = "lightblue")

# Picture Box
picture_1 = Picture(window, grid = [0, 0], image = "shed.png")   

picture_2 = Picture(window, grid = [1, 0], image = "coolkidd.png")

picture_3 = Picture(window, grid = [0, 1], image = "slasher.png")

picture_4 = Picture(window, grid = [1, 1], image = "guest.png")   

# Run app
window.display()