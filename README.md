# Smart Onboarding RH

Prototype d'automatisation RH centré sur l'orchestration de workflows avec n8n, la synthèse de contenu avec Azure OpenAI, la gestion des données avec Airtable, le suivi opérationnel avec Jira, et les notifications avec Slack/Gmail.

## Contexte

Les processus d'onboarding RH impliquent souvent plusieurs outils, des relances manuelles et une visibilité partielle sur l'avancement.
Ce projet illustre une approche structurée pour centraliser ces étapes dans un workflow simple, lisible et évolutif.

## Objectif

Montrer comment un flux RH peut être automatisé de bout en bout :
- collecte des informations,
- qualification,
- synthèse assistée par IA,
- suivi opérationnel,
- notifications,
- documentation.

## Stack

- **n8n** : orchestration des workflows.
- **Azure OpenAI** : génération de synthèses et reformulations assistées par IA.
- **Airtable** : base de données opérationnelle.
- **Jira** : suivi Kanban et pilotage des cas.
- **Slack** : notifications d'équipe.
- **Gmail** : relances automatisées.
- **Notion** : documentation interne.

## Workflow

1. Un candidat ou un utilisateur remplit un formulaire.
2. Les données sont stockées dans Airtable.
3. n8n déclenche le workflow.
4. Azure OpenAI génère une synthèse utile au traitement.
5. Jira met à jour le suivi.
6. Slack et Gmail envoient les alertes et relances.
7. Notion conserve la documentation et les consignes internes.

## Ce que ce projet démontre

- Compréhension d'un besoin métier RH.
- Capacité à structurer un workflow multi-outils.
- Usage pertinent de l'IA dans un contexte opérationnel.
- Vision claire des enjeux de traçabilité, d'automatisation et de gouvernance.

## Limites

Ce dépôt documente un prototype et une architecture de référence.
Il ne publie ni données sensibles, ni workflows réels de production.

## Utilisation

Ce projet sert de démonstrateur pour :
- un entretien,
- un portfolio GitHub,
- une présentation de cas d'usage Data & IA,
- une discussion sur l'automatisation RH.

## Licence

MIT.
