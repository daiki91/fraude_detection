import altair as alt
import pandas as pd
import streamlit as st

def graphe1():
    # Example data
    data = pd.DataFrame({
        'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'sales_amount': [30, 40, 45, 50, 20, 30, 70, 60, 50, 40, 30, 20]
    })

    chart = alt.Chart(data).mark_bar(cornerRadiusEnd=4, color='#277549').encode(
        x=alt.X('month', type='nominal', axis=alt.Axis(labelAngle=0, title=None, grid=False)),
        y=alt.Y('sales_amount', type='quantitative', axis=alt.Axis(title=None, grid=False))
    ).properties(
        width=704,
        height=350,
        padding={'bottom': 20},
        title=alt.TitleParams(
            text='Sales Amount by Month',  # Provide a title text
            align='left',
            anchor='start',
            color='#31333F',
            fontStyle='normal',
            fontWeight=600,
            fontSize=16,
            offset=26,
            orient='top'
        )
    ).configure(
        font="Source Sans Pro",
        background="#ffffff",
        axis=alt.AxisConfig(
            labelFontSize=12,
            labelFontWeight=400,
            labelColor="#808495",
            labelFontStyle='normal',
            titleFontWeight=400,
            titleFontSize=14,
            titleColor="#808495",
            titleFontStyle='normal',
            ticks=False,
            gridColor='#e6eaf1',
            domain=False,
            domainWidth=1,
            domainColor='#e6eaf1',
            labelFlush=True,
            labelFlushOffset=1,
            labelBound=False,
            labelLimit=100,
            titlePadding=16,
            labelPadding=16,
            labelSeparation=4,
            labelOverlap=True
        ),
        legend=alt.LegendConfig(
            labelFontSize=14,
            labelFontWeight=400,
            labelColor="#808495",
            titleFontSize=14,
            titleFontWeight=400,
            titleFontStyle='normal',
            titleColor='#808495',
            titlePadding=5,
            labelPadding=16,
            columnPadding=8,
            rowPadding=4,
            padding=7,
            symbolStrokeWidth=4
        ),
        view=alt.ViewConfig(
            strokeWidth=0,
            stroke='transparent',
            continuousHeight=350,
            continuousWidth=400
        )
    )

    st.altair_chart(chart)

if __name__ == "__main__":
    graphe1()
