"""
Prompt templates for different content types and tones.
"""

def get_prompt_template(content_type: str, tone: str, language: str = "English") -> str:
    """
    Get the appropriate prompt template based on content type, tone, and language.
    
    Args:
        content_type: Type of content (Product Description, Social Post, Email)
        tone: Tone of voice (Professional, Playful, Luxury, Casual)
        language: Language (English or French)
    
    Returns:
        Formatted prompt template string
    """
    
    # Base templates for different content types
    templates = {
        "Product Description": {
            "Professional": {
                "English": """Write a professional product description for {product_name} in the {category} category. 
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Professional, informative tone
                - Highlight key features and benefits
                - Include SEO-friendly keywords
                - 150-200 words
                - Focus on value proposition and quality""",
                
                "French": """Écrivez une description de produit professionnelle pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton professionnel et informatif
                - Mettre en avant les caractéristiques et avantages clés
                - Inclure des mots-clés SEO
                - 150-200 mots
                - Se concentrer sur la proposition de valeur et la qualité"""
            },
            
            "Playful": {
                "English": """Write a playful and engaging product description for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Fun, energetic tone with personality
                - Use creative language and emojis
                - Make it shareable and memorable
                - 120-180 words
                - Focus on excitement and user experience""",
                
                "French": """Écrivez une description de produit ludique et engageante pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton amusant et énergique avec de la personnalité
                - Utiliser un langage créatif et des emojis
                - Rendre partageable et mémorable
                - 120-180 mots
                - Se concentrer sur l'excitation et l'expérience utilisateur"""
            },
            
            "Luxury": {
                "English": """Write a sophisticated luxury product description for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Elegant, premium tone
                - Emphasize exclusivity and craftsmanship
                - Use refined vocabulary
                - 180-220 words
                - Focus on quality, prestige, and sophistication""",
                
                "French": """Écrivez une description de produit de luxe sophistiquée pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton élégant et premium
                - Souligner l'exclusivité et l'artisanat
                - Utiliser un vocabulaire raffiné
                - 180-220 mots
                - Se concentrer sur la qualité, le prestige et la sophistication"""
            },
            
            "Casual": {
                "English": """Write a casual, friendly product description for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Conversational, approachable tone
                - Use everyday language
                - Be relatable and down-to-earth
                - 130-170 words
                - Focus on practical benefits and ease of use""",
                
                "French": """Écrivez une description de produit décontractée et amicale pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton conversationnel et accessible
                - Utiliser un langage quotidien
                - Être relatable et terre-à-terre
                - 130-170 mots
                - Se concentrer sur les avantages pratiques et la facilité d'utilisation"""
            }
        },
        
        "Social Post": {
            "Professional": {
                "English": """Create a professional social media post for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Professional yet engaging tone
                - Include relevant hashtags
                - Call-to-action
                - 100-150 words
                - Platform-agnostic (works for LinkedIn, Facebook, Twitter)""",
                
                "French": """Créez un post de médias sociaux professionnel pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton professionnel mais engageant
                - Inclure des hashtags pertinents
                - Appel à l'action
                - 100-150 mots
                - Indépendant de la plateforme (fonctionne pour LinkedIn, Facebook, Twitter)"""
            },
            
            "Playful": {
                "English": """Create a fun, engaging social media post for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Playful, energetic tone with emojis
                - Creative hashtags
                - Strong call-to-action
                - 80-120 words
                - Highly shareable content""",
                
                "French": """Créez un post de médias sociaux amusant et engageant pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton ludique et énergique avec des emojis
                - Hashtags créatifs
                - Appel à l'action fort
                - 80-120 mots
                - Contenu hautement partageable"""
            },
            
            "Luxury": {
                "English": """Create a sophisticated luxury social media post for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Elegant, aspirational tone
                - Premium hashtags
                - Exclusive feel
                - 100-140 words
                - Focus on exclusivity and quality""",
                
                "French": """Créez un post de médias sociaux de luxe sophistiqué pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton élégant et inspirant
                - Hashtags premium
                - Sentiment d'exclusivité
                - 100-140 mots
                - Se concentrer sur l'exclusivité et la qualité"""
            },
            
            "Casual": {
                "English": """Create a casual, relatable social media post for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Conversational, friendly tone
                - Relatable hashtags
                - Easy-going call-to-action
                - 90-130 words
                - Authentic and approachable""",
                
                "French": """Créez un post de médias sociaux décontracté et relatable pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton conversationnel et amical
                - Hashtags relatables
                - Appel à l'action décontracté
                - 90-130 mots
                - Authentique et accessible"""
            }
        },
        
        "Email": {
            "Professional": {
                "English": """Write a professional email marketing content for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Professional, trustworthy tone
                - Clear subject line suggestion
                - Compelling body content
                - Strong call-to-action
                - 200-300 words
                - Focus on benefits and value""",
                
                "French": """Écrivez un contenu d'email marketing professionnel pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton professionnel et digne de confiance
                - Suggestion d'objet claire
                - Contenu de corps convaincant
                - Appel à l'action fort
                - 200-300 mots
                - Se concentrer sur les avantages et la valeur"""
            },
            
            "Playful": {
                "English": """Write a fun, engaging email marketing content for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Energetic, fun tone
                - Creative subject line
                - Engaging storytelling
                - Exciting call-to-action
                - 180-250 words
                - Focus on excitement and engagement""",
                
                "French": """Écrivez un contenu d'email marketing amusant et engageant pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton énergique et amusant
                - Objet créatif
                - Storytelling engageant
                - Appel à l'action excitant
                - 180-250 mots
                - Se concentrer sur l'excitation et l'engagement"""
            },
            
            "Luxury": {
                "English": """Write a sophisticated luxury email marketing content for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Elegant, premium tone
                - Exclusive subject line
                - Sophisticated language
                - Refined call-to-action
                - 220-320 words
                - Focus on exclusivity and prestige""",
                
                "French": """Écrivez un contenu d'email marketing de luxe sophistiqué pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton élégant et premium
                - Objet exclusif
                - Langage sophistiqué
                - Appel à l'action raffiné
                - 220-320 mots
                - Se concentrer sur l'exclusivité et le prestige"""
            },
            
            "Casual": {
                "English": """Write a casual, friendly email marketing content for {product_name} in the {category} category.
                Key features: {features}
                Target audience: {target_audience}
                
                Requirements:
                - Conversational, approachable tone
                - Friendly subject line
                - Personal touch
                - Easy-going call-to-action
                - 190-280 words
                - Focus on relatability and ease""",
                
                "French": """Écrivez un contenu d'email marketing décontracté et amical pour {product_name} dans la catégorie {category}.
                Caractéristiques clés: {features}
                Public cible: {target_audience}
                
                Exigences:
                - Ton conversationnel et accessible
                - Objet amical
                - Touche personnelle
                - Appel à l'action décontracté
                - 190-280 mots
                - Se concentrer sur la relatabilité et la facilité"""
            }
        }
    }
    
    return templates[content_type][tone][language]


def get_recommendations(content_type: str, tone: str) -> str:
    """
    Get recommendations based on content type and tone selection.
    
    Args:
        content_type: Type of content selected
        tone: Tone selected
    
    Returns:
        Recommendation string
    """
    recommendations = {
        "Product Description": {
            "Professional": "Professional tone is recommended for product pages to boost SEO and build credibility with customers.",
            "Playful": "Playful tone works great for lifestyle products and social media integration to increase engagement.",
            "Luxury": "Luxury tone is perfect for premium products to justify higher prices and attract affluent customers.",
            "Casual": "Casual tone helps make products more approachable and relatable to everyday consumers."
        },
        "Social Post": {
            "Professional": "Professional tone is ideal for LinkedIn and B2B platforms to maintain brand authority.",
            "Playful": "Playful tone is best for social media campaigns to increase engagement and shareability.",
            "Luxury": "Luxury tone creates aspirational content that drives premium brand perception.",
            "Casual": "Casual tone builds authentic connections and encourages user-generated content."
        },
        "Email": {
            "Professional": "Professional tone builds trust and is perfect for transactional and informational emails.",
            "Playful": "Playful tone increases open rates and engagement in promotional campaigns.",
            "Luxury": "Luxury tone creates exclusivity and drives high-value customer actions.",
            "Casual": "Casual tone improves deliverability and creates personal connections with subscribers."
        }
    }
    
    return recommendations[content_type][tone]
