from flask import Flask , render_template , request
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__);
Bootstrap(app)

@app.route("/home", methods=["GET", "POST"])
def start():
    
    return render_template('home.html')

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


@app.route("/")
def index2():
    with open('categories.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    with open('countries.json', encoding='utf-8') as country_file:
        country = json.loads(country_file.read())

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
    country_list =  [d['name'] for d in country] 
    print (country_list[0])
    return render_template('index2.html' , country_list = [d['name'] for d in country] , all_interest1 = enumerate(all_interest) ,  all_interest2 = enumerate(all_interest)  , all_interest3 = enumerate(all_interest)  , all_interest4 = enumerate(all_interest)  , all_interest5 = enumerate(all_interest)    )

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




# ver 14. VENUE_NAME 出力のDEBUGを行った。
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

# 以下は BigQueryや地図表示するためのImport。
from bigquery import get_client
from bigquery.errors import BigQueryTimeoutException
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap

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
                input_dict_category.update({item : 1 })
                # TODO convert from weight score into multiplyier
                
                # 
                #update alternative
                #all_interest_all_category.update({item : weight_score})
                all_interest_all_category[item] = weight_score
                #print(all_interest_all_category)
        dataset["0"] = input_dict_category;
        all_interest = all_interest_all_category
        #transform the input all_interest into smaller category
       
        print('Loading Traverler-Interest file...')
        with open("./Traveler_Interest_all.csv", "r") as csvfile:   
 #       with open("./Traveler_Interest_1_89308.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
# ver17 CSVの中に空の行があっても対応できるようにした。
            for row in reader:
                if len(row) == 0: #空の行に対応するため
                    break         #空の行に対応するため    
#                print(row)   # Debug用
                if(row[0]=='USER_ID'):
                    continue
                category_frequency = {}
                for i in range(1, len(row), 2):
                    if len(row[i]) > 0:
                        category_frequency[row[i]] = int(row[i + 1])
                    dataset[row[0]] = category_frequency
 
# 評価値の実験用に、以下３つのコマンドを ON-OFF の組み合わせでやる
                    
# 正規化適応 (normalize)          
#                normalize(dataset[row[0]] )
                    
# 偏差値以下を除外 (outlier)                
#                remove_outlier(dataset[row[0]])
                    
# 現時点では、Weight（重み）は必ず入れるようにする。                    
                apply_weight(dataset[row[0]] , all_interest)
                
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
                    
                country_frequency = {}
                for i in range(1, len(row), 2):
                    if len(row[i]) > 0:
                        country_frequency[row[i]] = int(row[i + 1])
                    countryset[row[0]] = country_frequency
    rankings = []
    # print(get_recommend(rankings, "0", country, 10))
    # Pattara が 3人だけ表示に修正した（時間短縮のため）
    rankings = get_recommend(rankings, "0", country, 3 , dataset , countryset)
    print(rankings)
    print('Calling Visualize:')   # Debug用 
    print(original_input,"\n")  # Debug用
    return visualize("0", country, rankings , all_interest, original_input) 
 
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
        #print(interest)
        for big_name in clean_data:
            if(interest == big_name["name"]):
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
                    all_input_interest.append(mid_name["name"])
                    for small_name in mid_name["categories"]:
                        all_input_interest.append(small_name["name"])
                        for tiny_name in small_name["categories"]:
                            all_input_interest.append(tiny_name["name"])
  
                for small_name in mid_name["categories"]:
                    if(interest == small_name["name"]):
                        all_input_interest.append(small_name["name"])
                        for tiny_name in small_name["categories"]:
                            all_input_interest.append(tiny_name["name"])
                        
                    for tiny_name in small_name["categories"]:
                        if(interest == tiny_name["name"]):
                            all_input_interest.append(tiny_name["name"])
#     #WRITE FILE
#     f = open("take_input_output.txt", "w" )
#     for item in all_input_interest:
#         f.write(item)\
 
    return all_input_interest
 
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
 
# 旅行者personに類似する他の旅行者を上位top_Nまでランキングする
def get_recommend(rankings, person, country, top_N , dataset , countryset):
    for other in list(dataset.keys()):
        if person != other: # 自分を除く
            if country in countryset[other].keys(): # 他の旅行者がcountryを訪問してるか？
                sim = get_similarity(person, other, dataset)
                rankings.append((sim, other))
    rankings.sort()
    rankings.reverse()
    return [i for i in rankings][:top_N]


def visualize(person, country, rankings,all_interest,original_input):
    
    #Outputをファイル1,2へ書き込み用の初期化
    
    timestamp = datetime.now().strftime("%Y%m%d_%H_%M_%S") 
    f = open("output_result " + timestamp + ".txt", "w" ,encoding='utf-8')
    f2 = open("output_result2 " + timestamp + ".txt", "w" ,encoding='utf-8')
#    f = open("output_result.txt", "w" ,encoding='utf-8')
#    f2 = open("output_result2.txt", "w" ,encoding='utf-8')
    # plt.figure(figsize=(14, 8))

 #地図を表示させたくない場合は、earth = Basemap()とearth.shadedrelief()をコメントアウトする
    #earth = Basemap()
    #earth.bluemarble()
    #earth.shadedrelief()

    #PROJECT_ID = 'tour-miner-project'
    SERVICE_ACCOUNT = 'bigquery-admin@tour-miner-project.iam.gserviceaccount.com'
    JSON_KEY_PATH = 'tour-miner-project-8873e737b27c.json'
    # BigQueryClientの取得
    client = get_client(json_key_file=JSON_KEY_PATH, readonly=True)
       
    #Interest Keyとその重みを表示
    print("Interested Category Input: ") 
    for key , value in all_interest.items():
        sys.stdout.write(key + ":" +str(value) +",")
#    print("\n")
    
# Output2への書き込み用； Interest Keyとその重みをHeaderとして書き込む
    f2.write("Original Input: \n")
    for key , value in original_input.items():
        f2.write(key + ":" +str(value) +",")
    f2.write("\nInterested Category Input: \n") 
    for key , value in all_interest.items():
        f2.write(key + ":" +str(value) +",")
    f2.write("\n \n")
    f2.write("Ranking =" + str(rankings) + "\n \n")
    
    print(len(rankings))
    web_result = ""
    for u in rankings:
        # queryの実行
        print("\nUser:" + u[1])
        query = 'SELECT VENUE_ID, LATITUDE, LONGITUDE, COUNTRY, HOME, CATEGORY, DATE FROM dataset_TIST2015.Checkins_POIs_Travel_marked WHERE USER_ID = ' \
         + u[1] + ' and TRAVEL = 1 and COUNTRY = \'' + country + '\''
        print(query)

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
        
        #以下が旧バージョン version (result結果をprintだけ)
        #print(results)
       
        total_weight = 0

# 入力あれる Country Nameが JPの時だけ VENUE_NAMEで出力するように対応        
        location_name = ""
 
        for q in results:
          if (country == "JP"):
                location_name = get_venue_name_from_venue_id(q['VENUE_ID'])
          else:
                location_name = q['VENUE_ID']
                       
          print(q['DATE'] + ',' + q['CATEGORY'] + ',' + location_name)
#          print(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + q['VENUE_ID'])
#          print(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + get_venue_name_from_venue_id(q['VENUE_ID']))
    
# Output1へ書き込み:主観的評価用（岡部さん用）:ここから
          #print ('Write file1')    #Debug用
          #print(all_interest)
          f = open("output_result " + timestamp + ".txt", "a" ,encoding='utf-8')
#          f = open("output_result.txt", "a" ,encoding='utf-8')
          counter = 0 
          for key_category , weight in all_interest.items():
              if (key_category == q['CATEGORY']):
                  counter = weight
              
          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + location_name + ",weight:" + str(counter))  
#          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + get_venue_name_from_venue_id(q['VENUE_ID']) + ",weight:" + str(counter))  
#          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + q['VENUE_ID'] + ",weight:" + str(counter))  
          f.write(("user:" + u[1]) + ',')  
          f.write(writing_information+"\n")  
# Output1へ書き込み：ここまで
        
# Output2へ書き込み:客観的評価用（パッタラ用）:ここから
          #print ('Write file2')    #Debug用      
          #print(all_interest)
          counter = 0 
          for key_category , weight in all_interest.items():
              if (key_category == q['CATEGORY']):
                  counter = weight
                  total_weight += weight
          
#          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + get_venue_name_from_venue_id(q['VENUE_ID']) + ",weight:" + str(counter))  
#          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + q['VENUE_ID'] + ",weight:" + str(counter))  
          writing_information =(q['DATE'] + ',' + q['CATEGORY'] + ',' + location_name + ",weight:" + str(counter))  
          f2.write(("user:" + u[1]) + ',')  
          f2.write(writing_information+"\n") 
          web_result += "user:" + u[1] + ',' + writing_information + "\n"
        f2.write("Weight Sum =" + str(total_weight) + "\n \n")
# Output2へ書き込み：ここまで
    
        lngs = [float(q['LONGITUDE']) for q in results]
        lats = [float(q['LATITUDE']) for q in results]
    return web_result

        #earth.drawcoastlines(color='#555566', linewidth=1)
    # 地図へ表示させる部分
        # plt.plot(lngs, lats, '-o', label=u[1]) 
        
    # plt.title('Travel Records of people who prefer checkin-spots similar to Traveler ' + person)
    # plt.legend()
    # plt.show()

# get_venue_name_from_venue_id() の実行例 
# get_venue_name_from_venue_id('4b569977f964a520551628e3')
# 東京スカイツリー(TokyoSkyTree)
def get_venue_name_from_venue_id(venue_id):
    #PROJECT_ID = 'tour-miner-project'
    SERVICE_ACCOUNT = 'bigquery-admin@tour-miner-project.iam.gserviceaccount.com'
    JSON_KEY_PATH = 'tour-miner-project-8873e737b27c.json'
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
import statistics
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
    app.run(debug=True,use_reloader=True)
