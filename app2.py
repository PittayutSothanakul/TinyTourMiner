from flask import Flask , render_template , request, url_for
from flask_bootstrap import Bootstrap
import json
import numpy as np
from matplotlib.widgets import Button
import matplotlib.image as mpimg
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map



app = Flask(__name__);
app.config['GOOGLEMAPS_KEY'] = "AIzaSyCDFpbv2jUwFTzHJ2Lo0odL52OJ0r3DX8o"

Bootstrap(app)
GoogleMaps(app, key="AIzaSyCDFpbv2jUwFTzHJ2Lo0odL52OJ0r3DX8o")


@app.route("/mapview", methods=["GET", "POST"])
def mapview():
    # creating a map in the view

    mymap = Map(
        identifier="view-side",
        lat= 36.2048,
        lng= 138.2529,
        markers=[(33.9567931, 131.2709503)] ,
        zoom = 4.5  ,
        style = "height:400px;width:500px;margin:auto;"

    )

  
    return render_template('mapview.html', mymap=mymap)

@app.route("/", methods=["GET", "POST"])
def start():
    
    return render_template('home.html')


@app.route("/region", methods=["GET", "POST"])
def region():

    
    return render_template('region.html', testtext = testtext)
    
travel_record1 = ""
travel_record2 = ""
travel_record3 = ""
travel_record4 = ""
travel_record5 = ""

array_record1 = []
array_record2 = []
array_record3 = []
array_record4 = []
array_record5 = []
array_latitude = []
array_longitude = []
array_longlat =[]

check_date = ""
text_date = ""
text_time = ""
text_category = ""
text_plcename = ""
array_date =[]
array_time = []
array_category = []
array_location = []


user1=""
user2=""
user3=""
user4=""
user5=""


@app.route('/interest', methods=['POST'])
def my_form_post():
    country = request.form['country']

    cat1 = request.form['category1']
    cat2 = request.form['category2']
    cat3 = request.form['category3']
    cat4 = request.form['category4']
    cat5 = request.form['category5']

    country_text = country
    cate_text = cat1+cat2+cat3+cat4+cat5


    #result = main_v2({'Temple':1},'JP')
    result = main_v2({str(cat1):1},country)
    # print(cat1)
    
    mymap = Map(
        identifier="view-side",
        lat= 36.2048,
        lng= 138.2529,
        markers=[ i for i in zip(array_longitude,array_latitude )] ,
        # markers=[(array_longitude[0], array_latitude[0]) , (array_longitude[1], array_latitude[1])] ,
        # markers=[(33.9567931, 131.2709503)] ,
        # markers=[(35.009186, 135.7743)] ,
         
        zoom = 4.5  ,
        style = "height:400px;width:500px;margin:auto;"

    )




    print("==================== Test Load ====================")  
    print(array_longitude[1])
    print(array_latitude[1])
    # print(array_record1)    
    # print(array_record2)    
    # print(array_record3)    
    # print(array_record4)    
    # print(array_record5)    
    print("==================== Finished Load ====================")   


    return render_template('mapview.html'
    , country_text = country_text , cate_text = cate_text , mymap = mymap
    , text_date = text_date , text_plcename = text_plcename , text_time = text_time
    , array_category = array_category, array_location=array_location , array_date= array_date
    , array_record1=array_record1 , array_record2=array_record2 , array_record3=array_record3 , array_record4=array_record4 , array_record5=array_record5
    , user1=user1,user2=user2,user3=user3,user4=user4,user5=user5,)

@app.route("/interest", methods=["GET", "POST"])
def home():
    with open('categories.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())


    with open('countries.json', encoding='utf-8') as country_file:
        country = json.loads(country_file.read())

    all_interest = [];
    all_countries = [];
    arrayTest = ["thai","japan"];
    country_list =  [d['name'] for d in country] 

    AllBigName = data["response"]["categories"]

    for bigName in AllBigName:
        big_category = bigName["name"]
        all_interest.append(big_category)
        for midName in bigName["categories"]:
            mid_category = midName["name"]
            all_interest.append(mid_category)
            for smallName in midName["categories"]:
                small_category = smallName["name"]
                all_interest.append(small_category)
                for tinyName in smallName["categories"]:
                    tiny_category = tinyName["name"]
                    all_interest.append(tiny_category)
                    
    country_list.sort()
    all_interest.sort()

    return render_template('interest.html', all_country_list = country_list ,all_list_interest = all_interest , all_interest1 = enumerate(all_interest) , all_interest2 = enumerate(all_interest) , all_interest3 = enumerate(all_interest) , all_interest4 = enumerate(all_interest) , all_interest5 = enumerate(all_interest) )



@app.route("/index2")
def index():
    with open('categories.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    all_interest = [];
    AllBigName = data["response"]["categories"]
    for bigName in AllBigName:
        big_category = "Main Categories : " + bigName["name"]
        all_interest.append(big_category)
        for midName in bigName["categories"]:
            mid_category = "  Sub Categories : " + midName["name"]
            all_interest.append(mid_category)
            # for smallName in midName["categories"]:
            #     small_category = "    Small Categories : " + smallName["name"]
            #     all_interest.append(small_category)
                # for tinyName in smallName["categories"]:
                #     tiny_category = "       Current Tiny : " + tinyName["name"]
                #     all_interest.append(tiny_category)
  
    return render_template('index.html' , all_interest = enumerate(all_interest) , all_interest2 = enumerate(all_interest) , all_interest3 = enumerate(all_interest) )

@app.route("/index2")
def index3():
    with open('categories.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    all_interest = [];
    AllBigName = data["response"]["categories"]
    for bigName in AllBigName:
        big_category = "Main Categories : " + bigName["name"]
        all_interest.append(big_category)
        for midName in bigName["categories"]:
            mid_category = "  Sub Categories : " + midName["name"]
            all_interest.append(mid_category)
            # for smallName in midName["categories"]:
            #     small_category = "    Small Categories : " + smallName["name"]
            #     all_interest.append(small_category)
                # for tinyName in smallName["categories"]:
                #     tiny_category = "       Current Tiny : " + tinyName["name"]
                #     all_interest.append(tiny_category)
  
    return render_template('index3.html' , all_interest1 = enumerate(all_interest) , all_interest2 = enumerate(all_interest) , all_interest3 = enumerate(all_interest) , all_interest4 = enumerate(all_interest) , all_interest5 = enumerate(all_interest) )


# @app.route("/")
# def index2():
#     with open('categories.json', encoding='utf-8') as data_file:
#         data = json.loads(data_file.read())

#     with open('countries.json', encoding='utf-8') as country_file:
#         country = json.loads(country_file.read())

#     all_interest = [];
#     AllBigName = data["response"]["categories"]
#     for bigName in AllBigName:
#         big_category = "Main Categories : " + bigName["name"]
#         all_interest.append(big_category)
#         for midName in bigName["categories"]:
#             mid_category = "  Sub Categories : " + midName["name"]
#             all_interest.append(mid_category)
#             # for smallName in midName["categories"]:
#             #     small_category = "    Small Categories : " + smallName["name"]
#             #     all_interest.append(small_category)
#                 # for tinyName in smallName["categories"]:
#                 #     tiny_category = "       Current Tiny : " + tinyName["name"]
#                 #     all_interest.append(tiny_category)
#     country_list =  [d['name'] for d in country] 
#     print (country_list[0])
#     return render_template('index2.html' , country_list = [d['name'] for d in country] , all_interest1 = enumerate(all_interest) ,  all_interest2 = enumerate(all_interest)  , all_interest3 = enumerate(all_interest)  , all_interest4 = enumerate(all_interest)  , all_interest5 = enumerate(all_interest)    )

@app.route("/search" ,methods=['POST'])
def search():
    #take all parameter
    input_country = request.form['country']
    interest1 = request.form['interest1']
    weight1 = request.form['weight1']
    interest2 = request.form['interest2']
    weight2 = request.form['weight2']
    interest3 = request.form['interest3']
    weight3 = request.form['weight3']
    interest4 = request.form['interest4']
    weight4 = request.form['weight4']
    interest5 = request.form['interest5']
    weight5 = request.form['weight5']

    input_dict = {}
    input_dict.update({interest1:weight1})
    input_dict.update({interest2:weight2})
    input_dict.update({interest3:weight3})
    input_dict.update({interest4:weight4})
    input_dict.update({interest5:weight5})
    
    #{'Music Venue' : 1 , 'Food' : 2},'US'
    #dict_ver = json.loads(input_interest)
    #print("Result from web"  + input_interest +",Country " + input_country+",Weight " + input_weight)
    result = "Hey"
    input = input_country
    #result = main_v2(dict_ver , input_country)
    # result = main_v2({'Music Venue' : 1 , 'Food' : 2},'US')
    return render_template('result.html', result = result , input = input)


@app.route("/plot", methods=["GET", "POST"])
def plot():

    input_interest = request.form['interest']
    input_country = request.form['country']
    #{'Music Venue' : 1 , 'Food' : 2},'US'
    result = main_v2(input_interest , input_country)

    return render_template('plot.html', result = result , input = input)




# Ver 21.6 ANDに対応 main_v2({"Train Station":3 , "Mall" : 3} , "JP")は
# (Train Station || Platform || Train) &&  Mallという解釈
# AND検索する場合は316行目でget_similarity_ANDを使う。従来通りの場合get_similarityを使う
# Ver 21. ①Sum Weight計算を変更。DataBaseのBugで全く同時刻に同じVENUEのcheckinが
# 見つかっため、previous_venue と previous_date を用いて、Sum Weightに加わらないようにした。
# ② 比較的に短いTravel Record(checkin数が例えば5箇所以下)を除外するために、
# main_v2()内に、元々の if len(row[i]) > 0 : の行を 
# if len(row[i]) > 0 and int(row[i+1]) > 5: に変更。5は適宜に変更して下さい。
# ③ 入力国がJPとSGの場合、プログラムが自動的にそれらの国のCSVファイルを使うようにした。
# ver 14. VENUE_NAME 出力のDEBUGを行った。SELECT VENUE_ID, LATITUDE, LONGITUDE, COUNTRY, HOME, CATEGORY, DATE FROM
# ver.11 Tiny_categoryのDebug @2018_1218 14:00 
# ver.10 Country Name がJPの場合だけ、VENUE_NAMEを出力
# ver.9  重みがマイナスの場合でも対応できるように絶対値(abs)を使用 @2018_1215
# 重み入力対応＋ 結果をoutput_resultへ出力(output_result.txt)
# main_v2 の実行形式, 重みは必ず指定すること。デフォルト値として1を入れること。
# main_v2({'Jazz Club':2,'Museum':1},'US')
# main_v2({'Jazz Club':-2,'Museum':5},'US')

from datetime import datetime
from math import sqrt
import csv
import sys
import json
import numpy as np
from matplotlib.widgets import Button
import matplotlib.image as mpimg


# 以下は BigQueryや地図表示するためのImport。
from bigquery import get_client
from bigquery.errors import BigQueryTimeoutException
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#以下の Gloval Variable をMain_v2内へ移動」
#dataset = {}
#countryset = {}

# 新しいバージョンの Main
def main_v2(all_interest, country):
   
    dataset = {}
    countryset = {}
    if len(dataset) == 0:
        
        input_dict_category = {}
        
        all_interest_all_category = {}
        original_input = all_interest
        #create the test user and put him in dataset
        for interest_location , weight_score  in all_interest.items():
            #print("input interest " + interest_location)
            subset_category = take_input(interest_location)
            #print(subset_category)
            for item in subset_category:
                # person0 を作成
                input_dict_category.update({item : 1 }) # 該当するカテの重み＝1,Dictに入れる
#                input_dict_category.update({interest_location : 1 })
                # TODO convert from weight score into multiplyier
                
                #update alternative
                #all_interest_all_category.update({item : weight_score})
                all_interest_all_category[item] = weight_score # 該当するカテに入力重み(1~5を適用)
#                all_interest_all_category[interest_location] = weight_score
                #print(all_interest_all_category)
        dataset["0"] = input_dict_category; # User0 を datasetに入れる
        all_interest = all_interest_all_category # Sub-Category＋重みをall_interestとして代入
        #transform the input all_interest into smaller category
        reader = ""
        print('Loading Traverler-Interest file...')
        if (country == "JP"):
            print ("Using JP Record")
            with open("./Traveler_Interest_JP.csv", "r") as csvfile:   
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 0: #空の行に対応するため
                        break         #空の行に対応するため    
                    if(row[0]=='USER_ID'):
                        continue
                    category_frequency = {}
                    for i in range(1, len(row), 2):
                        if len(row[i]) > 0:
                            category_frequency[row[i]] = int(row[i + 1])
                        dataset[row[0]] = category_frequency
                    apply_weight(dataset[row[0]] , all_interest) #Weight（重み）
        elif (country == "SG"):
            print ("Using SG Record")
            with open("./Traveler_Interest_SG.csv", "r") as csvfile:   
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 0: #空の行に対応するため
                        break         #空の行に対応するため    
                    if(row[0]=='USER_ID'):
                        continue
                    category_frequency = {}
                    for i in range(1, len(row), 2):
                        if len(row[i]) > 0:
                            category_frequency[row[i]] = int(row[i + 1])
                        dataset[row[0]] = category_frequency
                    apply_weight(dataset[row[0]] , all_interest) #Weight（重み）
        else:
            print('Using All Traverler-Interest Data')
            with open("./Traveler_Interest_all.csv", "r") as csvfile:   
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 0: #空の行に対応するため
                        break         #空の行に対応するため    
                    if(row[0]=='USER_ID'):
                        continue
                    category_frequency = {}
                    for i in range(1, len(row), 2):
                        if len(row[i]) > 0:
                            category_frequency[row[i]] = int(row[i + 1])
                        dataset[row[0]] = category_frequency
                    apply_weight(dataset[row[0]] , all_interest) #Weight（重み）
 
# 評価値の実験用に、以下３つのコマンドを ON-OFF の組み合わせでやる
                    
# 正規化適応 (normalize)          
#                normalize(dataset[row[0]] )
                    
# 偏差値以下を除外 (outlier)                
#                remove_outlier(dataset[row[0]])
                    
# 現時点では、Weight（重み）は必ず入れるようにする。                    
                #apply_weight(dataset[row[0]] , all_interest)
                
                #break;
                #print(dataset[row[0]])                     
      
    if len(countryset) == 0:
        print('Loading Traveler-Country file...')
#        with open("./Travelers_Countries_1_89308.csv", "r") as csvfile:
        with open("./Traveler_Countries_all.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
# ver17 CSVの中に空の行があっても対応できるようにした。
            for row in reader:
                if len(row) == 0: #空の行に対応するため
                    break         #空の行に対応するため 
# ver21 if len(row[i]) > 0 の行に and int(row[i+1]) > 5: を追加した。              
                country_frequency = {}
                for i in range(1, len(row), 2):
                    if len(row[i]) > 0 and int(row[i+1]) > 5:
                        country_frequency[row[i]] = int(row[i + 1])
                    countryset[row[0]] = country_frequency
    rankings = []
    # print(get_recommend(rankings, "0", country, 10))
    # Pattara が 3人だけ表示に修正した（時間短縮のため）
    print('Original Input from User:')
    print(original_input, country, "\n")  # Debug用
# v21.6 get_recommendの引数にoriginal_inputを追加
    rankings = get_recommend(rankings, "0", country, 5 , dataset , countryset, original_input)
    if (rankings == "Error"):
        print("No record match ! Terminate Program !")
        return 
    print('Top Rankings:', rankings, "\n")
    visualize("0", country, rankings , all_interest, original_input) 
 
# show_category() はFourSquareの全カテゴリーを試し出力（jsonファイルから）
def show_category():
    all_interest = []
    with open('categories.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    AllBigName = data["response"]["categories"]
    for bigName in AllBigName:
        big_category = "Current Big : " + bigName["name"]
        all_interest.append(big_category)
        for midName in bigName["categories"]:
            mid_category = "  Current Middle : " + midName["name"]
            all_interest.append(mid_category)
            for smallName in midName["categories"]:
                small_category = "    Current Small : " + smallName["name"]
                all_interest.append(small_category)
                for tinyName in smallName["categories"]:
                    tiny_category = "       Current Tiny : " + tinyName["name"]
                    all_interest.append(tiny_category)
 
#    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#    f = open("output_gaterory" +timestamp+ ".txt", "w" ,encoding='utf-8')
    f = open("output_gaterory.txt", "w" ,encoding='utf-8')
    for item in all_interest:
        f.write(item+"\n")  
 
# take_input() はUserが指定するカテゴリー名及びその下階層のサブカテゴリーを全て出力
# tiny_category(Categoryの4階層目)に適用できるようにDebugした
# Stringを入力と出来るようにしました。(2018_1212更新)
# 実行例① take_input(['Music Venue'])
# 実行例② take_input(['Music Venue','Travel & Transport'])    
import json
 
def take_input(all_interest):
    all_input_interest = [];
    if type(all_interest) == str:
        receive = all_interest
        all_interest = []
        all_interest.append(receive)
    with open('categories.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    clean_data = data["response"]["categories"]
    for interest in all_interest:
        counter =0
        #print(interest)
        for big_name in clean_data:
            if(interest == big_name["name"]):
                counter = 1
                #find and add the rest subcategory
                all_input_interest.append(big_name["name"])
                for mid_name in big_name["categories"]:
                    all_input_interest.append(mid_name["name"])
                    for small_name in mid_name["categories"]:
                        all_input_interest.append(small_name["name"])
                        for tiny_name in small_name["categories"]:
                            all_input_interest.append(tiny_name["name"])
  
            for mid_name in big_name["categories"]:
                if(interest == mid_name["name"]):
                    counter = 1
                    all_input_interest.append(mid_name["name"])
                    for small_name in mid_name["categories"]:
                        all_input_interest.append(small_name["name"])
                        for tiny_name in small_name["categories"]:
                            all_input_interest.append(tiny_name["name"])
  
                for small_name in mid_name["categories"]:
                    if(interest == small_name["name"]):
                        counter = 1
                        all_input_interest.append(small_name["name"])
                        for tiny_name in small_name["categories"]:
                            all_input_interest.append(tiny_name["name"])
                        
                    for tiny_name in small_name["categories"]:
                        if(interest == tiny_name["name"]):
                            counter = 1
                            all_input_interest.append(tiny_name["name"])
        if (counter == 0):
            all_input_interest.append(interest)
#     #WRITE FILE
#     f = open("take_input_output.txt", "w" )
#     for item in all_input_interest:
#         f.write(item)\

    return all_input_interest
 
# 2018_1225 person1のチェックインしたカテゴリ集合⊆person2のチェックインしたカテゴリ集合でなければ
# (person2がperson1のチェックインしたカテゴリを全て訪問していなければ)類似度0とする
# 
# 2018_1215 重みがマイナスの場合でも対応できるように  
#    union_num += absdataset[person1][union] を
#    union_num += abs(dataset[person1][union]) に変更 
# 旅行者person1とperson2の類似度[0, 1]を計算する
# ここでのperson1とperson2の類似度の定義
# person1とperson2の両方がチェックしたカテゴリをCとする
# 類似度　=
# person1がCにチェックインした回数 + person2がCにチェックインした回数 /
# person1のチェックイン総数 + person2のチェックイン総数
# ただしCが空集合の場合、類似度0とする
    
def get_similarity(person1, person2, dataset):
    set_person1 = set(dataset[person1].keys())
    set_person2 = set(dataset[person2].keys())
    #person1とperson2の両方がチェックしたカテゴリがない
    if len(set_person1.intersection(set_person2)) == 0:
        return 0
    #if not set_person1 <= set_person2:
     #   return 0
    # person1とperson2の両方がチェックしたカテゴリがある
    inter_num = 0
    union_num = 0
    for inter in set_person1.intersection(set_person2):
        inter_num += dataset[person1][inter]
        inter_num += dataset[person2][inter]
    for union in set_person1.union(set_person2):
        if union in dataset[person1]:
            union_num += abs(dataset[person1][union])
        if union in dataset[person2]:
            union_num += abs(dataset[person2][union])
    return inter_num / union_num

def get_similarity_AND(person1, person2, dataset, original_input):
    set_person1 = set(dataset[person1].keys())
    set_person2 = set(dataset[person2].keys())
    #person1とperson2の両方がチェックしたカテゴリがない
    if len(set_person1.intersection(set_person2)) == 0:
        return 0
# AND対応
    original_input_list = list(original_input)
    expanded_input = take_input(original_input)
    for i in range(len(original_input_list)):
        j = expanded_input.index(original_input_list[i])
        if i < len(original_input_list)-1:
            k = expanded_input.index(original_input_list[i+1])
        else:
            k = len(expanded_input)
        if len(set(expanded_input[j:k]).intersection(set_person2)) == 0:
#            print("not found:" + str(set(expanded_input[j:k])))# + "###" + str(set_person2))
            return 0
    #if not set_person1 <= set_person2:
     #   return 0
    # person1とperson2の両方がチェックしたカテゴリがある
#    print("OK:" + str(expanded_input))
    inter_num = 0
    union_num = 0
    for inter in set_person1.intersection(set_person2):
        inter_num += dataset[person1][inter]
        inter_num += dataset[person2][inter]
    for union in set_person1.union(set_person2):
        if union in dataset[person1]:
            union_num += abs(dataset[person1][union])
        if union in dataset[person2]:
            union_num += abs(dataset[person2][union])
    return inter_num / union_num

 
# 旅行者personに類似する他の旅行者を上位top_Nまでランキングする
def get_recommend(rankings, person, country, top_N , dataset , countryset, original_input):
    counter = 0
    for other in list(dataset.keys()):
        if person != other: # 自分を除く
            if country in countryset[other].keys(): # 他の旅行者がcountryを訪問してるか？
# v21_6 AND対応
#                sim = get_similarity(person, other, dataset)
                sim = get_similarity_AND(person, other, dataset, original_input)
                rankings.append((sim, other))
                if (sim != 0):
                    #print(counter)
                    counter = counter + 1
    rankings.sort()
    rankings.reverse()
    if (counter == 0 ):
        return "Error"
    return [i for i in rankings][:top_N]



# ranking_number = 0

def visualize(person, country, rankings,all_interest,original_input):
    
#Outputをファイル1,2へ書き込み用の初期化   
        
    global travel_record1
    global travel_record2
    global travel_record3
    global travel_record4
    global travel_record5

    global array_record1
    global array_record2
    global array_record3
    global array_record4
    global array_record5

    global array_latitude
    global array_longitude
    global array_longlat

    global check_date
    global array_date
    global array_time
    global array_category
    global array_location
    global text_date
    global text_time
    global check_category
    global text_category
    global text_plcename

    global user1
    global user2
    global user3
    global user4
    global user5
    
    array_record1.clear()
    array_record2.clear()
    array_record3.clear()
    array_record4.clear()
    array_record5.clear()

    global ranking_number

    timestamp = datetime.now().strftime("%Y%m%d_%H_%M_%S") 
    f = open("output_result " + timestamp + ".txt", "w" ,encoding='utf-8')
    f2 = open("output_result2 " + timestamp + ".txt", "w" ,encoding='utf-8')
    f3 = open("output_result3 " + timestamp + ".txt", "w" ,encoding='utf-8')
#    f = open("output_result.txt", "w" ,encoding='utf-8')
#    f2 = open("output_result2.txt", "w" ,encoding='utf-8')




    #PROJECT_ID = 'tour-miner-project'
#    SERVICE_ACCOUNT = 'bigquery-admin@tour-miner-project-2019.iam.gserviceaccount.com'
    JSON_KEY_PATH = 'tour-miner-project-2019-511090dd4bd9.json'
    # BigQueryClientの取得
    client = get_client(json_key_file=JSON_KEY_PATH, readonly=True)
       
    #Interest Keyとその重みを表示
    print("Matched Interested Category: ") 
    for key , value in all_interest.items():
        sys.stdout.write(key + ":" +str(value) +",")
#    print("\n")
    
# Output2への書き込み用； Interest Keyとその重みをHeaderとして書き込む
    f2.write("Input Country from User: " + country + "\n")
    f2.write("Input Interested Category from User: ")
    for key , value in original_input.items():
        f2.write(key + ":" +str(value) +",")
    f2.write("\nMatched Interested Category: \n") 
    for key , value in all_interest.items():
        f2.write(key + ":" +str(value) +",")
    f2.write("\n \n")
    f2.write("Top Rankings (Similarity,User Name): " + str(rankings)+ "\n \n")
    
    
    
#Output 3 
    f3.write("Input Country from User: " + country + "\n")
    f3.write("Input Interested Category from User: ")
    for key , value in original_input.items():
        f3.write(key + ":" +str(value) +",")
    f3.write("\nMatched Interested Category: \n") 
    for key , value in all_interest.items():
        f3.write(key + ":" +str(value) +",")
    f3.write("\n \n")
    f3.write("Top Rankings (Similarity,User Name): " + str(rankings)+ "\n \n")



    # print(len(rankings))
    ranking_number = 0
    while ranking_number < 5 :
        for u in rankings:

            #check user, Which that 

            user1= rankings[0][1]
            user2= rankings[1][1]
            user3= rankings[2][1]
            user4= rankings[3][1]
            user5= rankings[4][1]


            if(ranking_number == len(rankings)) :
                ranking_number = 0

            user = np.array(rankings[ranking_number])
            if(u[1] == user[1]) :
                
            # queryの実行
                print("\nUser:" + u[1])
                query = 'SELECT VENUE_ID, LATITUDE, LONGITUDE, COUNTRY, HOME, CATEGORY, DATE FROM dataset_TIST2015.Checkins_POIs_Travel_marked WHERE USER_ID = '          + u[1] + ' and TRAVEL = 1 and COUNTRY = \'' + country + '\''
                #print(query)

                try:
                    job_id, results = client.query(query, timeout=60)
                except BigQueryTimeoutException as e:
                    print('Exception')

                # 日付のフォーマットを変換
                for q in results:
                    q['DATE'] = q['DATE'][4:]
                    Mon = q['DATE'][:3]
                    q['DATE'] = q['DATE'][4:]
                    if Mon == "Jan":
                        q['DATE'] = "01" + q['DATE']
                    if Mon == "Feb":
                        q['DATE'] = "02" + q['DATE']
                    if Mon == "Mar":
                        q['DATE'] = "03" + q['DATE']
                    if Mon == "Apr":
                        q['DATE'] = "04" + q['DATE']
                    if Mon == "May":
                        q['DATE'] = "05" + q['DATE']
                    if Mon == "Jun":
                        q['DATE'] = "06" + q['DATE']
                    if Mon == "Jul":
                        q['DATE'] = "07" + q['DATE']
                    if Mon == "Aug":
                        q['DATE'] = "08" + q['DATE']
                    if Mon == "Sep":
                        q['DATE'] = "09" + q['DATE']
                    if Mon == "Oct":
                        q['DATE'] = "10" + q['DATE']
                    if Mon == "Nov":
                        q['DATE'] = "11" + q['DATE']
                    if Mon == "Dec":
                        q['DATE'] = "12" + q['DATE']
                    YEAR = q['DATE'][len(q['DATE'])-4:len(q['DATE'])]
                    q['DATE'] = YEAR + q['DATE'][:len(q['DATE'])-4]
            
                # 結果の表示
                results.sort(key=lambda x: x['DATE'])

                total_weight = 0     
                time_counter = 0
                
                previous_venue = "" # Version21で追加
                previous_date = ""  # Version21で追加

                # lngs = [float(q['LONGITUDE']) for q in results]
                # lats = [float(q['LATITUDE']) for q in results]

        # 入力される Country Nameが JPの時だけ VENUE_NAMEで出力するように対応        
                location_name_dictionary = {}
                if (country == "JP"):
                    location_name_dictionary = location_name = get_venue_names_from_venue_ids([q['VENUE_ID'] for q in results])
                location_name = ""
                previous_venue = "0"
                for q in results:

                    if q['VENUE_ID'] in location_name_dictionary:
                        location_name2 = location_name_dictionary[q['VENUE_ID']]
                    else:
                        location_name2 = q['VENUE_ID']   

                    check_date = q['DATE']
                    array_date.append(check_date.split(" ")[0])
                    array_time.append(check_date.split(" ")[1])
                    array_category.append(q['CATEGORY'])
                    array_location.append(location_name2)

                    text_date = check_date.split(" ")[0]
                    text_time = check_date.split(" ")[1] 
                    check_category = q['CATEGORY']
                    text_category = q['CATEGORY']
                    text_plcename = location_name2

                    counter = 0 
                    for key_category , weight in all_interest.items():
                        if (key_category == q['CATEGORY']):
                            counter = weight

                    if(ranking_number==0) :
                        travel_record1 = (q['DATE']  + q['CATEGORY']  + location_name + " "+ location_name2)
                        array_latitude.append(str(float(q['LONGITUDE'])))
                        array_longitude.append(str(float(q['LATITUDE'])))
                        array_record1.append(travel_record1)


                    elif(ranking_number==1) :
                        travel_record2 = (q['DATE']  + q['CATEGORY']  + location_name + " "+ location_name2)
                        array_record2.append(travel_record2)


                    elif(ranking_number==2) :
                        travel_record3 = (q['DATE']  + q['CATEGORY']  + location_name + " "+ location_name2)
                        array_record3.append(travel_record3)
  

                    elif(ranking_number==3) :
                        travel_record4 = (q['DATE']  + q['CATEGORY']  + location_name + " "+ location_name2)
                        array_record4.append(travel_record4)


                    elif(ranking_number==4) :
                        travel_record5 = (q['DATE']  + q['CATEGORY']  + location_name + " "+ location_name2)
                        array_record5.append(travel_record5)

                print(q['DATE'] + ', ' + q['CATEGORY'] + ', ' + location_name + ", Weight:" + str(counter))






        #          print(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + q['VENUE_ID'])
            
    # Output1へ書き込み:主観的評価用（岡部さん用）:ここから
                f = open("output_result " + timestamp + ".txt", "a" ,encoding='utf-8')
    #          f = open("output_result.txt", "a" ,encoding='utf-8')
                
                writing_information =(q['DATE'] + ', ' + q['CATEGORY'] + ', ' + location_name + ", Weight:" + str(counter) + ", Similarity:" + str("{0:.4f}".format(u[0])))  
        #          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + get_venue_name_from_venue_id(q['VENUE_ID']) + ",weight:" + str(counter))  
                f.write(("user:" + u[1]) + ', ')  
                f.write(writing_information+"\n")  
    # Output1へ書き込み：ここまで
            
    # Output2へ書き込み:客観的評価用（パッタラ用）:ここから          
                counter = 0 
    #          print(q['VENUE_ID'])
                if (previous_venue != q['VENUE_ID'] and previous_date != q['DATE']):             
                    for key_category , weight in all_interest.items():
                        if (key_category == q['CATEGORY']):
                            time_counter += 1  
                            counter = weight
                            total_weight += weight
                previous_venue = q['VENUE_ID']
                previous_date = q['DATE']
                
                writing_information =(q['DATE'] + ', ' + q['CATEGORY'] + ', ' + location_name + ", Weight:" + str(counter))  
                f2.write(("user:" + u[1]) + ',')  
                f2.write(writing_information+"\n") 
                
                if (counter>0):
                    writing_information =(q['DATE'] + ', ' + q['CATEGORY'] + ', ' + location_name + ", Weight:" + str(counter))  
                    f3.write(("user:" + u[1]) + ',')  
                    f3.write(writing_information+"\n") 
                
                
                f2.write("Sum Weight = " + str(total_weight) + ", Similarity = " + str("{0:.4f}".format(u[0])) + ", Number of correspond place = "+ str(time_counter) + "\n \n")
                f3.write("Sum Weight = " + str(total_weight) + ", Similarity = " + str("{0:.4f}".format(u[0])) + "\n \n")
        ranking_number = ranking_number + 1


#   上記Debug用  


# get_venue_name_from_venue_id() の実行例 
# get_venue_name_from_venue_id('4b569977f964a520551628e3')
# 東京スカイツリー(TokyoSkyTree)
def get_venue_name_from_venue_id(venue_id):
    #PROJECT_ID = 'tour-miner-project'
#    SERVICE_ACCOUNT = 'bigquery-admin@tour-miner-project.iam.gserviceaccount.com'
#    JSON_KEY_PATH = 'tour-miner-project-8873e737b27c.json'
    SERVICE_ACCOUNT ='bigquery-admin@tour-miner-project-2019.iam.gserviceaccount.com'
    JSON_KEY_PATH = 'tour-miner-project-2019-511090dd4bd9.json'    
    
    # BigQueryClientの取得
    client = get_client(json_key_file=JSON_KEY_PATH, readonly=True)

    query = '#standardSQL\nSELECT VENUE_NAME FROM `tour-miner-project.dataset_TIST2015.JP_VENUE_DICTIONARY` WHERE VENUE_ID = \'' + venue_id + '\' LIMIT 1'
#    print(query)

    try:
        job_id, results = client.query(query, timeout=60)
    except BigQueryTimeoutException as e:
        print(e)

    #venue_idと  VENUE_NAMEが該当しない時にエラーが出るため改良した
    #print(results[0]['VENUE_NAME'])
    if len(results)==0:
        return '該当なし'
    else:
        return (results[0]['VENUE_NAME'])

# Venue idのリストを名前のリストに一括変換する関数
# 2018年12月時点では、JPに限定されることに注意
# Input: List of venue id, ex. ['4d96a21fc19fb60c41908365', '4e478efcd164155c0df4bafc']    
# Output Dictionary of venue name (key: venue id, value venue name)
# {'VENUE_NAME': '上野動物園パンダ舎(GiantPandasCage-', 'VENUE_NAME': '上野動物園カピバラ舎'}
def get_venue_names_from_venue_ids(venue_id_list):
    #PROJECT_ID = 'tour-miner-project'
#    SERVICE_ACCOUNT = 'bigquery-admin@tour-miner-project.iam.gserviceaccount.com'
#    JSON_KEY_PATH = 'tour-miner-project-8873e737b27c.json'
#    SERVICE_ACCOUNT ='bigquery-admin@tour-miner-project-2019.iam.gserviceaccount.com'
    JSON_KEY_PATH = 'tour-miner-project-2019-511090dd4bd9.json'    
    
    # BigQueryClientの取得
    client = get_client(json_key_file=JSON_KEY_PATH, readonly=True)
    
    where_phrase = ''
    for i in range(len(venue_id_list)):
        where_phrase += "VENUE_ID = \'" + venue_id_list[i] + "\'"
        if i < len(venue_id_list) - 1: # 最後でなければORをつける
            where_phrase += ' or '
#    query = '#standardSQL\nSELECT VENUE_ID, VENUE_NAME FROM `tour-miner-project.dataset_TIST2015.JP_VENUE_DICTIONARY` WHERE ' + where_phrase
    query = '#standardSQL\nSELECT VENUE_ID, VENUE_NAME FROM `tour-miner-project-2019.dataset_TIST2015.JP_VENUE_DICTIONARY` WHERE ' + where_phrase
 #   print(query)

    try:
        job_id, results = client.query(query, timeout=60)
    except BigQueryTimeoutException as e:
        print(e)
 #   print(results)
    location_name_dictionary = {}
    for q in results:
        location_name_dictionary[q['VENUE_ID']] = q['VENUE_NAME']
    return location_name_dictionary


# 重みを与えるためのサブルーチン
def apply_weight(current_dataset , all_interest):
    #print(all_interest)
    for dataset_key , dataset_value in current_dataset.items():
        for interest_key , interest_value in all_interest.items():
            if(dataset_key == interest_key):
                current_dataset[dataset_key] *= interest_value
                #print("KEY IS " + dataset_key)

# 正規化計算 (ver10から追加)               
def normalize(current_dataset):

    minimum_value = 0
    maximum_value = 0
    
    #Find Max and Min 
    for dataset_value in current_dataset.values():
        #print(dataset_value)
        if(maximum_value < dataset_value):
            maximum_value = dataset_value
        
        if(minimum_value > dataset_value ):
            minimum_value = dataset_value
            
    #normalize 
    for dataset_key , dataset_value in current_dataset.items():
        new_value = ( dataset_value - minimum_value ) / (maximum_value - minimum_value )
        current_dataset[dataset_key] = new_value

# 偏差値以下のデータを取り除く (ver10から追加)       
# main_v2({'Jazz Club':2,'Museum':1},'US')
# main_v2({'Temple':1},'JP')

# main_v2({'Spiritual Center':1},'JP')

def remove_outlier(current_dataset):
    #if length is only 1 then do nothing
    if (len(current_dataset) == 1):
        return
    
    #find stdev
    current_stdev = statistics.stdev(current_dataset.values())
    category_to_remove = []
    #check  outlier
    for dataset_key , dataset_value in current_dataset.items():
        if (current_stdev > dataset_value):
            category_to_remove.append(dataset_key)
    
    #remove outlier
    for item_to_remove in category_to_remove:
        current_dataset.pop(item_to_remove)
if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(debug=True,use_reloader=True)