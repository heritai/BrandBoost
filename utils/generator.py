"""
Content generation utilities using Hugging Face Inference API.
"""

import os
import time
from typing import Dict, Any, Optional
from huggingface_hub import InferenceClient
import streamlit as st
try:
    from .prompt_templates import get_prompt_template, get_recommendations
except ImportError:
    from prompt_templates import get_prompt_template, get_recommendations


class ContentGenerator:
    """Main class for generating marketing content using Mistral 7B."""
    
    def __init__(self):
        """Initialize the content generator with Hugging Face client."""
        self.client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.1")
        self.generation_stats = {
            "total_generations": 0,
            "total_time_saved": 0,  # in minutes
            "total_cost_saved": 0   # in EUR
        }
    
    def generate_content(
        self, 
        product_data: Dict[str, Any], 
        content_type: str, 
        tone: str, 
        language: str = "English"
    ) -> Dict[str, Any]:
        """
        Generate marketing content for a product.
        
        Args:
            product_data: Dictionary containing product information
            content_type: Type of content to generate
            tone: Tone of voice for the content
            language: Language for the content (English/French)
        
        Returns:
            Dictionary containing generated content and metadata
        """
        try:
            # Get the appropriate prompt template
            prompt_template = get_prompt_template(content_type, tone, language)
            
            # Format the prompt with product data
            prompt = prompt_template.format(
                product_name=product_data["Product Name"],
                category=product_data["Category"],
                features=product_data["Features/Attributes"],
                target_audience=product_data["Target Audience"]
            )
            
            # Generate content using Mistral 7B
            start_time = time.time()
            
            with st.spinner("🤖 Generating content with AI..."):
                try:
                    response = self.client.text_generation(
                        prompt,
                        max_new_tokens=300,
                        temperature=0.7,
                        do_sample=True,
                        top_p=0.9
                    )
                except StopIteration:
                    # Fallback for when API returns empty response
                    response = self._generate_fallback_content(product_data, content_type, tone, language)
                except Exception as api_error:
                    st.warning(f"⚠️ API temporarily unavailable. Using fallback content generation.")
                    response = self._generate_fallback_content(product_data, content_type, tone, language)
            
            generation_time = time.time() - start_time
            
            # Update statistics
            self.generation_stats["total_generations"] += 1
            self.generation_stats["total_time_saved"] += 30  # Assume 30 minutes saved per generation
            self.generation_stats["total_cost_saved"] += 12  # Assume €12 saved per generation
            
            # Get recommendations
            recommendations = get_recommendations(content_type, tone)
            
            return {
                "content": response.strip(),
                "generation_time": generation_time,
                "recommendations": recommendations,
                "metadata": {
                    "product_name": product_data["Product Name"],
                    "content_type": content_type,
                    "tone": tone,
                    "language": language,
                    "timestamp": time.time()
                }
            }
            
        except Exception as e:
            st.error(f"❌ Error generating content: {str(e)}")
            return {
                "content": "Sorry, there was an error generating content. Please try again.",
                "generation_time": 0,
                "recommendations": "Please check your internet connection and try again.",
                "metadata": {
                    "product_name": product_data["Product Name"],
                    "content_type": content_type,
                    "tone": tone,
                    "language": language,
                    "timestamp": time.time(),
                    "error": str(e)
                }
            }
    
    def get_generation_stats(self) -> Dict[str, Any]:
        """Get current generation statistics."""
        return self.generation_stats.copy()
    
    def calculate_kpis(self) -> Dict[str, Any]:
        """Calculate key performance indicators."""
        stats = self.get_generation_stats()
        
        return {
            "time_saved_hours": round(stats["total_time_saved"] / 60, 1),
            "cost_saved_usd": stats["total_cost_saved"],
            "generations_count": stats["total_generations"],
            "avg_time_per_generation": round(stats["total_time_saved"] / max(stats["total_generations"], 1), 1)
        }
    
    def _generate_fallback_content(self, product_data: Dict[str, Any], content_type: str, tone: str, language: str) -> str:
        """
        Generate fallback content when API is unavailable.
        
        Args:
            product_data: Dictionary containing product information
            content_type: Type of content to generate
            tone: Tone of voice for the content
            language: Language for the content
        
        Returns:
            Fallback content string
        """
        product_name = product_data["Product Name"]
        category = product_data["Category"]
        features = product_data["Features/Attributes"]
        target_audience = product_data["Target Audience"]
        
        # Fallback content templates
        fallback_templates = {
            "Product Description": {
                "Professional": {
                    "English": f"Introducing {product_name}, a premium {category} designed for {target_audience}. This exceptional product features {features.replace(';', ', ')}. Experience the perfect blend of quality and innovation with {product_name}.",
                    "French": f"Présentation de {product_name}, un {category} premium conçu pour {target_audience}. Ce produit exceptionnel présente {features.replace(';', ', ')}. Découvrez le parfait équilibre entre qualité et innovation avec {product_name}."
                },
                "Playful": {
                    "English": f"🎉 Meet {product_name} - the {category} that's about to become your new obsession! Perfect for {target_audience}, it's packed with {features.replace(';', ', ')}. Get ready to fall in love! 💕",
                    "French": f"🎉 Rencontrez {product_name} - le {category} qui va devenir votre nouvelle obsession ! Parfait pour {target_audience}, il est rempli de {features.replace(';', ', ')}. Préparez-vous à tomber amoureux ! 💕"
                },
                "Luxury": {
                    "English": f"Indulge in the exquisite {product_name}, a distinguished {category} crafted for discerning {target_audience}. Featuring {features.replace(';', ', ')}, this masterpiece represents the pinnacle of luxury and sophistication.",
                    "French": f"Savourez l'exquis {product_name}, un {category} distingué conçu pour {target_audience} exigeants. Avec {features.replace(';', ', ')}, ce chef-d'œuvre représente le summum du luxe et de la sophistication."
                },
                "Casual": {
                    "English": f"Hey there! Check out {product_name} - it's a pretty cool {category} that {target_audience} are going to love. It's got {features.replace(';', ', ')} and honestly, it's just what you need.",
                    "French": f"Salut ! Découvrez {product_name} - c'est un {category} plutôt cool que {target_audience} vont adorer. Il a {features.replace(';', ', ')} et honnêtement, c'est exactement ce dont vous avez besoin."
                }
            },
            "Social Post": {
                "Professional": {
                    "English": f"Discover {product_name} - the {category} solution for {target_audience}. Features include {features.replace(';', ', ')}. #ProductLaunch #Innovation #Quality",
                    "French": f"Découvrez {product_name} - la solution {category} pour {target_audience}. Caractéristiques : {features.replace(';', ', ')}. #LancementProduit #Innovation #Qualité"
                },
                "Playful": {
                    "English": f"🚀 {product_name} is here and it's AMAZING! Perfect for {target_audience} who want {features.replace(';', ', ')}. Who's excited? 🙋‍♀️ #NewProduct #Excited #MustHave",
                    "French": f"🚀 {product_name} est là et c'est INCROYABLE ! Parfait pour {target_audience} qui veulent {features.replace(';', ', ')}. Qui est excité ? 🙋‍♀️ #NouveauProduit #Excité #Indispensable"
                },
                "Luxury": {
                    "English": f"Experience the epitome of luxury with {product_name}. This exclusive {category} offers {features.replace(';', ', ')} for the most discerning {target_audience}. #Luxury #Exclusive #Premium",
                    "French": f"Vivez l'épitomé du luxe avec {product_name}. Ce {category} exclusif offre {features.replace(';', ', ')} pour les {target_audience} les plus exigeants. #Luxe #Exclusif #Premium"
                },
                "Casual": {
                    "English": f"Just tried {product_name} and wow! 😍 Great {category} for {target_audience}. Love that it has {features.replace(';', ', ')}. Highly recommend! #Review #Recommendation",
                    "French": f"Je viens d'essayer {product_name} et wow ! 😍 Super {category} pour {target_audience}. J'adore qu'il ait {features.replace(';', ', ')}. Je recommande fortement ! #Avis #Recommandation"
                }
            },
            "Email": {
                "Professional": {
                    "English": f"Subject: Introducing {product_name} - The {category} Solution You've Been Waiting For\n\nDear Valued Customer,\n\nWe're excited to present {product_name}, a premium {category} designed specifically for {target_audience}. This innovative product features {features.replace(';', ', ')}.\n\nBest regards,\nThe BrandBoost Team",
                    "French": f"Objet : Présentation de {product_name} - La solution {category} que vous attendiez\n\nCher client,\n\nNous sommes ravis de vous présenter {product_name}, un {category} premium conçu spécifiquement pour {target_audience}. Ce produit innovant présente {features.replace(';', ', ')}.\n\nCordialement,\nL'équipe BrandBoost"
                },
                "Playful": {
                    "English": f"Subject: 🎉 {product_name} is HERE! (And it's amazing!)\n\nHey there!\n\nGuess what? {product_name} just dropped and it's everything {target_audience} have been dreaming of! With {features.replace(';', ', ')}, this {category} is about to change your life! 💫\n\nCheers,\nThe BrandBoost Squad",
                    "French": f"Objet : 🎉 {product_name} est LÀ ! (Et c'est incroyable !)\n\nSalut !\n\nDevine quoi ? {product_name} vient de sortir et c'est tout ce que {target_audience} rêvaient ! Avec {features.replace(';', ', ')}, ce {category} va changer votre vie ! 💫\n\nSalut,\nL'équipe BrandBoost"
                },
                "Luxury": {
                    "English": f"Subject: Exclusive Invitation: Discover {product_name}\n\nDear Esteemed Client,\n\nWe are honored to invite you to experience {product_name}, our most exclusive {category} offering. Crafted for the discerning {target_audience}, it embodies {features.replace(';', ', ')}.\n\nWarm regards,\nBrandBoost Luxury Division",
                    "French": f"Objet : Invitation exclusive : Découvrez {product_name}\n\nCher client estimé,\n\nNous avons l'honneur de vous inviter à découvrir {product_name}, notre offre {category} la plus exclusive. Conçu pour les {target_audience} exigeants, il incarne {features.replace(';', ', ')}.\n\nCordialement,\nDivision Luxe BrandBoost"
                },
                "Casual": {
                    "English": f"Subject: You'll love {product_name}!\n\nHi!\n\nJust wanted to share something cool with you - {product_name}! It's this awesome {category} that {target_audience} are totally into. The best part? It comes with {features.replace(';', ', ')}.\n\nTake care,\nThe BrandBoost Team",
                    "French": f"Objet : Vous allez adorer {product_name} !\n\nSalut !\n\nJe voulais juste partager quelque chose de cool avec toi - {product_name} ! C'est ce {category} génial que {target_audience} adorent. Le meilleur ? Il vient avec {features.replace(';', ', ')}.\n\nÀ bientôt,\nL'équipe BrandBoost"
                }
            }
        }
        
        return fallback_templates[content_type][tone][language]

    def export_content(self, content: str, filename: str = None) -> str:
        """
        Export generated content to a text file.
        
        Args:
            content: The content to export
            filename: Optional custom filename
        
        Returns:
            The filename of the exported file
        """
        if not filename:
            timestamp = int(time.time())
            filename = f"brandboost_content_{timestamp}.txt"
        
        # Ensure the reports directory exists
        os.makedirs("reports", exist_ok=True)
        
        filepath = os.path.join("reports", filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return filepath
        except Exception as e:
            st.error(f"❌ Error exporting content: {str(e)}")
            return None


def load_products(csv_path: str) -> list:
    """
    Load products from CSV file.
    
    Args:
        csv_path: Path to the products CSV file
    
    Returns:
        List of product dictionaries
    """
    import pandas as pd
    
    try:
        df = pd.read_csv(csv_path)
        return df.to_dict("records")
    except Exception as e:
        st.error(f"❌ Error loading products: {str(e)}")
        return []


def get_product_by_id(products: list, product_id: int) -> Optional[Dict[str, Any]]:
    """
    Get a specific product by its ID.
    
    Args:
        products: List of product dictionaries
        product_id: The ID of the product to find
    
    Returns:
        Product dictionary or None if not found
    """
    for product in products:
        if product["ProductID"] == product_id:
            return product
    return None
