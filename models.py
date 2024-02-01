from typing import Optional, List, Dict, Text, Union
from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Literal
from datetime import datetime

class Abonnent(BaseModel):
    """
    Datenmodell für die Abonnementverwaltung
    """
    untnr: Optional[str] = Field(title=u"Unternehmensnummer")
    vorname : str = Field(title=u"Vorname des Verantwortlichen für die Applikation")
    name : str = Field(title=u"Name des Verantwortlichen für die Applikation")
    email : EmailStr = Field(title=u"Versandadresse: E-Mail-Adresse")
    strhnr : Optional[str] = Field(title=u"Versandadresse: Straße und Hausnummer")
    plz : Optional[str] = Field(title=u"Versandadresse: Postleitzahl")
    ort : Optional[str] = Field(title=u"Versandadresse: Ort")
    medien : dict = Field(title="Dictionary mit Angabe zu medien")
    refresh : datetime = Field(title="Datum der letzten Aktualisierung")
