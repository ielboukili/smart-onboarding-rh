"""
Module d'extraction de l'intention et des mots-clés.
Version simplifiée (augmentable avec LLM)."""

import re
from typing import Dict, List


class QueryParser:
    INTENT_PATTERNS = {
        "faq": [r"(quoi|comment|quel|pourquoi|où|quand)", r"(conge|teletravail|mutuelle|salaire|pause)", r"(onboarding|arrival|integration)"],
        "resume": [r"(cv|resume|parcours|experience|competence)", r"(upload|envoyer|deposer)"]
    }

    STOP_WORDS = {"je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles", "le", "la", "les", "un", "une", "des", "du", "de", "a", "et", "ou", "est", "sont", "ce", "cette", "mon", "ma", "mes"}

    def parse(self, query: str) -> Dict:
        query_lower = query.lower()
        intent = self._detect_intent(query_lower)
        keywords = self._extract_keywords(query)
        return {"intent": intent, "keywords": keywords, "original": query}

    def _detect_intent(self, query: str) -> str:
        for intent, patterns in self.INTENT_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, query, re.IGNORECASE):
                    return intent
        return "unknown"

    def _extract_keywords(self, query: str) -> List[str]:
        words = re.findall(r"\w+", query.lower())
        return [w for w in words if w not in self.STOP_WORDS and len(w) > 2]
