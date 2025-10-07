# Create a timetable in your school

# Importing guizero
from guizero import App, Text

# Setting up main app with grid layout
window = App(title = "My Timetable", layout = "grid")

# Main thing

# Monday
monday_txt = Text(window, text = "Thứ hai", size = 15, grid = [0, 0])
monday_first = Text(window, text = "Sinh học", size = 15, grid = [0, 1])
monday_second = Text(window, text = "Vật lý", size = 15, grid = [0, 2])
monday_third = Text(window, text = "Tin học", size = 15, grid = [0, 3])
monday_fourth = Text(window, text = "HDTNHN", size = 15, grid = [0, 4])
monday_fifth =Text(window, text = "HDTNHN", size = 15, grid = [0, 5])

# Tuesday
tuesday_txt = Text(window, text= "Thứ ba", size= 15, grid= [1, 0])
tuesday_first = Text(window, text= "Ngữ văn", size= 15, grid= [1, 1])
tuesday_second = Text(window, text= "Lịch sử", size= 15, grid= [1, 2])
tuesday_third = Text(window, text= "Vật lý", size= 15, grid= [1, 3])
tuesday_fourth = Text(window, text= "Toán", size= 15, grid= [1, 4])
tuesday_fifth = Text(window, text= "Toán", size= 15, grid= [1, 5])

# Wednesday
wednesday_txt = Text(window, text= "Thứ tư", size=15, grid=[2, 0])
wednesday_first = Text(window, text= "Sinh học", size=15, grid=[2, 1])
wednesday_second = Text(window, text= "Lịch sử", size=15, grid=[2, 2])
wednesday_third = Text(window, text= "Vật lý", size=15, grid=[2, 3])
wednesday_fourth = Text(window, text= "Tiếng Anh", size=15, grid=[2, 4])
wednesday_fifth = Text(window, text= "Tiếng Anh", size=15, grid=[2, 5])

# Thursday
thursday_txt = Text(window, text= "Thứ năm", size= 15, grid= [3, 0])
thursday_first = Text(window, text= "Toán", size= 15, grid= [3, 1])
thursday_second = Text(window, text= "Toán", size= 15, grid= [3, 2])
thursday_third = Text(window, text= "Hóa học", size= 15, grid= [3, 3])
thursday_fourth = Text(window, text= "Tin học", size= 15, grid= [3, 4])
thursday_fifth = Text(window, text= "Tiếng Anh", size= 15, grid= [3, 5])

# Friday
friday_txt = Text(window, text= "Thứ sáu", size= 15, grid= [4, 0])
friday_first = Text(window, text= "Ngữ văn", size= 15, grid= [4, 1])
friday_second = Text(window, text= "Ngữ văn", size= 15, grid= [4, 2])
friday_third = Text(window, text= "Hóa học", size= 15, grid= [4, 3])
friday_fourth = Text(window, text= "Hóa học", size= 15, grid= [4, 4])
friday_fifth = Text(window, text= "HDTNHN", size= 15, grid= [4, 5])

# Run the app
window.display()