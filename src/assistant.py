"""
Module principal de l'assistant d'onboarding RH.
Orchestre les differentes fonctions de l'assistant.
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from rich.console import Console
from rich.panel import Panel

from .faq_search import FAQSearcher, FAQItem
from .query_parser import QueryParser
from .resume_parser import ResumeParser

load_dotenv()

console = Console()


class AssistantResponse(BaseModel):
    message: str
    intent: str
    suggestions: List[str] = Field(default_factory=list)
    faq_matches: List[FAQItem] = Field(default_factory=list)
    resume_insight: Optional[Dict] = None


class OnboardingAssistant:
    def __init__(self, faq_path: str = "data/onboarding_faq.json"):
        self.faq_searcher = FAQSearcher(faq_path)
        self.query_parser = QueryParser()
        self.resume_parser = ResumeParser()

    def process_query(self, query: str) -> AssistantResponse:
        parsed = self.query_parser.parse(query)
        intent = parsed["intent"]

        if intent == "faq":
            matches = self.faq_searcher.search(parsed["keywords"])
            if matches:
                return AssistantResponse(
                    message="Voici les reponses pertinentes a votre question:",
                    intent="faq",
                    faq_matches=matches,
                    suggestions=self._get_followup_suggestions(intent)
                )
            return AssistantResponse(
                message="Aucune question similaire trouvee dans la base.",
                intent="faq",
                suggestions=["Posez votre question autrement"]
            )

        elif intent == "resume":
            return AssistantResponse(
                message="Fonctionnalite de parsing de CV non encore activee.",
                intent="resume",
                suggestions=["Upload votre CV pour l'analyzer"]
            )

        else:
            return AssistantResponse(
                message="Je n'ai pas compris votre demande.",
                intent="unknown",
                suggestions=["Question sur l'onboarding?", "Besoin d'infos RH?"]
            )

    def _get_followup_suggestions(self, intent: str) -> List[str]:
        suggestions = {
            "faq": ["Informations sur les conges?", "Procedure de teletravail?"],
            "resume": ["Quels documents sont requis?"],
            "unknown": ["Parlez-moi de l'onboarding", "Comment fonctionne cet outil?"]
        }
        return suggestions.get(intent, [])

    def display_response(self, response: AssistantResponse) -> None:
        console.print(Panel(response.message, title="Assistant RH"))
        for faq in response.faq_matches:
            console.print(f"Q: {faq.question}")
            console.print(f"A: {faq.answer}")
            console.print(f"Categorie: {faq.category}")
            console.print("")
        if response.suggestions:
            console.print("Suggestions:", style="bold blue")
            for s in response.suggestions:
                console.print(f"  - {s}")
