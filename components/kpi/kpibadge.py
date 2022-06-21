from dash import html
import dash_bootstrap_components as dbc

class kpibadge:
  def __init__(self, kpi, label, badgetype):
    self.kpi = kpi
    self.label = label
    self.badgetype = badgetype
    if badgetype == "Dange":
      self.color = "danger"
    else:
      self.color = "success"

    def display(self):
      layout = html.Div(
        [
          ["yey"],
        ],
        className = "m-2",
      )
      return layout


