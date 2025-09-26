"""
BrandBoost - AI-Powered Marketing Content Generator
Main Streamlit application for generating marketing content using Mistral 7B.
"""

import streamlit as st
import pandas as pd
import os
import sys
from datetime import datetime
import base64

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from generator import ContentGenerator, load_products, get_product_by_id
from visualization import (
    display_kpi_cards, 
    create_time_savings_chart, 
    create_content_type_distribution,
    create_tone_effectiveness_chart,
    display_insights_panel,
    create_roi_calculation,
    display_roi_metrics
)

# Page configuration
st.set_page_config(
    page_title="BrandBoost - AI Content Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark/light mode compatibility
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .kpi-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    
    .recommendation-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 0.5rem 0;
        color: #1565c0;
    }
    
    /* Dark mode styles */
    @media (prefers-color-scheme: dark) {
        
        .recommendation-box {
            background: #1a365d !important;
            color: #e2e8f0 !important;
            border-left-color: #2196f3;
        }
        
        .stSelectbox > div > div {
            background-color: #2d3748 !important;
            color: #e2e8f0 !important;
        }
        
        .stTextArea > div > div > textarea {
            background-color: #2d3748 !important;
            color: #e2e8f0 !important;
        }
        
        .stTextInput > div > div > input {
            background-color: #2d3748 !important;
            color: #e2e8f0 !important;
        }
        
        .stNumberInput > div > div > input {
            background-color: #2d3748 !important;
            color: #e2e8f0 !important;
        }
    }
    
    /* Light mode styles */
    @media (prefers-color-scheme: light) {
        .recommendation-box {
            background: #e3f2fd !important;
            color: #1565c0 !important;
        }
    }
    
    /* Force dark mode for Streamlit components */
    .stApp {
        color: var(--text-color);
    }
    
    .stSelectbox > div > div {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stTextArea > div > div > textarea {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stTextInput > div > div > input {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stNumberInput > div > div > input {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    /* Ensure text is readable in all modes */
    .stMarkdown {
        color: var(--text-color);
    }
    
    .stMetric {
        color: var(--text-color);
    }
    
    .stAlert {
        color: var(--text-color);
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables."""
    if 'generator' not in st.session_state:
        st.session_state.generator = ContentGenerator()
    
    if 'generated_content' not in st.session_state:
        st.session_state.generated_content = None
    
    if 'products' not in st.session_state:
        st.session_state.products = []

def load_product_data():
    """Load product data from CSV."""
    csv_path = "sample_data/products.csv"
    if os.path.exists(csv_path):
        st.session_state.products = load_products(csv_path)
    else:
        st.error("❌ Product data file not found. Please ensure sample_data/products.csv exists.")
        return False
    return True

def display_header():
    """Display the main header with value proposition."""
    st.markdown("""
    <div class="main-header">
        <h1>🚀 BrandBoost</h1>
        <h3>AI-Powered Marketing Content Generator</h3>
        <p>Generate high-quality marketing content in seconds, in English or French</p>
        <p><small>💡 Note: Uses AI when available, with intelligent fallback for reliable content generation</small></p>
    </div>
    """, unsafe_allow_html=True)

def display_sidebar():
    """Display sidebar with basic controls."""
    # Sidebar removed - all functionality moved to main content area
    return "English"  # Default language

def display_content_generator():
    """Display the main content generation interface."""
    st.markdown("## 📝 Content Generator")
    
    if not st.session_state.products:
        st.warning("⚠️ Please load product data first.")
        return
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Product selection
        product_options = {
            f"{product['Product Name']} ({product['Category']})": product['ProductID'] 
            for product in st.session_state.products
        }
        
        selected_product_name = st.selectbox(
            "🛍️ Select Product",
            options=list(product_options.keys()),
            help="Choose a product from the catalog"
        )
        
        selected_product_id = product_options[selected_product_name]
        selected_product = get_product_by_id(st.session_state.products, selected_product_id)
        
        if selected_product:
            # Display product details
            st.markdown("### Product Details")
            col_info1, col_info2 = st.columns(2)
            
            with col_info1:
                st.write(f"**Category:** {selected_product['Category']}")
                st.write(f"**Target Audience:** {selected_product['Target Audience']}")
            
            with col_info2:
                st.write(f"**Features:** {selected_product['Features/Attributes']}")
    
    with col2:
        # Content type selection
        content_type = st.selectbox(
            "📄 Content Type",
            ["Product Description", "Social Post", "Email"],
            help="Choose the type of content to generate"
        )
        
        # Tone selection
        tone = st.selectbox(
            "🎭 Tone",
            ["Professional", "Playful", "Luxury", "Casual"],
            help="Select the tone of voice for your content"
        )
        
        # Language selection
        language = st.selectbox(
            "🌍 Language",
            ["English", "French"],
            help="Language for the generated content"
        )
    
    # Generate button
        if st.button("🚀 Generate Content", type="primary", use_container_width=True):
            if selected_product:
                with st.spinner("🤖 AI is crafting your content..."):
                    result = st.session_state.generator.generate_content(
                        selected_product,
                        content_type,
                        tone,
                        language
                    )
                    st.session_state.generated_content = result
                    
                    # Show info if fallback was used
                    if "error" in result.get("metadata", {}):
                        st.info("ℹ️ Using fallback content generation due to API limitations. The content is still high-quality and ready to use!")
            else:
                st.error("❌ Please select a product first.")

def display_generated_content():
    """Display the generated content and controls."""
    if st.session_state.generated_content:
        content_data = st.session_state.generated_content
        
        st.markdown("## ✨ Generated Content")
        
        # Editable text area
        edited_content = st.text_area(
            "Generated Content (Editable)",
            value=content_data['content'],
            height=200,
            help="You can edit the generated content and copy it manually"
        )
        
        # Generation info
        st.write(f"⏱️ Generated in {content_data['generation_time']:.2f} seconds")
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💡 AI Recommendation")
        st.info(content_data['recommendations'])

def display_analytics():
    """Display analytics and insights."""
    if not st.session_state.products:
        return
    
    st.markdown("## 📊 Analytics & Insights")
    
    # Display KPIs at the top
    kpis = st.session_state.generator.calculate_kpis()
    display_kpi_cards(kpis)
    
    # ROI Analysis
    roi_data = create_roi_calculation(kpis)
    display_roi_metrics(roi_data)
    
    st.markdown("---")
    
    # Create tabs for different analytics views
    tab1, tab2, tab3 = st.tabs(["📈 Performance", "🎯 Content Strategy", "💡 Insights"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = create_time_savings_chart(kpis)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = create_content_type_distribution(st.session_state.products)
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        fig3 = create_tone_effectiveness_chart()
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab3:
        display_insights_panel()

def main():
    """Main application function."""
    # Initialize session state
    initialize_session_state()
    
    # Load product data
    if not load_product_data():
        return
    
    # Display header
    display_header()
    
    # Main content area
    tab1, tab2, tab3 = st.tabs(["🎯 Content Generator", "📊 Analytics", "ℹ️ About"])
    
    with tab1:
        display_content_generator()
        st.markdown("---")
        display_generated_content()
    
    with tab2:
        display_analytics()
    
    with tab3:
        st.markdown("""
        ## About BrandBoost
        
        **BrandBoost** is an AI-powered marketing content generator that helps e-commerce businesses 
        create consistent, high-quality marketing content across all channels.
        
        ### 🎯 Key Features
        - **Multi-format Content**: Generate product descriptions, social posts, and email content
        - **Multiple Tones**: Professional, Playful, Luxury, and Casual tones
        - **Bilingual Support**: English and French content generation
        - **AI-Powered**: Powered by Mistral 7B via Hugging Face
        - **Real-time Analytics**: Track performance and ROI
        
        ### 🚀 How It Works
        1. Select a product from your catalog
        2. Choose content type and tone
        3. Generate content with AI
        4. Edit and export as needed
        
        ### 📊 Business Impact
        - **Time Savings**: 25 minutes per content piece
        - **Cost Reduction**: 60% lower content creation costs (€33.67 saved per piece)
        - **Consistency**: Maintain brand voice across all channels
        - **Scalability**: Generate unlimited content variations
        
        ### 🔧 Technical Details
        - **AI Model**: Mistral-7B-Instruct-v0.1
        - **API**: Hugging Face Inference API
        - **Framework**: Streamlit
        - **Data**: Synthetic product catalog for demonstration
        
        ---
        
        **Disclaimer**: This is a demonstration project using synthetic data and the free 
        Hugging Face Inference API. For production use, consider implementing proper 
        authentication, rate limiting, and data validation.
        """)

if __name__ == "__main__":
    main()
