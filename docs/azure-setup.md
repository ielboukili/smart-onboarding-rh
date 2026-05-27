# Azure OpenAI — Approche technique et choix d'architecture

## Pourquoi Azure OpenAI ?

Dans le projet Smart Onboarding RH, le choix d'Azure OpenAI plutôt que l'API OpenAI directe repose sur trois critères :

- **Souveraineté des données** : les données RH traitées restent hébergées en Europe (région France Central / West Europe), conformément au RGPD.
- **Conformité entreprise** : Azure OpenAI s'intègre dans un cadre de sécurité maîtrisé (RBAC, VNet, clés gérées par le client).
- **Évolutivité** : le endpoint Azure permet de switcher de modèle (GPT-4o, GPT-4-turbo) sans changer l'architecture applicative.

## Stack Azure utilisée

| Service | Usage dans le projet |
|---|---|
| **Azure OpenAI Service** | Génération de synthèses candidats via GPT-4o |
| **Azure AI Studio** | Configuration des deployments et tests playground |
| **Azure Resource Group** | Isolation et gouvernance des ressources |

## Intégration dans le workflow n8n

Le workflow n8n appelle Azure OpenAI via un nœud HTTP Request configuré avec :

- `endpoint` : URL du deployment Azure OpenAI
- `api-key` : clé stockée en variable d'environnement (jamais en clair)
- `model` : `gpt-4o` (deployment personnalisé)
- `prompt` : template structuré pour la synthèse RH

## Exemple de prompt utilisé

```
Tu es un assistant RH. À partir des informations suivantes sur un candidat,
génère une synthèse structurée en 5 points : profil, disponibilité,
compétences clés, points d'attention, recommandation.

Candidat : {{nom}} | Poste visé : {{poste}} | Expérience : {{experience}}
```

## Bonnes pratiques appliquées

- Variables d'environnement pour toutes les clés API (`.env` non versionné)
- Aucune donnée personnelle réelle dans le dépôt (conformité RGPD)
- Logs d'appels conservés dans Airtable pour traçabilité
- Quota et rate limiting gérés côté n8n (retry automatique)

## Références

- [Azure OpenAI Documentation](https://learn.microsoft.com/fr-fr/azure/ai-services/openai/)
- [Azure AI Studio](https://ai.azure.com)
- [RGPD et Azure](https://azure.microsoft.com/fr-fr/explore/trusted-cloud/privacy/)
