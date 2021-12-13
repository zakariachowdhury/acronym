import streamlit as st
from acronym import acronym
import nltk

APP_TITLE = "Acronym Generator"

def main():
    st.title(APP_TITLE)

    min_length = max_length = strict = None

    with st.expander('Info', False):
        st.write('A python-based tool for creating English-ish Acronyms from your fancy project.')
        st.write('ACRONYM is described in this paper released on the arXiv: https://arxiv.org/abs/1903.12180')
        st.markdown('<iframe src="https://ghbtns.com/github-btn.html?user=zakariachowdhury&repo=acronym&type=star&count=true" frameborder="0" scrolling="0" width="150" height="20" title="GitHub"></iframe>', unsafe_allow_html=True)

        st.subheader('Scoring System')
        st.markdown('* 10 points if first letter in a word (with exception of first letter)')
        st.markdown('* 3 point if second or last letter in a word')
        st.markdown('* 1 point otherwise')
        st.markdown('* N bonus points if begins an N-length valid sub-word (ex: multiVariable -> 8 bonus points)')
        st.markdown('* 2 bonus points if immediately following another capitalizd letter')


    with st.expander('Options', False):
        min_length = st.number_input('Min Length', 0, 10, 4)
        max_length = st.number_input('Max Length', 0, 15, 9)
        strict = st.selectbox('How strictly should the words be related to real English?', ['None', 'Strict', 'Very Strict'])

    name = st.text_input('Enter your keywords')

    if st.button('Generate'):
        if name is not None and len(name):
            # try:
            if strict == 'None':
                corpus = nltk.corpus.words
            elif strict == 'Strict':
                corpus = nltk.corpus.brown
            else:
                corpus = nltk.corpus.gutenberg

            with st.spinner('Generating acronyms, please wait...'):
                results = acronym.find_acronyms(name, corpus, min_length, max_length)
                st.subheader('Results')
                st.write(results)
                st.info('Total Acronyms = ' + str(len(results)))
            # except:
            #     st.error('Unable to generate acronyms')
        else:
            st.error('Enter your keywords first')
main()