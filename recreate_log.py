from glob import glob
import re
import csv

talk_data_num_file = open("talk_data_num_file.txt", "w")
for file in glob("D:/人狼知能開発/Past Log/GAT2017Log05/gat2017log05" + "/*/*.log"):
    log_data = open(file)
    talks = []
    day_talk = []
    day = 0
    talk_num = ""
    status = ""
    for line in log_data:
        line = line.replace("\n", "")
        line_list = line.split(",")
        if line_list[0] != str(day):
            talks.append(day_talk)
            day_talk = []
            talk_data_num_file.write(status + "\n")
            talk_data_num_file.write(talk_num + "\n")
            print(talk_num)
            talk_num = ""
            day += 1
        if line_list[1] == "status":
            if line_list[0] == "0":
                if status == "":
                    status += line_list[3]
                else:
                    status += "," + line_list[3]
        if line_list[1] == "talk":
            text = line_list[5]
            talker = line_list[4]
            words = text.split(" ")
            if words[0] == "AGREE" or words[0] == "DISAGREE":
                day_search = re.search(r"[0-9]+", words[2])
                talk_ID_search = re.search(r"[0-9]+", words[3])

                day_ = int(day_search.group())
                talk_ID = int(talk_ID_search.group())

                if day == day_:
                    text = words[0] + " " + day_talk[talk_ID]
                else:
                    text = words[0] + " " + talks[day_][talk_ID]
            
            day_talk.append(text)
            write_text = "{}:{}".format(talker, text)

            talk_data_file = open("./talkdata.csv")
            
            for talk_data in talk_data_file:
                talk_data_list = talk_data.split(",")
                if write_text == talk_data_list[0]:
                    if talk_num == "":
                        talk_num += talk_data_list[1]
                    else:
                        talk_num += "," + talk_data_list[1]
            talk_data_file.close()
                

    log_data.close()

talk_data_num_file.close()