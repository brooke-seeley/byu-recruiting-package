# visualize.py

import matplotlib.pyplot as plt


def plot_distance_distribution(df):
    """
    Plot distance distributions for committed vs non-committed players.
    """
    fig, ax = plt.subplots()

    ax.hist(df[df['BYU'] == 1]['Distance'], bins=20, alpha=0.6, label='Committed')
    ax.hist(df[df['BYU'] == 0]['Distance'], bins=20, alpha=0.6, label='Not Committed')

    ax.set_title('Distance from BYU')
    ax.set_xlabel('Miles')
    ax.legend()

    return fig


def plot_score_distribution(df):
    """
    Plot composite score distributions.
    """
    fig, ax = plt.subplots()

    ax.hist(df[df['BYU'] == 1]['Score'], bins=20, alpha=0.6, label='Committed')
    ax.hist(df[df['BYU'] == 0]['Score'], bins=20, alpha=0.6, label='Not Committed')

    ax.set_title('247 Composite Score')
    ax.set_xlabel('Score')
    ax.legend()

    return fig


def plot_height_weight(df):
    """
    Scatter plot of height vs weight.
    """
    fig, ax = plt.subplots()

    ax.scatter(df['Height'], df['Weight'], alpha=0.5)

    ax.set_title('Height vs Weight')
    ax.set_xlabel('Height (inches)')
    ax.set_ylabel('Weight (lbs)')

    return fig


def plot_distance_comparison(hs_df, transfer_df):
    """
    Compare distance distributions between HS and Transfer players.
    """
    fig, ax = plt.subplots()

    ax.hist(hs_df['Distance'], bins=20, alpha=0.5, label='HS')
    ax.hist(transfer_df['Distance'], bins=20, alpha=0.5, label='Transfer')

    ax.set_title('HS vs Transfer Distance')
    ax.legend()

    return fig