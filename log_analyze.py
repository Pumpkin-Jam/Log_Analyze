from glob import glob
import re

talk_data_file = open("talkdata.csv", "w")
write_file = open("test_logs1.txt", "w")
talk_data_dict = {}

for file in glob("D:/人狼知能開発/Past Log/GAT2017Log05/gat2017log05" + "/*/*.log"):
    log_data = open(file)
    talks = []
    day_talk = []
    day = 0
    
    for line in log_data:
        line = line.replace("\n", "")
        lines = line.split(",")
        if lines[0] != str(day):
            talks.append(day_talk)
            day_talk = []
            day += 1
            #print(talks)
            #print(day, lines[0])
        if lines[1] == "talk":
            text = lines[5]
            talker = lines[4]
            words = text.split(" ")
            if words[0] == "AGREE" or words[0] == "DISAGREE":
                if words[1] == "TALK":
                    day_search = re.search(r"[0-9]+", words[2])
                    talk_ID_search = re.search(r"[0-9]+", words[3])
                    
                    day_ = int(day_search.group())
                    talk_ID = int(talk_ID_search.group())
                    #print(day_, talk_ID)
                    
                    if day == day_:
                        text = words[0] + " " + day_talk[talk_ID]
                    else:
                        text = words[0] + " " + talks[day_][talk_ID]
            
            day_talk.append(text)
            write_text = "{}:{}".format(talker, text)
            #print(write_text)
            write_file.write(write_text + "\n")
            
            is_found = False
            counter = 0
            for key, value in talk_data_dict.items():
                if key==write_text:
                    is_found = True
                    value = [value[0], value[1]+1]
                    talk_data_dict[key] = value
                    #print(value)
                    break
                counter += 1
                
            if not is_found:
                talk_data_dict[write_text] = [counter, 1]
            #print(talk_data_dict)

    log_data.close()

write_file.close()

for key, value in talk_data_dict.items():
    talk_data_file.write(key + "," + str(value[0]) + "," + str(value[1]) + "\n")

talk_data_file.close()
