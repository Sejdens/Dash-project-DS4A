import dash_bootstrap_components as dbc
from dash import html


class photocard:
    def __init__(self, img, title, description):
        self.img = f"/assets/{img}"
        self.title = title
        self.description = description


    def display(self):
        layout = dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                src=self.img,
                                className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4(self.title, className="card-title"),
                                    html.P(
                                        self.description,
                                        className="card-text",
                                    ),
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
            className="mb-3",
            style={"maxWidth": "540px"},
        )
        return layout
