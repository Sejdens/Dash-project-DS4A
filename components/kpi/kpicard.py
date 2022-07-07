from dash import html

class kpicard:
    def __init__(self, title, number, icon, id):
        self.title = title
        self.number = number
        self.id = id
        self.icon = f"/assets/{icon}"

    def display(self):
        layout = html.Div(
            [
                html.P(self.title, className="kpi__title"),
                html.Div(
                    [
                        html.P(id = self.id, children=self.number, className="kpi__number"),
                        html.Img(src=self.icon, className="kpi__icon"),
                    ],
                    className="kpi__div",
                )
            ],
            className = "my-4 mx-auto kpicard",
        )
        return layout
