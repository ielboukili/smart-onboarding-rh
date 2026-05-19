  """
Module d'analyse et de parsing de CV.
Version simplifiee pour le prototype.
"""

import re
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class ResumeData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    experience_years: Optional[int] = None
    education: List[str] = Field(default_factory=list)
    position_applied: Optional[str] = None


class ResumeParser:
    EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    PHONE_PATTERN = r"(?:\+33|0)[1-9](?:[\s.-]?\d{2}){4}"

    def parse(self, text: str) -> Dict:
        data = {
            "name": self._extract_name(text),
            "email": self._extract_email(text),
            "phone": self._extract_phone(text),
            "skills": self._extract_skills(text),
            "experience_years": self._extract_experience(text),
            "education": self._extract_education(text),
            "position_applied": self._extract_position(text)
        }
        return data

    def _extract_email(self, text: str) -> Optional[str]:
        match = re.search(self.EMAIL_PATTERN, text)
        return match.group(0) if match else None

    def _extract_phone(self, text: str) -> Optional[str]:
        match = re.search(self.PHONE_PATTERN, text)
        return match.group(0) if match else None

    def _extract_skills(self, text: str) -> List[str]:
        keywords = ["python", "java", "javascript", "sql", "docker", "kubernetes", "aws", "azure", "gcp", "git", "agile", "scrum", "react", "vue", "node", "typescript"]
        found = [kw for kw in keywords if kw in text.lower()]
        return found

    def _extract_experience(self, text: str) -> Optional[int]:
        match = re.search(r"(\d+)\s*(?:ans?|annees?)", text.lower())
        return int(match.group(1)) if match else None

    def _extract_name(self, text: str) -> Optional[str]:
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        if lines:
            first_line = lines[0].replace("CV", "").replace("CURRICULUM", "").strip()
            return first_line if len(first_line) < 50 else None
        return None

    def _extract_education(self, text: str) -> List[str]:
        schools = []
        for match in re.finditer(r"(?:diplome|licence|master|ingenieur).*?(?:en|de)\s*([A-Za-z\s]+?)(?:\n|$)", text.lower()):
            schools.append(match.group(0).strip())
        return schools[:5]

    def _extract_position(self, text: str) -> Optional[str]:
        match = re.search(r"(?:poste|fonction|objectif).*?:?\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
        return match.group(1).strip() if match else None
