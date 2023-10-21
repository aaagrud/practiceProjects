import flet as ft
def main(page):
    page.title = "Timed ToDo"
    def add_task(e):
        page.add(ft.Checkbox(label=f"{new_task.value} : {time.value}"))
        new_task.value = ""
        new_task.focus()
        new_task.update()
        time.value = ""
        time.focus()
        time.update()
    new_task = ft.TextField(hint_text="Whats needs to be done?", width=400)
    time = ft.TextField(hint_text="time?", width=200)
    page.add(ft.Row([new_task, time, ft.ElevatedButton("Add", on_click=add_task)]))
ft.app(target=main)