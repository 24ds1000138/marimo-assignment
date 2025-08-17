# analysis.py
# Email: 24ds1000138@ds.study.iitm.ac.in

import marimo

__generated_with = "0.14.17"
app = marimo.App()


# Cell 0: Import marimo as mo (needed for widgets and markdown)
@app.cell
def _():
    import marimo as mo
    return mo,


# Cell 1: Load dataset
# This cell loads a built-in dataset (penguins) into a DataFrame.
@app.cell
def _():
    import seaborn as sns
    df = sns.load_dataset("penguins").dropna()
    df
    return df, sns


# Cell 2: Slider widget
# This slider controls how many rows of the dataset to display.
@app.cell
def _(mo):
    slider = mo.ui.slider(5, 50, 5, value=10, label="Number of rows")
    slider
    return slider,


# Cell 3: Filtered dataset based on slider
# This depends on both the dataset (df) and slider widget value.
@app.cell
def _(df, slider):
    filtered_df = df.head(slider.value)
    filtered_df
    return filtered_df,


# Cell 4: Dynamic markdown
# This cell generates text that updates whenever the slider changes.
@app.cell
def _(mo, slider):
    mo.md(f"""
    ### Dataset Preview  
    You are currently viewing the **first {slider.value} rows** of the dataset.
    """)
    return


# Cell 5: Scatterplot visualization
# This depends on the filtered dataset and seaborn.
@app.cell
def _(filtered_df, sns, plt):
    fig, ax = plt.subplots()
    sns.scatterplot(
        data=filtered_df,
        x="bill_length_mm",
        y="bill_depth_mm",
        hue="species",
        ax=ax
    )
    fig
    return fig,


# Cell 6: Import matplotlib
# Used by the plotting cell above.
@app.cell
def _():
    import matplotlib.pyplot as plt
    return plt,


if __name__ == "__main__":
    app.run()
