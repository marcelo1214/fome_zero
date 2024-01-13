import streamlit as st 


def aling(h = 'h1',text = 'title'):
    corpo = "<" + h
    corpo += " style=" + "'text-align: center'>"
    corpo += text
    corpo += "</" + h + ">"
    return  corpo