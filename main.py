# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.write('Sample data plot')
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    
    st.line_chart(chart_data)

if __name__ == '__main__':
    main()
