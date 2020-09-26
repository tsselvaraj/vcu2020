from pprint import pprint as print
from gensim.summarization import summarize
import requests

text = (
    "Thomas A. Anderson is a man living two lives. By day he is an "
    "average computer programmer and by night a hacker known as "
    "Neo. Neo has always questioned his reality, but the truth is "
    "far beyond his imagination. Neo finds himself targeted by the "
    "police when he is contacted by Morpheus, a legendary computer "
    "hacker branded a terrorist by the government. Morpheus awakens "
    "Neo to the real world, a ravaged wasteland where most of "
    "humanity have been captured by a race of machines that live "
    "off of the humans' body heat and electrochemical energy and "
    "who imprison their minds within an artificial reality known as "
    "the Matrix. As a rebel against the machines, Neo must return to "
    "the Matrix and confront the agents: super-powerful computer "
    "programs devoted to snuffing out Neo and the entire human "
    "rebellion. "
)
print(text)
print("-------")
print(summarize(text))
print("-------")
text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text
print(summarize(text, ratio=0.01))
print("-------")