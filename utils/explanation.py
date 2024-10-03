import streamlit as st
import os
import pandas as pd


def explanation(explain_path):
    explain = pd.read_json(explain_path)