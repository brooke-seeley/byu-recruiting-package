import streamlit as st
import pandas as pd

from byu_recruiting import load_model, predict_proba

from byu_recruiting import load_hs_data, load_transfer_data

from byu_recruiting import (
    plot_distance_distribution,
    plot_score_distribution,
    plot_height_weight,
    plot_distance_comparison
)

# -------------------------------
# LOAD MODELS
# -------------------------------
hs_model = load_model('models/hs_model.pkl')
transfer_model = load_model('models/transfer_jc_model.pkl')

# -------------------------------
# LOAD DATA
# -------------------------------

X_hs, y_hs, _ = load_hs_data('data/RecruitmentPrediction.xlsx')
X_tr, y_tr, _ = load_transfer_data('data/RecruitmentPrediction.xlsx')

# Combine back into DataFrames for plotting
hs_data = X_hs.copy()
hs_data['BYU'] = y_hs

transfer_data = X_tr.copy()
transfer_data['BYU'] = y_tr

st.set_page_config(page_title="BYU Predictor", layout="wide")

st.title('BYU Commitment Predictor')

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
page = st.sidebar.selectbox(
    'Select Page',
    ['Prediction Tool', 'Model Insights', 'Data Insights']
)

# ===============================
# PAGE 1: PREDICTION TOOL
# ===============================
if page == 'Prediction Tool':

    player_type = st.selectbox(
        'Select Player Type',
        ['High School', 'Transfer / Junior College']
    )

    st.write('Enter player information below:')

    # -----------------------
    # MAPPINGS
    # -----------------------
    yes_no = {'Yes': 'Y', 'No': 'N'}

    conf_map = {
        'ACC': 'ACC',
        'Big 12': 'B12',
        'Big Ten': 'B1G',
        'SEC': 'SEC',
        'Group of 6/Independent': 'G6I',
        'FCS School': 'FCS',
        'Junior College': 'JC'
    }

    pos_map_1 = {
        'CB': 'CB',
        'DB/S': 'DB',
        'DL/DE/DT': 'DL',
        'LB': 'LB',
        'OL': 'OL',
        'QB': 'QB',
        'RB': 'RB',
        'TE': 'TE',
        'WR': 'WR'
    }

    pos_map_2 = {
        'CB/DB': 'CB',
        'DL/DE/DT': 'DL',
        'LB': 'LB',
        'OL': 'OL',
        'QB': 'QB',
        'RB': 'RB',
        'TE': 'TE',
        'WR': 'WR'
    }

    # ===============================
    # HIGH SCHOOL FORM
    # ===============================
    if player_type == 'High School':

        top247 = yes_no[st.selectbox('Top 247 Recruit?', yes_no.keys())]
        position = pos_map_1[st.selectbox('Position', pos_map_1.keys())]
        utah = yes_no[st.selectbox('From Utah?', yes_no.keys())]

        distance = st.number_input('Distance from BYU (miles)', min_value=0.0)
        height = st.number_input('Height (inches)', step=1, format="%d")
        weight = st.number_input('Weight (lbs)', step=1, format="%d")
        score = st.number_input('247 Composite Score', 0.0, 1.0, step=0.0001, format="%.4f")

        lds = yes_no[st.selectbox('LDS?', yes_no.keys())]
        alumni = yes_no[st.selectbox('Alumni Connection?', yes_no.keys())]
        poly = yes_no[st.selectbox('Polynesian?', yes_no.keys())]

        input_data = pd.DataFrame([{
            '247Top': top247,
            'Position': position,
            'Utah': utah,
            'Distance': distance,
            'Height': height,
            'Weight': weight,
            'Score': score,
            'LDS': lds,
            'Alumni': alumni,
            'Poly': poly
        }])

        model = hs_model

    # ===============================
    # TRANSFER / JC FORM
    # ===============================
    else:

        years = st.number_input('Years of Eligibility Remaining', min_value=0)
        top247 = yes_no[st.selectbox('Top 247 Transfer?', yes_no.keys())]
        position = pos_map_2[st.selectbox('Position', pos_map_2.keys())]
        distance = st.number_input('Distance from BYU (miles)', min_value=0.0)

        conf = conf_map[st.selectbox('Conference', conf_map.keys())]

        height = st.number_input('Height (inches)', min_value=60, step=1, format="%d")
        weight = st.number_input('Weight (lbs)', min_value=150, step=1, format="%d")
        score = st.number_input('247 Composite Score', 0.0, 1.0, step=0.0001, format="%.4f")

        lds = yes_no[st.selectbox('LDS?', yes_no.keys())]
        alumni = yes_no[st.selectbox('Alumni Connection?', yes_no.keys())]
        prev = yes_no[st.selectbox('Offered in High School?', yes_no.keys())]
        poly = yes_no[st.selectbox('Polynesian?', yes_no.keys())]

        input_data = pd.DataFrame([{
            'Years': years,
            '247Top': top247,
            'Position': position,
            'Distance': distance,
            'Conf': conf,
            'Height': height,
            'Weight': weight,
            'Score': score,
            'LDS': lds,
            'Alumni': alumni,
            'Prev': prev,
            'Poly': poly
        }])

        model = transfer_model

    # -------------------------------
    # PREDICT
    # -------------------------------
    if st.button('Predict Commitment Probability'):

        prob = predict_proba(model, input_data)[0]

        st.subheader(f'Probability of Commitment: {prob:.3f}')
        st.progress(float(prob))

        if prob > 0.7:
            st.success('High likelihood of committing to BYU')
        elif prob > 0.4:
            st.warning('Moderate likelihood')
        else:
            st.error('Low likelihood')

# ===============================
# PAGE 2: MODEL INSIGHTS
# ===============================
elif page == 'Model Insights':

    st.header('Prediction Model Insights')

    st.write("""
    This page provides a look into how the model makes decisions.
    """)

    st.subheader('Feature Importance (High School Model)')

    try:
        import matplotlib.pyplot as plt

        model = hs_model.named_steps['model']
        importances = model.feature_importances_

        st.write('Top features influencing predictions:')

        fig, ax = plt.subplots()
        ax.barh(range(len(importances)), importances)
        ax.set_title('Feature Importance')
        st.pyplot(fig)

    except:
        st.info('Feature importance not available for this model.')

    st.subheader('How to Interpret Predictions')

    st.write("""
    - Values closer to 1 indicate a higher likelihood of committing to BYU  
    - Values closer to 0 indicate a lower likelihood  
    - The model is trained on historical recruiting data including geography, ratings, and player background  
    """)

# ===============================
# PAGE 3: DATA INSIGHTS
# ===============================

elif page == 'Data Insights':

    st.header('Recruiting Data Insights')

    st.write("""
    These visualizations explore patterns in BYU recruiting data,
    comparing committed vs non-committed players and differences
    between high school and transfer recruits.
    """)

    # -------------------------------
    # SELECT DATASET
    # -------------------------------
    dataset_choice = st.selectbox(
        'Select Dataset',
        ['High School', 'Transfer / JC']
    )

    df = hs_data if dataset_choice == 'High School' else transfer_data

    # -------------------------------
    # TOGGLE FILTER
    # -------------------------------
    show_commits_only = st.checkbox('Show only committed players')

    if show_commits_only:
        df = df[df['BYU'] == 1]
        st.info('Showing committed players only')
    else:
        st.info('Showing all players')

    # -------------------------------
    # DISTANCE DISTRIBUTION
    # -------------------------------
    st.subheader('Distance from BYU')

    fig = plot_distance_distribution(df)
    st.pyplot(fig)

    if not show_commits_only:
        avg_dist = df.groupby('BYU')['Distance'].mean()
        st.markdown(f"""
        **Insight:**  
        Committed players average **{avg_dist[1]:.1f} miles**,  
        compared to **{avg_dist[0]:.1f} miles** for non-commits.
        """)

    # -------------------------------
    # SCORE DISTRIBUTION
    # -------------------------------
    st.subheader('247 Composite Score')

    fig = plot_score_distribution(df)
    st.pyplot(fig)

    if not show_commits_only:
        avg_score = df.groupby('BYU')['Score'].mean()
        st.markdown(f"""
        **Insight:**  
        Committed players average **{avg_score[1]:.3f}**,  
        vs **{avg_score[0]:.3f}** for non-committed players.
        """)

    # -------------------------------
    # HEIGHT vs WEIGHT
    # -------------------------------
    st.subheader('Height vs Weight')

    fig = plot_height_weight(df)
    st.pyplot(fig)

    st.markdown("""
    **Insight:**  
    Physical attributes alone do not strongly separate players.
    """)

    # -------------------------------
    # HS vs TRANSFER COMPARISON
    # -------------------------------
    if not show_commits_only:
        st.subheader('High School vs Transfer Comparison')

        fig = plot_distance_comparison(hs_data, transfer_data)
        st.pyplot(fig)

        st.markdown("""
        **Insight:**  
        Transfer players tend to come from a wider geographic range.
        """)