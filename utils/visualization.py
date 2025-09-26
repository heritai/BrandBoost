"""
Visualization utilities for KPIs and insights.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd


def display_kpi_cards(kpis: dict) -> None:
    """
    Display KPI cards in the main content area.
    
    Args:
        kpis: Dictionary containing KPI data
    """
    st.markdown("### 📊 Performance Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="⏱️ Time Saved",
            value=f"{kpis['time_saved_hours']}h",
            delta=f"+{kpis['avg_time_per_generation']}min avg"
        )
    
    with col2:
        st.metric(
            label="💰 Cost Saved",
            value=f"€{kpis['cost_saved_usd']}",
            delta="vs manual writing"
        )
    
    with col3:
        st.metric(
            label="📝 Content Generated",
            value=f"{kpis['generations_count']}",
            delta="pieces created"
        )


def create_time_savings_chart(kpis: dict) -> go.Figure:
    """
    Create a chart showing time savings over time.
    
    Args:
        kpis: Dictionary containing KPI data
    
    Returns:
        Plotly figure object
    """
    # Generate sample data for the last 7 days
    dates = [datetime.now() - timedelta(days=i) for i in range(6, -1, -1)]
    daily_savings = [kpis['time_saved_hours'] / 7] * 7  # Distribute evenly for demo
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=daily_savings,
        mode='lines+markers',
        name='Time Saved (Hours)',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="Daily Time Savings",
        xaxis_title="Date",
        yaxis_title="Hours Saved",
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig


def create_content_type_distribution(products: list) -> go.Figure:
    """
    Create a pie chart showing product category distribution.
    
    Args:
        products: List of product dictionaries
    
    Returns:
        Plotly figure object
    """
    if not products:
        return go.Figure()
    
    # Count products by category
    categories = [product['Category'] for product in products]
    category_counts = pd.Series(categories).value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=category_counts.index,
        values=category_counts.values,
        hole=0.3,
        textinfo='label+percent',
        textfont_size=12
    )])
    
    fig.update_layout(
        title="Product Categories",
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig


def create_tone_effectiveness_chart() -> go.Figure:
    """
    Create a chart showing tone effectiveness for different content types.
    
    Returns:
        Plotly figure object
    """
    # Sample data for tone effectiveness
    data = {
        'Content Type': ['Product Description', 'Social Post', 'Email', 'Product Description', 'Social Post', 'Email'],
        'Tone': ['Professional', 'Professional', 'Professional', 'Playful', 'Playful', 'Playful'],
        'Engagement Rate': [85, 78, 82, 92, 95, 88]
    }
    
    df = pd.DataFrame(data)
    
    fig = px.bar(
        df, 
        x='Content Type', 
        y='Engagement Rate', 
        color='Tone',
        title="Tone Effectiveness by Content Type",
        color_discrete_sequence=['#1f77b4', '#ff7f0e']
    )
    
    fig.update_layout(
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig


def display_insights_panel() -> None:
    """
    Display insights and recommendations panel.
    """
    st.markdown("### 💡 AI Insights & Recommendations")
    
    insights = [
        "🎯 **Content Strategy**: Playful tone increases social media engagement by 15%",
        "📈 **SEO Optimization**: Professional product descriptions improve search rankings",
        "💌 **Email Performance**: Casual tone has 23% higher open rates",
        "🏆 **Luxury Positioning**: Premium tone justifies 30% higher pricing",
        "⏰ **Time Efficiency**: AI generation saves 25 minutes per content piece",
        "💰 **Cost Savings**: Reduces content creation costs by 60%"
    ]
    
    for insight in insights:
        st.markdown(f"• {insight}")
    
    st.markdown("---")
    st.markdown("### 🚀 Best Practices")
    
    best_practices = [
        "**Product Descriptions**: Use professional tone for e-commerce, playful for lifestyle",
        "**Social Posts**: Mix tones based on platform - professional for LinkedIn, playful for Instagram",
        "**Email Campaigns**: Match tone to audience - luxury for premium customers, casual for general audience",
        "**A/B Testing**: Test different tones to find what works best for your audience",
        "**Consistency**: Maintain consistent tone across all content for the same product"
    ]
    
    for practice in best_practices:
        st.markdown(practice)


def create_roi_calculation(kpis: dict) -> dict:
    """
    Calculate ROI metrics for the content generation system.
    
    Args:
        kpis: Dictionary containing KPI data
    
    Returns:
        Dictionary containing ROI calculations
    """
    # Assumptions for ROI calculation
    hourly_writer_rate = 45  # EUR per hour
    ai_cost_per_generation = 0.08  # EUR per generation
    
    time_saved_hours = kpis['time_saved_hours']
    generations = kpis['generations_count']
    
    # Calculate savings
    manual_cost = time_saved_hours * hourly_writer_rate
    ai_cost = generations * ai_cost_per_generation
    net_savings = manual_cost - ai_cost
    
    # Calculate ROI
    roi_percentage = (net_savings / max(ai_cost, 1)) * 100
    
    return {
        "manual_cost": manual_cost,
        "ai_cost": ai_cost,
        "net_savings": net_savings,
        "roi_percentage": roi_percentage,
        "cost_per_content": ai_cost_per_generation
    }


def display_roi_metrics(roi_data: dict) -> None:
    """
    Display ROI metrics in a visually appealing way.
    
    Args:
        roi_data: Dictionary containing ROI calculations
    """
    st.markdown("### 💰 ROI Analysis")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Manual Writing Cost",
            value=f"€{roi_data['manual_cost']:.0f}",
            help="Cost if content was written manually"
        )
    
    with col2:
        st.metric(
            label="AI Generation Cost",
            value=f"€{roi_data['ai_cost']:.2f}",
            help="Actual cost using AI generation"
        )
    
    with col3:
        st.metric(
            label="Net Savings",
            value=f"€{roi_data['net_savings']:.0f}",
            delta=f"{roi_data['roi_percentage']:.0f}% ROI",
            help="Total savings achieved"
        )
    
    with col4:
        st.metric(
            label="Cost per Content",
            value=f"€{roi_data['cost_per_content']:.2f}",
            help="Average cost per generated content piece"
        )
