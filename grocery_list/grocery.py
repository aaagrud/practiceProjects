import flet as ft

def main(page):
    page.title = "Grocery List"
    def when_click(e):
        if new_task.value == "":
            new_task.value = "invalid entry"
            page.add(ft.Checkbox(label = new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()
        else:
            page.add(ft.Checkbox(label = new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()
    
    page.add(ft.Text(value = "GROCERY LIST!", color="blue"))
    new_task = ft.TextField(hint_text="Enter Grocery Item", width = 500)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add To List", on_click = when_click)]))

ft.app(target = main)