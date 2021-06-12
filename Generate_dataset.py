import pandas as pd

# df = pd.read_csv('Data/Iran Hotels Data.csv', index_col=False)
#
# f = open('Data/Iran Hotels Reviews.csv', 'w+')
# f.write(
#     'hotel,city,subject,comment_time,enter_time,stay_duration,permanent_residence,travel_type,comment_positive,comment_negative,user_score,hotel_star')
# f.close()
#
# for i in range(len(df["hotel"])):
#     if int(df["user_score"][i]) > 3:
#         f = open('Data/Iran Hotels Reviews.csv', 'a', encoding="utf-8")
#         # print(str(df["hotel"][i]))
#         f.write(
#             '\n' + str(df["hotel"][i]) + ',' + str(df["city"][i]) + ',' + str(
#                 df["subject"][i]) + ',' + str(df["comment_time"][i]) + ',' + str(df["enter_time"][i]) + ',' + str(
#                 df["stay_duration"][i]) + ',' + str(df["permanent_residence"][i]) + ',' + str(
#                 df["travel_type"][i]) + ',' + str(
#                 df["comment"][i]) + ',' + str("NaN"
#                                               ) + ',' + str(df["user_score"][i]) + ',' + str(df["hotel_star"][i]))
#         f.close()
#     elif int(df["user_score"][i]) < 3:
#         f = open('Data/Iran Hotels Reviews.csv', 'a', encoding="utf-8")
#         f.write(
#             '\n' + str(df["hotel"][i]) + ',' + str(df["city"][i]) + ',' + str(
#                 df["subject"][i]) + ',' + str(df["comment_time"][i]) + ',' + str(df["enter_time"][i]) + ',' + str(
#                 df["stay_duration"][i]) + ',' + str(df["permanent_residence"][i]) + ',' + str(
#                 df["travel_type"][i]) + ',' + str(
#                 "NaN") + ',' + str(df["comment"][i]
#                                    ) + ',' + str(df["user_score"][i]) + ',' + str(df["hotel_star"][i]))
#         f.close()




df = pd.read_csv('Data/Hotel_Reviews.csv')

f = open('Data/Hotel Reviews.csv', 'w+')
f.write(
    'hotel,country,subject,comment_time,enter_time,stay_duration,permanent_residence,travel_type,comment_positive,comment_negative,user_score,hotel_star')
f.close()

for i in range(len(df["Hotel_Name"])):
    # if df["user_score"][i] > 3:
    f = open('Data/Hotel Reviews.csv', 'a', encoding="utf-8")

    travel_type = ""
    # print(df["Tags"][i])
    tags = [df["Tags"][i][2]]
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    for j in range(3, len(df["Tags"][i]) - 2):
        if df["Tags"][i][j] != "," or df["Tags"][i][j] != "'":
            tags[-1] = tags[-1] + df["Tags"][i][j]
        elif df["Tags"][i][j] == ",":
            tags.append("")

    # print(("'" + tags[0].replace("'", "") + "'").split(","))
    # print((tags[0].replace("'", "")).split(","))
    tags = (tags[0].replace("'", "")).split(",")
    # print(tags)
    for k in range(len(tags)):
        # print(term)
        if tags[k][0:2] == "  ":
            tags[k] = tags[k][1:]

    # print(df["Tags"][i])
    # print(list(df["Tags"][i]))
    # df["Tags"][i] = tags
    #
    # if df
    if len(tags) > 1:
        flag = 0
        if tags[0] != " Leisure trip " and tags[0] != " Business trip " and "Solo" not in tags[0]:
            del tags[0]
        if tags[0] == " Leisure trip ":
            if " Family with" in tags[1]:
                travel_type = "Family"
            elif tags[1] == " Group ":
                travel_type = "Friends"
            else:
                travel_type = tags[1].split(" ")[1]
        elif tags[0] == " Business trip ":
            travel_type = "Business"
        elif "Solo" in tags[0]:
            travel_type = "Solo"
            tags.insert(0, " ")
        elif "Couple" in tags[0]:
            travel_type = "Couple"
            tags.insert(0, " ")
        elif "Family" in tags[0]:
            travel_type = "Family"
            tags.insert(0, " ")
            if "Stayed" in tags[2]:
                tags.insert(0, " ")
        elif "Group" in tags[0]:
            travel_type = "Group"
            flag = 1
        else:
            travel_type = "NaN"
            flag = 1
            # break

        if len(tags) > 3 and flag == 0:
            # print(tags)
            # if " Stayed " in df["Tags"][i][3]:
            stay_duration = tags[3].split(" Stayed ")[1].split("night")[0]
        elif flag == 1:
            stay_duration = "NaN"
        else:
            stay_duration = "NaN"

        if df["Positive_Review"][i] == "No Positive":
            df["Positive_Review"][i] = "NaN"
        if df["Negative_Review"][i] == "No Negative":
            df["Negative_Review"][i] = "NaN"
        f.write(
            '\n' + str(df["Hotel_Name"][i]) + ',' + str(df["Hotel_Address"][i].split(" ")[-1]) + ',' + str(
                "NaN") + ',' + str("NaN") + ',' + str(df["days_since_review"][i]) + ',' + str(
                stay_duration) + ',' + str(df["Reviewer_Nationality"][i]) + ',' + str(travel_type) + ',' + str(
                df["Positive_Review"][i]) + ',' + str(df["Negative_Review"][i]
                                                      ) + ',' + str(df["Reviewer_Score"][i]) + ',' + str("NaN"))
        f.close()

# elif df["user_score"][i] < 3:

