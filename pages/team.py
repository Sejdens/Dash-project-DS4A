import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.cards.photocard import photocard

register_page(__name__, path="/team")

david = photocard("david.jpeg", "David Alexander Patarroyo Aponte",
                  "Systems Engineer, MBA, Specialist in BI.")

diana = photocard("diana.jpeg", "Diana Aribel Guzmán",
                  "I am from Cali. I am a proactive and goal-oriented Industrial Engineer. I have been working for the last 5 years in multi-professional environments in the pharmaceutical industry. I love to learn, so I am a passionate for reading.")

edgar = photocard("edgar.jpeg", "Edgar Dario Monsalve",
                  "I am from Arauca, I am a Statistician, I have experience as a data scientist and business analyst in fraud prevention in the financial sector, my greatest hobbies are riding a bicycle and watching formula 1")

jenny = photocard("jenny.jpeg", "Jenny",
                  "Economist and political scientist. Experienced in data analysis on conflict, security and migration issues.")

moises = photocard("moises.jpg", "Moisés Herrera",
                  "Musician, Language Activist and Web Developer, passionate about Open Source and Education.")

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            david.display(),
            diana.display(),
            edgar.display(),
            jenny.display(),
            moises.display(),
        ],
        className="d-flex flex-wrap justify-content-center",
        ),
    ]),
], fluid=True)
