import matplotlib.pyplot as plt
from wordcloud import WordCloud

def text_data_analysis_word_clouds():
    # Sample text data
    text = """
    Python is an interpreted, high-level, general-purpose programming language.
    Created by Guido van Rossum and first released in 1991, Python's design
    philosophy emphasizes code readability with its notable use of significant whitespace.
    Its language constructs and object-oriented approach aim to help programmers write
    clear, logical code for small and large-scale projects.
    Python is dynamically-typed and garbage-collected. It supports multiple programming
    paradigms, including structured (particularly, procedural), object-oriented, and
    functional programming. Python is often described as a "batteries included" language
    due to its comprehensive standard library.
    """

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the generated image:
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("word_cloud.png")
    print("Word cloud saved to word_cloud.png")

text_data_analysis_word_clouds()
