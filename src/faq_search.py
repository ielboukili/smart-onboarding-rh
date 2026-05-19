"""
Module de recherche semantique dans la FAQ.
Utilise des embeddings sentence-transformers et faiss.
"""

import json
import os
from typing import List, Optional
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class FAQItem(BaseModel):
    question: str
    answer: str
    category: str
    tags: List[str] = []


class FAQSearcher:
    def __init__(self, faq_path: str):
        self.faq_path = faq_path
        self.faqs: List[FAQItem] = []
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index: Optional[faiss.IndexFlatL2] = None
        self._load_faq()
        self._build_index()

    def _load_faq(self):
        with open(self.faq_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.faqs = [FAQItem(**item) for item in data["faq"]]

    def _build_index(self):
        questions = [faq.question for faq in self.faqs]
        embeddings = self.model.encode(questions, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def search(self, keywords: List[str], top_k: int = 3) -> List[FAQItem]:
        query = " ".join(keywords)
        query_vec = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vec, k=top_k)
        results = []
        for idx in indices[0]:
            if idx < len(self.faqs):
                results.append(self.faqs[idx])
        return results

    def search_by_category(self, category: str) -> List[FAQItem]:
        return [faq for faq in self.faqs if faq.category == category]

    def get_categories(self) -> List[str]:
        return list(set(faq.category for faq in self.faqs))
