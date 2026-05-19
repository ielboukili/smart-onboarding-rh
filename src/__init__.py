  """
smart-onboarding-rh - Assistant d'onboarding RH intelligent.
"""

__version__ = "0.1.0"

from .assistant import OnboardingAssistant, AssistantResponse, answer_question
from .query_parser import QueryParser
from .faq_search import FAQSearcher, FAQItem
from .resume_parser import ResumeParser, ResumeData

__all__ = [
    "OnboardingAssistant",
    "AssistantResponse",
    "answer_question",
    "QueryParser",
    "FAQSearcher",
    "FAQItem",
    "ResumeParser",
    "ResumeData",
]
