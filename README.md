# Smart Onboarding RH

Prototype d'automatisation RH centré sur l'orchestration de workflows avec n8n, la synthèse de contenu avec Azure OpenAI, la gestion des données avec Airtable, le suivi opérationnel avec Jira, et les notifications avec Slack/Gmail.

## Contexte

Les processus d'onboarding RH impliquent souvent plusieurs outils, des relances manuelles et une visibilité partielle sur l'avancement.
Ce projet illustre une approche structurée pour centraliser ces étapes dans un workflow simple, lisible et évolutif — en intégrant l'IA générative comme levier opérationnel, et non comme gadget.

## Objectif

Montrer comment un flux RH peut être automatisé de bout en bout :
- collecte et qualification des informations,
- transformation et nettoyage des données (ETL),
- synthèse assistée par IA,
- suivi opérationnel,
- notifications automatisées,
- documentation et traçabilité.

## Stack

| Outil | Rôle |
|-------|------|
| **n8n** | Orchestration des workflows bout en bout |
| **Azure OpenAI** | Génération de synthèses IA — choix souverain, données hébergées en Europe |
| **Airtable** | Base de données opérationnelle et gestion des candidats |
| **ETL / dbt** | Transformation, nettoyage et structuration des données avant traitement IA |
| **Jira** | Suivi Kanban, pilotage des cas et traçabilité Agile |
| **Slack** | Notifications d'équipe en temps réel |
| **Gmail** | Relances automatisées J+2 / J+5 |
| **Notion** | Documentation interne et consignes opérationnelles |

## Workflow

1. Un candidat remplit un formulaire d'entrée.
2. Les données sont stockées et structurées dans Airtable (ETL).
3. n8n déclenche le workflow d'orchestration.
4. Azure OpenAI génère une synthèse utile au traitement du dossier.
5. Jira met à jour le suivi Kanban du cas.
6. Slack et Gmail envoient les alertes et relances automatiques.
7. Notion conserve la documentation et les consignes internes.

📐 Voir le schéma d'architecture dans [ARCHITECTURE.md](https://www.perplexity.ai/search/ARCHITECTURE.md)

## Ce que ce projet démontre

- Compréhension d'un besoin métier RH terrain.
- Capacité à structurer un workflow multi-outils orienté valeur.
- Usage pertinent de l'IA générative dans un contexte opérationnel réel.
- Gouvernance des données, traçabilité et conformité RGPD dans un contexte multi-outils.
- Maîtrise des pratiques Agile/Scrum pour le pilotage et la livraison.

## Pourquoi Azure OpenAI plutôt qu'OpenAI direct ?

Azure OpenAI garantit que les données restent hébergées en Europe, dans un environnement conforme RGPD — critère essentiel pour tout traitement de données RH sensibles. C'est également l'approche adoptée par les acteurs souverains du marché pour éviter le Shadow AI.

## Limites

Ce dépôt documente un prototype et une architecture de référence.
Il ne publie ni données sensibles, ni workflows réels de production, conformément aux contraintes de confidentialité client et de conformité RGPD.

## Utilisation

Ce projet sert de démonstrateur pour :

- un entretien technique ou fonctionnel,
- un portfolio GitHub orienté Data & IA,
- une présentation de cas d'usage d'automatisation opérationnelle,
- une discussion sur l'intégration IA générative dans les processus métier.

## Licence

MIT.
