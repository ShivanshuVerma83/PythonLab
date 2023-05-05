import re

def extract_hashtags(text):

    regex = "#(\w+)"


    hashtag_list = re.findall(regex, text)
    print("The hashtags in \"" + text + "\" are :")
    for hashtag in hashtag_list:
        print('#',hashtag)

text1 = "i mad a  wonderful #website for #ComputerScience"
text2 = "This day is beautiful ! #instagood #photooftheday #cute"
extract_hashtags(text1)
extract_hashtags(text2)

