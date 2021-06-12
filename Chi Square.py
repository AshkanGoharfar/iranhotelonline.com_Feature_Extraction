import numpy as np
import pandas as pd
import scipy.stats as stats


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
    content = content.replace("nan", "")
    for i in range(len(lines)):
        content = content.replace(lines[i], " ")
    return content


def persian_category_words(df1, category, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
    all_comments = persian_remove_stopwords(all_comments)
    all_comments = "".join(all_comments.split("،"))
    all_comments = "".join(all_comments.split("."))
    words_list = all_comments.split(" ")
    category_list = []
    for i in range(len(words_list)):
        category_list.append(category)
    del words_list[0]
    del category_list[0]
    return words_list, category_list


def english_category_words(df1, category, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
    all_comments = persian_remove_stopwords(all_comments)
    all_comments = "".join(all_comments.split("،"))
    all_comments = "".join(all_comments.split("."))
    all_comments = english_remove_stopwords(all_comments)
    words_list = all_comments.split(" ")

    category_list = []
    for i in range(len(words_list)):
        category_list.append(category)
    del words_list[0]
    del category_list[0]
    return words_list, category_list


def persian_extract_all_words(df1, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    bag_of_words = []
    for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
    all_comments = persian_remove_stopwords(all_comments)
    all_comments = "".join(all_comments.split("،"))
    all_comments = "".join(all_comments.split("."))
    words_list = all_comments.split(" ")
    for i in range(len(words_list)):
        if words_list[i] not in bag_of_words:
            bag_of_words.append(words_list[i])
    del bag_of_words[0]
    return bag_of_words


def english_extract_all_words(df1, comment_type):
    all_comments = ""
    list_comment = list(df1[comment_type])
    bag_of_words = []
    for i in range(len(list_comment)):
        if str(list_comment[i]) != "NaN" or str(list_comment[i]) != "nan":
            all_comments = all_comments + str(list_comment[i])
    all_comments = persian_remove_stopwords(all_comments)
    all_comments = "".join(all_comments.split(","))
    all_comments = "".join(all_comments.split("."))
    words_list = all_comments.split(" ")
    for i in range(len(words_list)):
        if words_list[i] not in bag_of_words:
            bag_of_words.append(words_list[i])
    del bag_of_words[0]
    return bag_of_words


def chi_square_positive_persian():
    df1 = pd.read_csv('Data/Iran Hotels Reviews.csv', error_bad_lines=False)
    df_family_trip = df1[df1["travel_type"] == "سفر با خانواده"]
    df_couple_trip = df1[df1["travel_type"] == "سفر با همسر"]
    df_single_trip = df1[df1["travel_type"] == "سفر مجردی"]
    df_business_trip = df1[df1["travel_type"] == "سفر تجاری"]
    df_friends_trip = df1[df1["travel_type"] == "سفر با دوستان"]

    all_words = []
    all_categories = []

    words_list, category_list = persian_category_words(df_family_trip, "Family", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)
    # print("********************************************************************")

    words_list, category_list = persian_category_words(df_couple_trip, "Couple", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7")

    words_list, category_list = persian_category_words(df_single_trip, "Solo", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    words_list, category_list = persian_category_words(df_business_trip, "Business", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    words_list, category_list = persian_category_words(df_friends_trip, "Friends", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    # print("********************************************************")
    words = np.array(all_words, dtype=object)
    categories = np.array(all_categories, dtype=object)

    observed = pd.DataFrame({"words": words,
                             "categories": categories})
    # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5555")
    observed_tab = pd.crosstab(observed.words, observed.categories, margins=True, margins_name="Total")

    # print(observed)
    # print("***************************************************")

    word_list_1 = []
    column_list_1 = []

    for key in observed_tab:
        column_list_1.append(key)

    word_list_1 = persian_extract_all_words(df1, "comment_positive")
    word_list_1.append("Total")

    observed_tab.index = word_list_1
    observed_tab.columns = column_list_1

    observed = observed_tab.ix[0:len(observed_tab.index) - 1, 0:len(observed_tab.columns) - 1]

    # print(observed)
    # print("################################################################################")
    expected = np.outer(observed_tab["Total"][0:len(observed_tab.index) - 1],
                        observed_tab.ix["Total"][0:len(observed_tab.columns) - 1]) / 1000
    count = 0

    # print("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    # for item in expected:
    #     print(len(item))
    # print("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    #
    # for key in expected:
    #     count += 1
    # print(count)
    # print(expected)
    expected = pd.DataFrame(expected)
    del column_list_1[-1]
    word_list_2 = persian_extract_all_words(df1, "comment_positive")
    expected.columns = column_list_1
    expected.index = word_list_2

    # print(expected)
    #
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    chi_square_res = (((observed - expected) ** 2) / expected)

    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print(len(chi_square_res["Family"]))
    # print(len(word_list_2))
    sorted_family_score = sorted(chi_square_res["Family"], reverse=True)[0:50]
    sorted_couple_score = sorted(chi_square_res["Couple"], reverse=True)[0:50]
    sorted_solo_score = sorted(chi_square_res["Solo"], reverse=True)[0:50]
    sorted_business_score = sorted(chi_square_res["Business"], reverse=True)[0:50]
    sorted_friends_score = sorted(chi_square_res["Friends"], reverse=True)[0:50]

    print(sorted_family_score)
    print("Positive comment : ")
    print("Family trip : ")
    for item in sorted_family_score:
        print(item)
        print(word_list_2[sorted_family_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Couple trip : ")
    for item in sorted_couple_score:
        print(item)
        print(word_list_2[sorted_couple_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Solo trip : ")
    for item in sorted_solo_score:
        print(item)
        print(word_list_2[sorted_solo_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Business trip : ")
    for item in sorted_business_score:
        print(item)
        print(word_list_2[sorted_business_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Friends trip : ")
    for item in sorted_friends_score:
        print(item)
        print(word_list_2[sorted_friends_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def chi_square_negative_persian():
    df1 = pd.read_csv('Data/Iran Hotels Reviews.csv', error_bad_lines=False)
    df_family_trip = df1[df1["travel_type"] == "سفر با خانواده"]
    df_couple_trip = df1[df1["travel_type"] == "سفر با همسر"]
    df_single_trip = df1[df1["travel_type"] == "سفر مجردی"]
    df_business_trip = df1[df1["travel_type"] == "سفر تجاری"]
    df_friends_trip = df1[df1["travel_type"] == "سفر با دوستان"]

    all_words = []
    all_categories = []

    words_list, category_list = persian_category_words(df_family_trip, "Family", "comment_negative")
    all_words.extend(words_list)
    all_categories.extend(category_list)
    print("********************************************************************")

    words_list, category_list = persian_category_words(df_couple_trip, "Couple", "comment_negative")
    all_words.extend(words_list)
    all_categories.extend(category_list)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7")

    words_list, category_list = persian_category_words(df_single_trip, "Solo", "comment_negative")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    words_list, category_list = persian_category_words(df_business_trip, "Business", "comment_negative")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    words_list, category_list = persian_category_words(df_friends_trip, "Friends", "comment_negative")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    print("********************************************************")
    words = np.array(all_words, dtype=object)
    categories = np.array(all_categories, dtype=object)

    observed = pd.DataFrame({"words": words,
                             "categories": categories})
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5555")
    observed_tab = pd.crosstab(observed.words, observed.categories, margins=True, margins_name="Total")

    print(observed)
    print("***************************************************")

    word_list_1 = []
    for item in words:
        if item not in word_list_1:
            word_list_1.append(item)
    column_list_1 = []

    for key in observed_tab:
        column_list_1.append(key)

    word_list_3 = persian_extract_all_words(df1, "comment_negative")
    # word_list_1.append("شاک")
    # del word_list_1[1]
    # for item in word_list_3:
    #     if item not in word_list_1:
    #         word_list_1.append(item)
    for item in word_list_1:
        if item not in word_list_3:
            word_list_3.append(item)

    # word_list_1.append("رت")
    # word_list_1.append("مل")
    # word_list_1.append("بغ")
    # word_list_1.append("هن")
    # del word_list_1[1]
    # del word_list_1[1]
    # del word_list_1[1]
    # del word_list_1[1]
    # del word_list_1[1]
    # if "Total" in word_list_1:
    #     print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    word_list_3.append("Total")
    word_list_1.append("Total")
    word_list_4 = []
    # for item in word_list_3:
    print(len(word_list_3))
    print(len(word_list_1))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^66")
    print(word_list_1)
    observed_tab.index = word_list_1
    # observed_tab.index = word_list_3
    observed_tab.columns = column_list_1

    observed = observed_tab.ix[0:len(observed_tab.index) - 1, 0:len(observed_tab.columns) - 1]

    print(observed)
    print("################################################################################")
    expected = np.outer(observed_tab["Total"][0:len(observed_tab.index) - 1],
                        observed_tab.ix["Total"][0:len(observed_tab.columns) - 1]) / 1000

    expected = pd.DataFrame(expected)
    del column_list_1[-1]
    word_list_2 = persian_extract_all_words(df1, "comment_negative")
    expected.columns = column_list_1
    expected.index = word_list_2

    print(expected)

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    chi_square_res = (((observed - expected) ** 2) / expected)

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(len(chi_square_res["Family"]))
    print(len(word_list_2))
    sorted_family_score = sorted(chi_square_res["Family"], reverse=True)[0:50]
    sorted_couple_score = sorted(chi_square_res["Couple"], reverse=True)[0:50]
    sorted_solo_score = sorted(chi_square_res["Solo"], reverse=True)[0:50]
    sorted_business_score = sorted(chi_square_res["Business"], reverse=True)[0:50]
    sorted_friends_score = sorted(chi_square_res["Friends"], reverse=True)[0:50]

    print(sorted_family_score)
    print("Negative comment : ")
    print("Family trip : ")
    for item in sorted_family_score:
        print(item)
        print(word_list_2[sorted_family_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Couple trip : ")
    for item in sorted_couple_score:
        print(item)
        print(word_list_2[sorted_couple_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Solo trip : ")
    for item in sorted_solo_score:
        print(item)
        print(word_list_2[sorted_solo_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Business trip : ")
    for item in sorted_business_score:
        print(item)
        print(word_list_2[sorted_business_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Friends trip : ")
    for item in sorted_friends_score:
        print(item)
        print(word_list_2[sorted_friends_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def chi_square_positive_english():
    df1 = pd.read_csv('Data/Hotel Reviews.csv', error_bad_lines=False)
    df_family_trip = df1[df1["travel_type"] == "Family"]
    df_couple_trip = df1[df1["travel_type"] == "Couple"]
    df_single_trip = df1[df1["travel_type"] == "Solo"]
    df_business_trip = df1[df1["travel_type"] == "Business"]
    df_friends_trip = df1[df1["travel_type"] == "Friends"]

    all_words = []
    all_categories = []

    words_list, category_list = english_category_words(df_family_trip, "Family", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)
    # print("********************************************************************")

    words_list, category_list = english_category_words(df_couple_trip, "Couple", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7")

    words_list, category_list = english_category_words(df_single_trip, "Solo", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    words_list, category_list = english_category_words(df_business_trip, "Business", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    words_list, category_list = english_category_words(df_friends_trip, "Friends", "comment_positive")
    all_words.extend(words_list)
    all_categories.extend(category_list)

    # print("********************************************************")

    words = np.array(all_words, dtype=object)
    categories = np.array(all_categories, dtype=object)

    observed = pd.DataFrame({"words": words,
                             "categories": categories})
    # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5555")
    # word_list_1 = persian_extract_all_words(df1, "comment_positive")
    # word_list_1.append("Total")
    # print(len(observed.words))
    # print(len(observed.categories))
    # index_list = []
    # for item in observed.index:
    #     index_list.append(item)
    # for i in range(len(observed.index)):
    #     print(observed.index[i])
    observed_tab = pd.crosstab(observed.words, observed.categories, margins=True, margins_name="Total")
    # observed_tab = pd.crosstab(observed.words, observed.categories, index=word_list_1, columns=column_list_1, margins=True)

    # print(observed)
    # print("***************************************************")
    # print(observed_tab)
    word_list_1 = []
    column_list_1 = []

    # column_list_1 = ["Family, Couple", "Solo", "Business", "Friends", "Total"]
    # column_list_1 = ["Family, Couple", "Solo", "Business", "Friends"]
    # for key in observed_tab:
    #     column_list_1.append(key)

    for item in words:
        if item not in word_list_1:
            word_list_1.append(item)
    word_list_1.append("Total")

    for key in observed_tab:
        column_list_1.append(key)
    # del column_list_1[-1]
    # print(column_list_1)

    observed_tab.index = word_list_1
    observed_tab.columns = column_list_1

    observed = observed_tab.ix[0:len(observed_tab.index) - 1, 0:len(observed_tab.columns) - 1]

    # print(observed)
    # print("################################################################################")
    expected = np.outer(observed_tab["Total"][0:len(observed_tab.index) - 1],
                        observed_tab.ix["Total"][0:len(observed_tab.columns) - 1]) / 1000
    # expected = np.outer(observed_tab.ix["Total"][0:len(observed_tab.columns) - 1],
    #                     observed_tab["Total"][0:len(observed_tab.index) - 1]) / 1000
    # print(len(observed_tab.columns))
    # print("iinininii")
    count = 0
    # print(expected)
    # print("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    for i in range(len(expected)):
        np.reshape(expected[i][6:], 6)
    # print("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

    # for key in expected:
    #     count += 1
    #     # print(key)
    # print(count)
    expected = pd.DataFrame(expected)
    # expected.drop(0, inplace=True, axis=1)
    # expected.drop(1, inplace=True, axis=1)
    # expected.drop(2, inplace=True, axis=1)
    # expected.drop(3, inplace=True, axis=1)
    # expected.drop(4, inplace=True, axis=1)
    # expected.drop(5, inplace=True, axis=1)

    # expected.drop(6, inplace=True, axis=1)
    # expected.drop(7, inplace=True, axis=1)
    # expected.drop(8, inplace=True, axis=1)
    # expected.drop(9, inplace=True, axis=1)
    # expected.drop(10, inplace=True, axis=1)
    # expected.drop(11, inplace=True, axis=1)

    # for key in expected:
    #     print(key)
    #
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    # del column_list_1[-1]
    column_list_1.extend(column_list_1)
    word_list_2 = word_list_1[:-1]
    # word_list_2 = persian_extract_all_words(df1, "comment_positive")
    expected.columns = column_list_1
    expected.index = word_list_2
    # expected.columns = word_list_2
    # expected.index = column_list_1

    expected.drop(columns=["Business", "Couple", "Family", "Friends", "Solo", "Total"])
    # print(expected["Business"].to_numpy())
    business_list = []
    for item in expected["Business"].to_numpy():
        business_list.append(item[1])
        # print("gayiidi")
    # print(len(expected["Business"].to_numpy()))
    couple_list = []
    for item in expected["Couple"].to_numpy():
        couple_list.append(item[1])
    family_list = []
    for item in expected["Family"].to_numpy():
        family_list.append(item[1])
    friends_list = []
    for item in expected["Friends"].to_numpy():
        friends_list.append(item[1])
    solo_list = []
    for item in expected["Solo"].to_numpy():
        solo_list.append(item[1])
    # d = {'Business': business_list, 'Couple': couple_list, 'Family': family_list, 'Friends': friends_list, 'Solo':solo_list}
    # expected_2 = pd.DataFrame(data=d)
    # expected_2 = pd.DataFrame(np.array([business_list, couple_list, family_list, friends_list, solo_list]),
    #                columns=['Business', 'Couple', 'Family', "Friends", "Solo"])
    # expected.drop([0,1,2,3,4,5])
    expected_2 = expected
    expected_3 = expected_2.ix[:, ~expected_2.columns.duplicated()]
    # expected_2.drop(expected_3)
    expected_3 = expected_3.drop(columns=["Total"])
    for i in range(len(expected_3["Business"])):
        expected_3["Business"][i] = business_list[i]
    for i in range(len(expected_3["Couple"])):
        expected_3["Couple"][i] = couple_list[i]
    for i in range(len(expected_3["Family"])):
        expected_3["Family"][i] = family_list[i]
    for i in range(len(expected_3["Friends"])):
        expected_3["Friends"][i] = friends_list[i]
    for i in range(len(expected_3["Solo"])):
        expected_3["Solo"][i] = solo_list[i]
    # expected_2 = expected_2[!expected_3]

    # for key in expected_3:
    #     print(key)
    # print(expected_3)
    expected = expected_3
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    chi_square_res = (((observed - expected) ** 2) / expected)

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print(len(chi_square_res["Family"]))
    # print(len(word_list_2))
    sorted_family_score = sorted(chi_square_res["Family"], reverse=True)[0:50]
    sorted_couple_score = sorted(chi_square_res["Couple"], reverse=True)[0:50]
    sorted_solo_score = sorted(chi_square_res["Solo"], reverse=True)[0:50]
    sorted_business_score = sorted(chi_square_res["Business"], reverse=True)[0:50]
    sorted_friends_score = sorted(chi_square_res["Friends"], reverse=True)[0:50]

    print(sorted_family_score)
    print("Positive comment : ")
    print("Family trip : ")
    for item in sorted_family_score:
        print(item)
        print(word_list_2[sorted_family_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Couple trip : ")
    for item in sorted_couple_score:
        print(item)
        print(word_list_2[sorted_couple_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Solo trip : ")
    for item in sorted_solo_score:
        print(item)
        print(word_list_2[sorted_solo_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Business trip : ")
    for item in sorted_business_score:
        print(item)
        print(word_list_2[sorted_business_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Friends trip : ")
    for item in sorted_friends_score:
        print(item)
        print(word_list_2[sorted_friends_score.index(item)])
        print("***********************************************")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


chi_square_positive_persian()

# chi_square_negative_persian()

chi_square_positive_english()
