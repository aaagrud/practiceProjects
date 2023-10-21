import flet as ft

def main(page: ft.page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    a = ft.TextField(label="a", autofocus=True, width=100)
    b = ft.TextField(label="b", width=100)
    operation = ft.TextField(label = "+", width=100)
    result = ft.TextField(value = "", width=100)
    status = ft.Text(value= "", color = "red")
    page.title = "Calculator"

    def calculator(e):
        if operation.value == '+':
            result.value = int(a.value) + int(b.value)
            page.update()
        if operation.value == '-':
            result.value = int(a.value) - int(b.value)
            page.update()
        if operation.value == '*':
            result.value = int(a.value) * int(b.value)
            page.update()
        if operation.value == '/':
            if int(b.value) == 0:
                print("here")
                status.value = "Invald Entry!"
            else:
                result.value = int(a.value) / int(b.value)
            page.update()



    page.add(
        ft.Row([
            a,
            operation,
            b,
            ft.ElevatedButton("=", on_click = calculator),
            result,
            status
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)