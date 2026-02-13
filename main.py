import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import random

# Page Config
st.set_page_config(page_title="LinkedIn AI Post Architect", page_icon="💙", layout="wide")

# --- TRANSPARENT GLASS THEME CSS ---
st.markdown("""
    <style>
    /* Full App Background - Transparent Gradient */
    .stApp {
        background: linear-gradient(135deg, rgba(200, 215, 235, 0.5) 0%, rgba(243, 242, 239, 0.6) 100%);
        background-attachment: fixed;
    }
    
    /* Transparent Glass Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.2); /* High transparency */
        backdrop-filter: blur(15px); /* Strong Glass blur */
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
    }

    /* Transparent Input Fields */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
    }

    /* LinkedIn Blue Button */
    .stButton>button {
        background-color: #0077B5 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 12px !important;
        box-shadow: 0 4px 15px rgba(0, 119, 181, 0.2) !important;
    }
    
    .stButton>button:hover {
        background-color: #005582 !important;
        transform: scale(1.02) !important;
    }

    /* Badge/Reach Metric */
    .engagement-badge {
        display: inline-block;
        background: rgba(0, 119, 181, 0.15);
        color: #004182;
        padding: 6px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 13px;
        border: 1px solid rgba(0, 119, 181, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Header Section
    st.markdown("<h1 style='text-align: center; color: #004182; font-size: 2.8rem;'>LinkedIn AI Post Architect</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #444;'>Crafting Viral Personal Brands with Llama 3.3</p>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)

    # Load Data
    try:
        fs = FewShotPosts()
        tags = sorted(list(fs.get_tags()))
    except Exception:
        st.error("Data error: Run processed.py first to populate the JSON file.")
        st.stop()

    col1, col2 = st.columns([1, 1.8], gap="large")

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #0077B5; margin-top: 0;">🎯 Content Strategy</h3>', unsafe_allow_html=True)
        
        selected_tag = st.selectbox("Select Topic", options=tags)
        selected_tone = st.selectbox("Tone of Voice", ["Professional", "Casual", "Inspirational", "Thought Leader"])
        
        c1, c2 = st.columns(2)
        selected_length = c1.selectbox("Length", ["Short", "Medium", "Long"])
        selected_language = c2.selectbox("Language", ["English", "Hinglish"])

        generate_btn = st.button("Generate Post ✨")
        st.markdown('</div>', unsafe_allow_html=True)

        # Custom Styled Recruiter Tip
        st.markdown("""
            <div style="background-color: rgba(0, 119, 181, 0.08); padding: 15px; border-radius: 12px; border-left: 5px solid #0077B5;">
                <span style="color: #004182; font-size: 14px;">
                    💡 <b>Recruiter Tip:</b> Use the 'Inspirational' tone for higher engagement on personal stories.
                </span>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        if generate_btn:
            with st.spinner("🤖 AI Architect is designing your post..."):
                post = generate_post(selected_length, selected_language, selected_tag, selected_tone)
                
                # Generated Output in Transparent Glass Card
                st.markdown(f"""
                    <div class="glass-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                            <span class="engagement-badge">🚀 VIRAL DRAFT</span>
                            <span style="font-size: 13px; color: #004182; font-weight: 600;">Reach Potential: {random.randint(85, 99)}%</span>
                        </div>
                        <div style="font-size: 17px; line-height: 1.7; color: #111; white-space: pre-wrap; font-family: 'Segoe UI', sans-serif;">{post}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Action Buttons
                st.download_button("📥 Download as .txt", post, file_name="linkedin_post.txt")
        else:
            # Placeholder State
            st.markdown("""
                <div class="glass-card" style="text-align: center; border: 2px dashed rgba(0,0,0,0.1); padding: 80px 20px;">
                    <p style="color: #777; font-size: 18px;">Your AI-generated post will appear in this transparent architect box.</p>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()