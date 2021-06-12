import spacy
import pytextrank
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def persian_text_rank(df1, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
    all_comments = ''.join(all_comments.split("هتل"))
    all_comments = ''.join(all_comments.split("خوب"))
    all_comments = persian_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")

    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)

    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        else:
            return 0
        counter += 1


def english_text_rank(df1, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    persian_remove_stopwords("ok1")
    # print(len(list_comment))
    for i in range(10400):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1




    all_comments = ""
    for i in range(10401, 21000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(21000, 31000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1



    all_comments = ""
    for i in range(31000, 41000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(41000, 51000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(51000, 61000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(61000, 71000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1



    all_comments = ""
    for i in range(71000, 81000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1




def english_text_rank_single_trip(df1, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    persian_remove_stopwords("ok1")
    # print(len(list_comment))
    for i in range(10400):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1




    all_comments = ""
    for i in range(10401, 21000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(21000, 31000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1



    all_comments = ""
    for i in range(31000, 41000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1



    all_comments = ""
    for i in range(41000, len(list_comment)):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1






def english_text_rank_friends_trip(df1, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    persian_remove_stopwords("ok1")
    # print(len(list_comment))
    for i in range(10400):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1




    all_comments = ""
    for i in range(10401, 21000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(21000, 31000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1



    all_comments = ""
    for i in range(31000, 41000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(41000, 51000):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1


    all_comments = ""
    for i in range(51000, len(list_comment)):
    # for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
        # print(i)
    all_comments = ''.join(all_comments.split("hotel"))
    # all_comments = ''.join(all_comments.split(""))
    all_comments = english_remove_stopwords(all_comments)
    text = all_comments
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")
    persian_remove_stopwords("ok2")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)
    persian_remove_stopwords("ok3")
    # examine the top-ranked phrases in the document
    counter = 0
    for phrase in doc._.phrases:
        if counter < 7:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
            print("*********************************************")
        # else:
        #     return 0
        counter += 1





def persian_remove_stopwords(content):
    file1 = open('Data/PersianStoplist.txt', 'r', encoding="utf-8")
    lines = file1.readlines()

    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = " " + lines[i].split("\n")[0] + " "

    content = content.replace("nan", "")
    for i in range(len(lines)):
        content = content.replace(lines[i], " ")
    return content


def english_remove_stopwords(content):
    file1 = open('Data/SmartStoplist.txt', 'r', encoding="utf-8")
    lines = file1.readlines()
    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = " " + lines[i].split("\n")[0] + " "
    for i in range(len(lines)):
        content = content.replace(lines[i], " ")
    return content


# persian_remove_stopwords()


def main():
    # df1 = pd.read_csv('Data/Iran Hotels Reviews.csv', error_bad_lines=False)
    # df_family_trip = df1[df1["travel_type"] == "سفر با خانواده"]
    # df_couple_trip = df1[df1["travel_type"] == "سفر با همسر"]
    # df_single_trip = df1[df1["travel_type"] == "سفر مجردی"]
    # df_business_trip = df1[df1["travel_type"] == "سفر تجاری"]
    # df_friends_trip = df1[df1["travel_type"] == "سفر با دوستان"]
    # print("Persian Comments Positive Views")
    # print("family_trip : ")
    # persian_text_rank(df_family_trip, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("couple_trip : ")
    # persian_text_rank(df_couple_trip, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("single_trip : ")
    # persian_text_rank(df_single_trip, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("business_trip : ")
    # persian_text_rank(df_business_trip, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("friends_trip : ")
    # persian_text_rank(df_friends_trip, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #
    # print("Persian Comments Negative Views")
    # print("family_trip : ")
    # persian_text_rank(df_family_trip, "comment_negative")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("couple_trip : ")
    # persian_text_rank(df_couple_trip, "comment_negative")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("single_trip : ")
    # persian_text_rank(df_single_trip, "comment_negative")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("business_trip : ")
    # persian_text_rank(df_business_trip, "comment_negative")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("friends_trip : ")
    # persian_text_rank(df_friends_trip, "comment_negative")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


    df2 = pd.read_csv('Data/Hotel Reviews.csv')
    df_family_trip_2 = df2[df2["travel_type"] == "Family"]
    df_couple_trip_2 = df2[df2["travel_type"] == "Couple"]
    df_single_trip_2 = df2[df2["travel_type"] == "Solo"]
    df_business_trip_2 = df2[df2["travel_type"] == "Business"]
    df_friends_trip_2 = df2[df2["travel_type"] == "Friends"]



    # print("English Comments Positive Views")
    # print("family_trip : ")
    # english_text_rank(df_family_trip_2, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("couple_trip : ")
    # english_text_rank(df_couple_trip_2, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("single_trip : ")
    # english_text_rank_single_trip(df_single_trip_2, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("business_trip : ")
    # english_text_rank(df_business_trip_2, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("friends_trip : ")
    # english_text_rank_friends_trip(df_friends_trip_2, "comment_positive")
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    print("English Comments Negative Views")
    print("family_trip : ")
    english_text_rank(df_family_trip_2, "comment_negative")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("couple_trip : ")
    english_text_rank(df_couple_trip_2, "comment_negative")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("single_trip : ")
    english_text_rank_single_trip(df_single_trip_2, "comment_negative")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("business_trip : ")
    english_text_rank(df_business_trip_2, "comment_negative")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("friends_trip : ")
    english_text_rank_friends_trip(df_friends_trip_2, "comment_negative")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


main()
