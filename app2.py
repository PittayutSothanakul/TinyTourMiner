from flask import Flask , render_template , request, url_for
from flask_bootstrap import Bootstrap
import json
import numpy as np
from matplotlib.widgets import Button
import matplotlib.image as mpimg
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import copy
from userid_country import userid_country

app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAswPHPy8HBkOhb9aDWsadudZ8KX379hgY"

# app.config['GOOGLEMAPS_KEY'] = "AIzaSyCDFpbv2jUwFTzHJ2Lo0odL52OJ0r3DX8o"

Bootstrap(app)
GoogleMaps(app, key="AIzaSyAswPHPy8HBkOhb9aDWsadudZ8KX379hgY")
# GoogleMaps(app, key="AIzaSyCDFpbv2jUwFTzHJ2Lo0odL52OJ0r3DX8o")

age_user = ""
gender_user = ""
interest_user = ""
interest_array_user = ""
region_user = ""

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
array_latitude2 = []
array_longitude2 = []
array_latitude3 = []
array_longitude3 = []
array_latitude4 = []
array_longitude4 = []
array_latitude5 = []
array_longitude5 = []
array_longlat =[]

modify_array_cat1 = []
modify_array_cat2 = []
modify_array_cat3 = []
modify_array_cat4 = []
modify_array_cat5 = []
array_cat1 = []
array_cat2 = []
array_cat3 = []
array_cat4 = []
array_cat5 = []

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

boolean_check_rankings = False


@app.route("/guidebook", methods=["GET", "POST"])
def guidebook():
    
    return render_template('guidebook.html')

@app.route("/member", methods=["GET", "POST"])
def member():
    
    return render_template('member.html')

@app.route("/En", methods=["GET", "POST"])
def start():
    
    return render_template('home.html')

@app.route("/form")
def form():
   return render_template('form.html')

@app.route("/interest3", methods=["GET", "POST"])
def interest3():
    if request.method == 'POST':
        gender = request.form.get('input_gender')
        age = request.form['input_age']
        global age_user
        global gender_user
        age_user = age
        gender_user = gender
        return render_template("interest3.html")

@app.route("/region3", methods=["GET", "POST"])
def region3():
    if request.method == 'POST':
        cat1_array = []
        cat1 = request.form['interest_category']
        print(cat1)
        cat1_array = cat1.split(',')
        global age_user
        global gender_user
        global interest_user
        global interest_array_user
        interest_user = cat1
        interest_array_user = cat1_array
        return render_template("region3.html")

@app.route("/mapview3", methods=["GET", "POST"])
def mapview3():
    if request.method == 'POST':
        interest_region = "("+request.form['interest_region']+")"
        
        global age_user
        global gender_user
        global interest_user
        global interest_array_user
        global region_user
        region_user = interest_region
        
        print("=================== Information of User ===================")
        print("User Gender : " + gender_user)
        print("Age : "+ age_user)
        print("Interest : ") 
        print(interest_array_user) #['Temple', 'Shrine']
        print("Region : " ) 
        print(region_user)
        print("=================== ==================== ===================")

        if(len(interest_array_user) == 1):
            result = main_v2({str(interest_array_user[0]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 2):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 3):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 4):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 5):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 6):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 7):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 8):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1,str(interest_array_user[7]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 9):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1,str(interest_array_user[7]):1,str(interest_array_user[8]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 10):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1,str(interest_array_user[7]):1,str(interest_array_user[8]):1,str(interest_array_user[9]):1},'JP',str(interest_region))


        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','Map and Travel From Traveler : '+ userid_country[int(user1)][1])
            print("Showing User : " + user1)

            # txt_no_result = txt_no_result.replace('\n','Map and Travel record of User:'+ user1)


        modify_array_record1 = [w.replace('\n','<br>') for w in array_record1]
        modify_array_cat1 = []
        for i in range(len(array_cat1)):
            txt_cat = array_cat1[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat1.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat1.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat1.append("<img style='width: 54px;height:54px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong = []         
        temp_dict = {}
        for i in range(len(array_latitude)):   
            temp_dict = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong.append(copy.deepcopy(temp_dict))

        polyline = {
            'stroke_color': '#2C528C', #Blue
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }
        polyline.update({'path': list_latlong})

        mymap = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline]
        
        )


        # print("==================== Test Load ====================")  
        # print("User interest : "+ array_cat1)
        # print("Region : "+interest_region)
        # # print(modify_array_cat1)
        # print("==================== Finished Load ====================")  

        return render_template("mapview3.html"
        , modify_array_cat1 = modify_array_cat1 
        , modify_array_record1 = modify_array_record1
        , mymap = mymap 
        , txt_no_result = txt_no_result
        , user1=user1,user2=user2,user3=user3,user4=user4,user5=user5,)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking1", methods=["GET", "POST"])
def mapview3_ranking1():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','Map and Travel From Traveler : '+ userid_country[int(user1)][1])
            print("Showing User : " + user2)

        modify_array_record1 = [w.replace('\n','<br>') for w in array_record1]
        modify_array_cat1 = []
        for i in range(len(array_cat1)):
            txt_cat = array_cat1[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat1.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat1.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat1.append("<img style='width: 54px;height:54px;' src ='/static/"+txt_cat+".png'/>")
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(modify_array_cat1[i])

        list_latlong1= []         
        temp_dict1 = {}
        for i in range(len(array_latitude)):   
            temp_dict1 = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong1.append(copy.deepcopy(temp_dict1))

        polyline1 = {
            'stroke_color': '#2C528C', #Blue
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline1.update({'path': list_latlong1})
        mymap1 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline1]
        ) 

        return render_template("mapview3_ranking1.html"
        , modify_array_cat1 = modify_array_cat1 
        , modify_array_record1 = modify_array_record1
        , mymap1=mymap1
        , txt_no_result =txt_no_result
        , user1=user1)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking2", methods=["GET", "POST"])
def mapview3_ranking2():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','Map and Travel From Traveler : '+ userid_country[int(user2)][1])
            print("Showing User : " + user2)

        modify_array_record2 = [w.replace('\n','<br>') for w in array_record2]
        modify_array_cat2 = []
        for i in range(len(array_cat2)):
            txt_cat = array_cat2[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat2.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat2.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat2.append("<img style='width: 54px;height:54px;' src ='/static/"+txt_cat+".png'/>")
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(modify_array_cat2[i])

        list_latlong2 = []         
        temp_dict2 = {}
        for i in range(len(array_latitude2)):   
            temp_dict2 = {'lat': float(array_latitude2[i]) , 'lng': float(array_longitude2[i])}
            list_latlong2.append(copy.deepcopy(temp_dict2))

        polyline2 = {
            'stroke_color': '#E86100', #Orange
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline2.update({'path': list_latlong2})
        mymap2 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude2, array_longitude2)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline2]
        ) 

        return render_template("mapview3_ranking2.html"
        , modify_array_cat2 = modify_array_cat2 
        , modify_array_record2 = modify_array_record2
        , mymap2=mymap2
        , txt_no_result =txt_no_result
        , user2=user2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking3", methods=["GET", "POST"])
def mapview3_ranking3():
    if request.method == 'POST':

        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','Map and Travel From Traveler : '+ userid_country[int(user3)][1])
            print("Showing User : " + user3)

        
        modify_array_record3 = [w.replace('\n','<br>') for w in array_record3]
        modify_array_cat3 = []
        for i in range(len(array_cat3)):
            txt_cat = array_cat3[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat3.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat3.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat3.append("<img style='width: 54px;height:54px;' src ='/static/"+txt_cat+".png'/>")
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(modify_array_cat3[i])

        list_latlong3 = []         
        temp_dict3 = {}
        for i in range(len(array_latitude3)):   
            temp_dict3 = {'lat': float(array_latitude3[i]) , 'lng': float(array_longitude3[i])}
            list_latlong3.append(copy.deepcopy(temp_dict3))

        polyline3 = {
            'stroke_color': '#296E01', #Green
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline3.update({'path': list_latlong3})
        mymap3 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude3, array_longitude3)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline3]
        ) 

        return render_template("mapview3_ranking3.html"
        , modify_array_cat3 = modify_array_cat3
        , modify_array_record3 = modify_array_record3
        , mymap3=mymap3
        , txt_no_result =txt_no_result
        , user3=user3)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking4", methods=["GET", "POST"])
def mapview3_ranking4():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','Map and Travel From Traveler : '+ userid_country[int(user4)][1])
            print("Showing User : " + user4)

        modify_array_record4 = [w.replace('\n','<br>') for w in array_record4]
        modify_array_cat4 = []
        for i in range(len(array_cat4)):
            txt_cat = array_cat4[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat4.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat4.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat4.append("<img style='width: 54px;height:54px;' src ='/static/"+txt_cat+".png'/>")
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(modify_array_cat4[i])

        list_latlong4= []         
        temp_dict4 = {}
        for i in range(len(array_latitude)):   
            temp_dict4 = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong4.append(copy.deepcopy(temp_dict4))

        polyline4 = {
            'stroke_color': '#FF0000', #Red
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline4.update({'path': list_latlong4})
        mymap4 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline4]
        ) 

        return render_template("mapview3_ranking4.html"
        , modify_array_cat4 = modify_array_cat4 
        , modify_array_record4 = modify_array_record4
        , mymap4=mymap4
        , txt_no_result =txt_no_result
        , user4=user4)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking5", methods=["GET", "POST"])
def mapview3_ranking5():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','Map and Travel From Traveler : '+ userid_country[int(user5)][1])
            print("Showing User : " + user5)

        modify_array_record5 = [w.replace('\n','<br>') for w in array_record5]
        modify_array_cat5 = []
        for i in range(len(array_cat5)):
            txt_cat = array_cat5[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat5.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat5.append("<img style='width: 54px;height:54px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat5.append("<img style='width: 54px;height:54px;' src ='/static/"+txt_cat+".png'/>")
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(modify_array_cat5[i])

        list_latlong5= []         
        temp_dict5 = {}
        for i in range(len(array_latitude)):   
            temp_dict5 = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong5.append(copy.deepcopy(temp_dict5))

        polyline5 = {
            'stroke_color': '#7D44AA', #Purple
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline5.update({'path': list_latlong5})
        mymap5 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline5]
        ) 

        return render_template("mapview3_ranking5.html"
        , modify_array_cat5 = modify_array_cat5
        , modify_array_record5 = modify_array_record5
        , txt_no_result =txt_no_result
        , mymap5=mymap5
        , user5=user5)





#========================================================== Version Japan ==========================================================
@app.route("/", methods=["GET", "POST"])
def start_jp():
    
    return render_template('home_jp.html')

@app.route("/form_jp")
def form_jp():
   return render_template('form_jp.html')

@app.route("/interest3_jp", methods=["GET", "POST"])
def interest3_jp():
    if request.method == 'POST':
        gender = request.form.get('input_gender')
        age = request.form['input_age']
        global age_user
        global gender_user
        age_user = age
        gender_user = gender

        return render_template("interest3_jp.html")

@app.route("/region3_jp", methods=["GET", "POST"])
def region3_jp():
    if request.method == 'POST':
        cat1_array = []
        cat1 = request.form['interest_category']
        cat1_array = cat1.split(',')

        global age_user
        global gender_user
        global interest_user
        global interest_array_user
        interest_user = cat1
        interest_array_user = cat1_array

        return render_template("region3_jp.html")


@app.route("/mapview3_jp", methods=["GET", "POST"])
def mapview3_jp():
    if request.method == 'POST':
        interest_region = "("+request.form['interest_region']+")"
        
        global age_user
        global gender_user
        global interest_user
        global interest_array_user
        global region_user
        region_user = interest_region
        
        print("=================== Information of User ===================")
        print("User Gender : " + gender_user)
        print("Age : "+ age_user)
        print("Interest : ") 
        print(interest_array_user) #['Temple', 'Shrine']
        print("Region : " ) 
        print(region_user)
        print("=================== ==================== ===================")

        if(len(interest_array_user) == 1):
            result = main_v2({str(interest_array_user[0]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 2):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 3):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 4):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 5):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 6):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 7):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 8):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1,str(interest_array_user[7]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 9):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1,str(interest_array_user[7]):1,str(interest_array_user[8]):1},'JP',str(interest_region))
        elif(len(interest_array_user) == 10):
            result = main_v2({str(interest_array_user[0]):1,str(interest_array_user[1]):1,str(interest_array_user[2]):1,str(interest_array_user[3]):1,str(interest_array_user[4]):1,str(interest_array_user[5]):1,str(interest_array_user[6]):1,str(interest_array_user[7]):1,str(interest_array_user[8]):1,str(interest_array_user[9]):1},'JP',str(interest_region))


        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','<ruby><rb>興味</rb><rt>きょうみ</rt></ruby>に<ruby><rb>合</rb><rt>あ</rt></ruby>った<ruby><rb>旅行記録</rb><rt>りょこうきろく</rt></ruby>を<ruby><rb>見</rb><rt>み</rt></ruby>つけました．'
            + "これは"
            + userid_country[int(user1)][2]
            + "からの<ruby><rb>旅行者</rb><rt>りょこうしゃ</rt></ruby>のものです")

            print("Showing User : " + user1)
            # txt_no_result = txt_no_result.replace('\n','Map and Travel record of User:'+ user1)


        modify_array_record1 = [w.replace('\n','<br>') for w in array_record1]
        modify_array_cat1 = []
        for i in range(len(array_cat1)):
            txt_cat = array_cat1[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat1.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat1.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat1.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong = []         
        temp_dict = {}
        for i in range(len(array_latitude)):   
            temp_dict = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong.append(copy.deepcopy(temp_dict))

        polyline = {
            'stroke_color': '#2C528C', #Blue
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }
        polyline.update({'path': list_latlong})

        mymap = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline]
        
        )

        return render_template("mapview3_jp.html"
        , modify_array_cat1 = modify_array_cat1 
        , modify_array_record1 = modify_array_record1
        , mymap = mymap 
        , txt_no_result = txt_no_result
        , user1=user1,user2=user2,user3=user3,user4=user4,user5=user5,)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking1_jp", methods=["GET", "POST"])
def mapview3_ranking1_jp():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','<ruby><rb>興味</rb><rt>きょうみ</rt></ruby>に<ruby><rb>合</rb><rt>あ</rt></ruby>った<ruby><rb>旅行記録</rb><rt>りょこうきろく</rt></ruby>を<ruby><rb>見</rb><rt>み</rt></ruby>つけました．'
            + "これは"
            + userid_country[int(user1)][2]
            + "からの<ruby><rb>旅行者</rb><rt>りょこうしゃ</rt></ruby>のものです")

        modify_array_record1 = [w.replace('\n','<br>') for w in array_record1]
        modify_array_cat1 = []
        for i in range(len(array_cat1)):
            txt_cat = array_cat1[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat1.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat1.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat1.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong1= []         
        temp_dict1 = {}
        for i in range(len(array_latitude)):   
            temp_dict1 = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong1.append(copy.deepcopy(temp_dict1))

        polyline1 = {
            'stroke_color': '#2C528C', #Blue
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline1.update({'path': list_latlong1})
        mymap1 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline1]
        ) 

        return render_template("mapview3_ranking1_jp.html"
        , modify_array_cat1 = modify_array_cat1 
        , modify_array_record1 = modify_array_record1
        , mymap1=mymap1
        , txt_no_result =txt_no_result
        , user1=user1)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking2_jp", methods=["GET", "POST"])
def mapview3_ranking2_jp():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','<ruby><rb>興味</rb><rt>きょうみ</rt></ruby>に<ruby><rb>合</rb><rt>あ</rt></ruby>った<ruby><rb>旅行記録</rb><rt>りょこうきろく</rt></ruby>を<ruby><rb>見</rb><rt>み</rt></ruby>つけました．'
            + "これは"
            + userid_country[int(user2)][2]
            + "からの<ruby><rb>旅行者</rb><rt>りょこうしゃ</rt></ruby>のものです")

        modify_array_record2 = [w.replace('\n','<br>') for w in array_record2]
        modify_array_cat2 = []
        for i in range(len(array_cat2)):
            txt_cat = array_cat2[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat2.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat2.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat2.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong2 = []         
        temp_dict2 = {}
        for i in range(len(array_latitude2)):   
            temp_dict2 = {'lat': float(array_latitude2[i]) , 'lng': float(array_longitude2[i])}
            list_latlong2.append(copy.deepcopy(temp_dict2))

        polyline2 = {
            'stroke_color': '#E86100', #Orange
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline2.update({'path': list_latlong2})
        mymap2 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude2, array_longitude2)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline2]
        ) 

        return render_template("mapview3_ranking2_jp.html"
        , modify_array_cat2 = modify_array_cat2 
        , modify_array_record2 = modify_array_record2
        , mymap2=mymap2
        , txt_no_result =txt_no_result
        , user2=user2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking3_jp", methods=["GET", "POST"])
def mapview3_ranking3_jp():
    if request.method == 'POST':

        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','<ruby><rb>興味</rb><rt>きょうみ</rt></ruby>に<ruby><rb>合</rb><rt>あ</rt></ruby>った<ruby><rb>旅行記録</rb><rt>りょこうきろく</rt></ruby>を<ruby><rb>見</rb><rt>み</rt></ruby>つけました．'
            + "これは"
            + userid_country[int(user3)][2]
            + "からの<ruby><rb>旅行者</rb><rt>りょこうしゃ</rt></ruby>のものです")

        
        modify_array_record3 = [w.replace('\n','<br>') for w in array_record3]
        modify_array_cat3 = []
        for i in range(len(array_cat3)):
            txt_cat = array_cat3[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat3.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat3.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat3.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong3 = []         
        temp_dict3 = {}
        for i in range(len(array_latitude3)):   
            temp_dict3 = {'lat': float(array_latitude3[i]) , 'lng': float(array_longitude3[i])}
            list_latlong3.append(copy.deepcopy(temp_dict3))

        polyline3 = {
            'stroke_color': '#296E01', #Green
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline3.update({'path': list_latlong3})
        mymap3 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude3, array_longitude3)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline3]
        ) 

        return render_template("mapview3_ranking3_jp.html"
        , modify_array_cat3 = modify_array_cat3
        , modify_array_record3 = modify_array_record3
        , mymap3=mymap3
        , txt_no_result =txt_no_result
        , user3=user3)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking4_jp", methods=["GET", "POST"])
def mapview3_ranking4_jp():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','<ruby><rb>興味</rb><rt>きょうみ</rt></ruby>に<ruby><rb>合</rb><rt>あ</rt></ruby>った<ruby><rb>旅行記録</rb><rt>りょこうきろく</rt></ruby>を<ruby><rb>見</rb><rt>み</rt></ruby>つけました．'
            + "これは"
            + userid_country[int(user4)][2]
            + "からの<ruby><rb>旅行者</rb><rt>りょこうしゃ</rt></ruby>のものです")

        modify_array_record4 = [w.replace('\n','<br>') for w in array_record4]
        modify_array_cat4 = []
        for i in range(len(array_cat4)):
            txt_cat = array_cat4[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat4.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat4.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat4.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong4= []         
        temp_dict4 = {}
        for i in range(len(array_latitude)):   
            temp_dict4 = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong4.append(copy.deepcopy(temp_dict4))

        polyline4 = {
            'stroke_color': '#FF0000', #Red
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline4.update({'path': list_latlong4})
        mymap4 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline4]
        ) 

        return render_template("mapview3_ranking4_jp.html"
        , modify_array_cat4 = modify_array_cat4 
        , modify_array_record4 = modify_array_record4
        , mymap4=mymap4
        , txt_no_result =txt_no_result
        , user4=user4)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mapview3_ranking5_jp", methods=["GET", "POST"])
def mapview3_ranking5_jp():
    if request.method == 'POST':
        
        txt_no_result = "\n"
        if(boolean_check_rankings== True):
            txt_no_result = txt_no_result.replace('\n','No Result That Match Your Interest')
        else :
            txt_no_result = txt_no_result.replace('\n','<ruby><rb>興味</rb><rt>きょうみ</rt></ruby>に<ruby><rb>合</rb><rt>あ</rt></ruby>った<ruby><rb>旅行記録</rb><rt>りょこうきろく</rt></ruby>を<ruby><rb>見</rb><rt>み</rt></ruby>つけました．'
            + "これは"
            + userid_country[int(user5)][2]
            + "からの<ruby><rb>旅行者</rb><rt>りょこうしゃ</rt></ruby>のものです")

        modify_array_record5 = [w.replace('\n','<br>') for w in array_record5]
        modify_array_cat5 = []
        for i in range(len(array_cat5)):
            txt_cat = array_cat5[i]
            if '/' in txt_cat :
                change_text = txt_cat.replace('/' , ':')
                modify_array_cat5.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            elif ' ' in txt_cat :
                change_text = txt_cat.replace(' ' , '')
                modify_array_cat5.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+change_text+".png'/>")
            else :
                modify_array_cat5.append("<img style='width: 54px;height:54px;margin:20px;' src ='/static/"+txt_cat+".png'/>")

        list_latlong5= []         
        temp_dict5 = {}
        for i in range(len(array_latitude)):   
            temp_dict5 = {'lat': float(array_latitude[i]) , 'lng': float(array_longitude[i])}
            list_latlong5.append(copy.deepcopy(temp_dict5))

        polyline5 = {
            'stroke_color': '#7D44AA', #Purple
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': []
        }

        polyline5.update({'path': list_latlong5})
        mymap5 = Map(
            identifier="view-side",
            lat= 36.2048,
            lng= 138.2529,
            markers=[ i for i in zip(array_latitude, array_longitude)] ,
            zoom = 4.5  ,
            style = "height:400px;width:500px;margin:auto;" ,
            polylines=[polyline5]
        ) 

        return render_template("mapview3_ranking5_jp.html"
        , modify_array_cat5 = modify_array_cat5
        , modify_array_record5 = modify_array_record5
        , txt_no_result =txt_no_result
        , mymap5=mymap5
        , user5=user5)


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
# from mpl_toolkits.basemap import Basemap

#以下の Gloval Variable をMain_v2内へ移動」
#dataset = {}
#countryset = {}

# 新しいバージョンの Main
def main_v2(all_interest, country,interest_region):
   
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
    
   # ver190717 begin
#    rankings = get_recommend(rankings, "0", country, 5 , dataset , countryset, original_input)
    rankings = get_recommend(rankings, "0", country, 10, dataset , countryset, original_input)

    # specufied_regions = ("Hokkaido")
    # specufied_regions = ("Hokkaido", "Kanto")
    specufied_regions = interest_region

    user_visited_region_num = {}
    with open("./JP_Travelers_VENU_ID_REGION_FREQ2.csv", "r") as csvfile:   
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 0: #空の行に対応するため
                    break         #空の行に対応するため    
                if(row[0]=='USER_ID'):
                    continue
                visited_region_num = 0
                for i in range(1, len(row)):
                    if row[i] in specufied_regions:
                        visited_region_num=visited_region_num + 1
                user_visited_region_num[row[0]] = visited_region_num
#    print(user_visited_region_num)
    new_rankings = []
    global boolean_check_rankings
    # i=0
    for u in rankings:
        # if(1<=i<len(rankings)-1):
        try:
            boolean_check_rankings = False
            # print(boolean_check_rankings)
            new_rankings.append([u[0], u[1], user_visited_region_num[u[1]]])
        except IndexError:
            boolean_check_rankings = True
            break

        #     gotdata = 'null'
#    print(new_rankings)   
    sorted_new_rankings = sorted(new_rankings, key=lambda a: a[2], reverse=True)
    print("Before sort")
    print(rankings)   
    print("After sort")
    print(sorted_new_rankings)   
    rankings = []
    for u in sorted_new_rankings:
        rankings.append((u[0], u[1]))
#    print(rankings)   
#    print(sorted_user_visited_region_num)
#    new_rankings = []
#    for item in sorted_user_visited_region_num:
#        for jtem in rankings:
#            if item[0] = jtem[0]:
#                new_rankings.append(jtem)
#    print(new_rankings)

# ver190717 end

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
    # f = open("output_gaterory.txt", "w" ,encoding='utf-8')
    # for item in all_interest:
    #     f.write(item+"\n")  
 
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
    global array_latitude2
    global array_longitude2
    global array_latitude3
    global array_longitude3
    global array_latitude4
    global array_longitude4
    global array_latitude5
    global array_longitude5

    global  array_cat1

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
    array_latitude.clear()
    array_longitude.clear()
    array_latitude2.clear()
    array_longitude2.clear()
    array_latitude3.clear()
    array_longitude3.clear()
    array_latitude4.clear()
    array_longitude4.clear()
    array_latitude5.clear()
    array_longitude5.clear()

    array_cat1.clear()
    array_cat2.clear()
    array_cat3.clear()
    array_cat4.clear()
    array_cat5.clear()

    global ranking_number

    timestamp = datetime.now().strftime("%Y%m%d_%H_%M_%S") 
    f = open("output_result " + timestamp + ".txt", "w" ,encoding='utf-8')

    #PROJECT_ID = 'tour-miner-project'
#    SERVICE_ACCOUNT = 'bigquery-admin@tour-miner-project-2019.iam.gserviceaccount.com'
    JSON_KEY_PATH = 'tour-miner-project-2019-511090dd4bd9.json'
    # BigQueryClientの取得
    client = get_client(json_key_file=JSON_KEY_PATH, readonly=True)
       
    #Interest Keyとその重みを表示

    f.write("User Gender : "+gender_user + "\nAge : " + age_user+"\n")
    f.write("Interest : ")
    for item in interest_array_user:
        f.write("%s ," % item)
    f.write("\nRegion : " + region_user +"\n")
    f.write("\n")
    print("Matched Interested Category: ") 
    f.write("Matched Interested Category: ") 

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
                f.write("\nUser:" + u[1])
                print("From : " + userid_country[int(u[1])][1] +"   "+ userid_country[int(u[1])][2])
                f.write("\nFrom : " + userid_country[int(u[1])][1] +"   "+ userid_country[int(u[1])][2] + "\n")

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
                        f.write("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2+"\n")
                        print("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2 )
                        travel_record1 = ("Date : " + text_date + "\n" + "Name : " + location_name2  +"\n" + "Time : " + text_time)
                        array_latitude.append(str(float(q['LATITUDE'])))
                        array_longitude.append(str(float(q['LONGITUDE'])))
                        array_cat1.append(q['CATEGORY'])
                        array_record1.append(travel_record1)
                        
                    elif(ranking_number==1) :
                        f.write("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2+"\n")
                        print("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2 )
                        travel_record2 = ("Date : " + text_date + "\n" + "Name : " + location_name2  +"\n" + "Time : " + text_time)
                        array_latitude2.append(str(float(q['LATITUDE'])))
                        array_longitude2.append(str(float(q['LONGITUDE'])))
                        array_cat2.append(q['CATEGORY'])
                        array_record2.append(travel_record2)

                    elif(ranking_number==2) :
                        f.write("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2+"\n")
                        print("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2 )
                        travel_record3 = ("Date : " + text_date + "\n" + "Name : " + location_name2  +"\n" + "Time : " + text_time)
                        array_latitude3.append(str(float(q['LATITUDE'])))
                        array_longitude3.append(str(float(q['LONGITUDE'])))
                        array_cat3.append(q['CATEGORY'])
                        array_record3.append(travel_record3)

                    elif(ranking_number==3) :
                        f.write("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2+"\n")                       
                        print("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2 )
                        travel_record4 = ("Date : " + text_date + "\n" + "Name : " + location_name2  +"\n" + "Time : " + text_time)
                        array_latitude4.append(str(float(q['LATITUDE'])))
                        array_longitude4.append(str(float(q['LONGITUDE'])))
                        array_cat4.append(q['CATEGORY'])
                        array_record4.append(travel_record4)

                    elif(ranking_number==4) :
                        f.write("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2+"\n")
                        print("Date : " + text_date + " " + "Time : " + text_time +" "+ "Category : " + q['CATEGORY'] + " " + "Place Name : " + location_name2 )
                        travel_record5 = ("Date : " + text_date + "\n" + "Name : " + location_name2  +"\n" + "Time : " + text_time)
                        array_latitude5.append(str(float(q['LATITUDE'])))
                        array_longitude5.append(str(float(q['LONGITUDE'])))
                        array_cat5.append(q['CATEGORY'])
                        array_record5.append(travel_record5)

                # print(q['DATE'] + ', ' + q['CATEGORY'] + ', ' + location_name + ", Weight:" + str(counter))
                # print(array_record1)




        #          print(q['DATE'] + ',' + q['CATEGORY'] + ',' + str(q['LONGITUDE']) + ',' + str(q['LATITUDE']) + ',' + q['VENUE_ID'])
            
    # Output1へ書き込み:主観的評価用（岡部さん用）:ここから

                
                # writing_information =(q['DATE'] + ', ' + q['CATEGORY'] + ', ' + location_name + ", Weight:" + str(counter) + ", Similarity:" + str("{0:.4f}".format(u[0])))  
                # f.write(("user:" + u[1]) + ', ')  
                # f.write(writing_information+"\n")  
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
                                
        ranking_number = ranking_number + 1
        f.write("\n")
    f.close() 


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
    
    # app.run(host='192.168.8.100',debug=True,use_reloader=True)
    # software1
    app.run(host='0.0.0.0', port=80,debug=True,use_reloader=True)

    # Mac mini
    app.run(host='133.62.160.28', port=80,debug=True,use_reloader=True)

    # app.run(host='192.168.11.44', port=80 ,debug=True,use_reloader=True)
    # softbank tourminer
    # app.run(host='10.221.208.217',debug=True,use_reloader=True)