from fastapi import FastAPI, HTTPException
from models import Abonnent

app = FastAPI(
    title="OpenAPI der Trainings-Session",
    description="OpenAPI Services für die Abonnentenverwaltung",
    version="0.9btn (better than nothing)",
)

@app.get("/")
def welcome():
    return "BGETEM Abonnentenverwaltung"

@app.post("/{api_version}/abo", response_model=Abonnent)
def send_abonnement(api_version:str, data:Abonnent):
    """
    """
    if api_version == '0.9btn':
        print(data.email)
        return data #Wir geben das Request-Model als Datenmodell zurück
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")
