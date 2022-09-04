from multiprocessing import Array
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from cv2 import add
import jovian
import requests
from bs4 import BeautifulSoup
import pandas as pd
from home.models import Engineering_colleges,Medical_colleges,Management_colleges,Design_colleges,Science_colleges,Law_colleges
# Create your views here.

def college_list(clg_india_url,image_list,page):
    
    selection_class = "jsx-2158881826 font-weight-bold text-md m-0"

    doc = BeautifulSoup(page.content, 'html.parser')

    clg_name = doc.find_all('h3', {'class': selection_class})

    fees_class_selection="jsx-2158881826 lr-key text-lg text-primary d-block font-weight-bold mb-1"
    fees=doc.find_all('span', {'class':fees_class_selection})

    course_name_class= 'jsx-2158881826 lr-value d-block mb-1'
    course_name=doc.find_all('span' , {'class':course_name_class})

    rating_class_selection='jsx-2158881826 rating-text text-white font-weight-bold text-base d-block text-right'
    rating=doc.find_all('span', {'class':rating_class_selection})

    address_class='jsx-2158881826 pr-1 location'
    address=doc.find_all('span',{'class':address_class})

    image_class='jsx-2158881826 img-overlay'
    image=doc.find_all('div',{'class':image_class})

    return clg_name,fees,course_name,rating,address,image


def home_page(request):
    return render(request, "home/index.html")
    #return HttpResponse("<h1>Hello World!</h1>")
def analytics_page(request):
    return render(request,"home/analytics.html")

def engineering(request):
    return render(request,"home/result.html")

def design(request):
    return render(request,"home/result.html")
    
def law(request):
    return render(request,"home/result.html")

def medical(request):
    return render(request,"home/result.html")

def mba(request):
    return render(request,"home/result.html")

def science(request):
    return render(request,"home/result.html")


def engineering_college_list(request):
    clg_india_url='https://collegedunia.com/btech-colleges'

    image_list=['https://images.collegedunia.com/public/college_data/images/appImage/1509430807cover.jpg?h=300&w=250&mode=stretch','https://images.collegedunia.com/public/college_data/images/appImage/25703_IIT_New.jpg?h=300&w=250&mode=stretch']
    
    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
        page=requests.get(clg_india_url,headers=header)
        clg_name,fees,course_name,rating,address,image=college_list(clg_india_url,image_list,page)
        parameter=[]
        index_for_fee=0

        for i in range(0,22):
            if(clg_name[i].text!="Parul University, Vadodara" and clg_name[i].text!="NIT Trichy, Tiruchirappalli" and clg_name[i].text!="Institute of Aeronautics and Engineering -[IAE], Bhopal" and clg_name[i].text!="Institute of Chemical Technology - [ICT], Mumbai" and clg_name[i].text!="Sha-Shib Aviation Academy, Kochi" and clg_name[i].text!="Academy of Aviation and Engineering - [AAE], Bangalore" and clg_name[i].text!="Indian Institute of Engineering Science and Technology - [IIEST] Shibpur, Howrah" and clg_name[i].text!="East Point Group of Institutions - [EPGI], Bangalore"):
                parameter_item={}
                parameter_item["College_Name"]=clg_name[i].text
                parameter_item["Fee"]=fees[index_for_fee].text
                parameter_item["Exam"]=fees[index_for_fee+1].text
                parameter_item["Rating"]=fees[index_for_fee+2].text
                parameter_item["Address"]=address[i].text
                if(i<2):
                        parameter_item['Img']=image_list[i]
                else:
                        parameter_item['Img']=image[i+2].previous_sibling['data-src']
                parameter.append(parameter_item)
                modelObject=Engineering_colleges(College_Name=parameter_item["College_Name"],Fee=parameter_item["Fee"],Exam=parameter_item["Exam"],Rating=parameter_item["Rating"],Address=parameter_item["Address"],Img=parameter_item['Img'])
                modelObject.save()
                index_for_fee+=3
            else:
                index_for_fee+=2

        top_colleges_df=pd.DataFrame(parameter)

        #print(parameter)

        top_colleges_df.to_csv('top_clgs.csv', index=None)

        df_new = pd.read_csv('top_clgs.csv')

        return JsonResponse(parameter,safe=False)
    except:
        return JsonResponse(list(Engineering_colleges.objects.values()),safe=False)


def medical_college_list(request):

    clg_india_url='https://collegedunia.com/mbbs-colleges'
    image_list=[]

    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
        page=requests.get(clg_india_url,headers=header)
        clg_name,fees,course_name,rating,address,image=college_list(clg_india_url,image_list,page)

        parameter=[]
        index_for_fee=0

        for i in range(0,21):
            parameter_item={}
            if(index_for_fee>len(fees)-3):
                break
            if(clg_name[i].text!="Parul University, Vadodara" and clg_name[i].text!="NIT Trichy, Tiruchirappalli" and clg_name[i].text!="Institute of Aeronautics and Engineering -[IAE], Bhopal" and clg_name[i].text!="Institute of Chemical Technology - [ICT], Mumbai" and clg_name[i].text!="Sha-Shib Aviation Academy, Kochi" and clg_name[i].text!="Academy of Aviation and Engineering - [AAE], Bangalore" and clg_name[i].text!="Indian Institute of Engineering Science and Technology - [IIEST] Shibpur, Howrah" and clg_name[i].text!="East Point Group of Institutions - [EPGI], Bangalore"):
                parameter_item["College Name"]=clg_name[i].text
                parameter_item["Fee"]=fees[index_for_fee].text
                parameter_item["Exam"]=fees[index_for_fee+1].text
                parameter_item["Rating"]=fees[index_for_fee+2].text
                if(i<2):
                    parameter_item['Img']=image_list[i]
                else:
                    parameter_item['Img']=image[i+2].previous_sibling['data-src']
                parameter_item["Address"]=address[i].text
                parameter.append(parameter_item)
                modelObject=Medical_colleges(College_Name=parameter_item["College_Name"],Fee=parameter_item["Fee"],Exam=parameter_item["Exam"],Rating=parameter_item["Rating"],Address=parameter_item["Address"],Img=parameter_item['Img'])
                modelObject.save()
                #index_for_clg_name+=1
                index_for_fee+=3
            else:
                #index_for_clg_name+=1
                index_for_fee+=2

        top_colleges_df=pd.DataFrame(parameter)

        #print(top_colleges_df)

        top_colleges_df.to_csv('top_medical_clgs.csv', index=None)

        df_new = pd.read_csv('top_medical_clgs.csv')

        return JsonResponse(parameter,safe=False)
    except:
        return JsonResponse(list(Medical_colleges.objects.values()),safe=False)

def mba_college_list(request):
    clg_india_url='https://collegedunia.com/mba-colleges'
    image_list=["https://images.collegedunia.com/public/college_data/images/appImage/27897_NIFT_New.jpg?h=300&w=250&mode=stretch","https://images.collegedunia.com/public/college_data/images/appImage/6914_NIFTMUMBAI_APP.jpg?h=300&w=250&mode=stretch"]

    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
        page=requests.get(clg_india_url,headers=header)
        clg_name,fees,course_name,rating,address,image=college_list(clg_india_url,image_list,page)

        parameter=[]
        index_for_fee=0 

        for i in range(0,21):
            parameter_item={}
            if(index_for_fee>len(fees)-3):
                break
            if(clg_name[i].text!="JG University, Ahmedabad" and clg_name[i].text!="Indian Institute of Management - [IIMK], Kozhikode" and clg_name[i].text!="Bharati Vidyapeeth Deemed University, School of Distance Education - [BVDU SDE], Pune"):
                parameter_item["College Name"]=clg_name[i].text
                parameter_item["Total Fees"]=fees[index_for_fee].text
                parameter_item["Exam Excepted"]=fees[index_for_fee+1].text
                parameter_item["Rating"]=fees[index_for_fee+2].text[0:4]
                parameter_item["Address"]=address[i].text
                parameter.append(parameter_item)
                modelObject=Management_colleges(College_Name=parameter_item["College_Name"],Fee=parameter_item["Fee"],Exam=parameter_item["Exam"],Rating=parameter_item["Rating"],Address=parameter_item["Address"],Img=parameter_item['Img'])
                modelObject.save()
                #index_for_clg_name+=1
                index_for_fee+=3
            elif(clg_name[i].text!="JG University, Ahmedabad"):
                #index_for_clg_name+=1
                index_for_fee+=2
            else:
                index_for_fee+=1

        top_colleges_df=pd.DataFrame(parameter)

        #print(top_colleges_df)

        top_colleges_df.to_csv('top_medical_clgs.csv', index=None)

        df_new = pd.read_csv('top_medical_clgs.csv')

        return JsonResponse(parameter,safe=False)
    except:
        return JsonResponse(list(Management_colleges.objects.values()),safe=False)  

def design_college_list(request):

    clg_india_url='https://collegedunia.com/design-colleges'
    image_list=["https://images.collegedunia.com/public/college_data/images/appImage/27897_NIFT_New.jpg?h=300&w=250&mode=stretch","https://images.collegedunia.com/public/college_data/images/appImage/6914_NIFTMUMBAI_APP.jpg?h=300&w=250&mode=stretch"]
    
    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
        page=requests.get(clg_india_url,headers=header)
        clg_name,fees,course_name,rating,address,image=college_list(clg_india_url,image_list,page)

        parameter=[]
        index_for_fee=0 
        for i in range(0,22):
            parameter_item={}
            if(index_for_fee>len(fees)-3):
                break
            if(clg_name[i].text!="AND Academy, New Delhi" and clg_name[i].text!="Symbiosis Institute of Design - [SID], Pune"):
                parameter_item["College Name"]=clg_name[i].text
                parameter_item["Fee"]=fees[index_for_fee].text
                parameter_item["Exam"]=fees[index_for_fee+1].text
                parameter_item["Rating"]=fees[index_for_fee+2].text
                if(i<2):
                    parameter_item['Img']=image_list[i]
                else:
                    parameter_item['Img']=image[i+2].previous_sibling['data-src']
                parameter_item["Address"]=address[i].text
                parameter.append(parameter_item)
                modelObject=Design_colleges(College_Name=parameter_item["College_Name"],Fee=parameter_item["Fee"],Exam=parameter_item["Exam"],Rating=parameter_item["Rating"],Address=parameter_item["Address"],Img=parameter_item['Img'])
                modelObject.save()
                #index_for_clg_name+=1
                index_for_fee+=3
            elif(clg_name[i].text!="AND Academy, New Delhi"):
                #index_for_clg_name+=1
                index_for_fee+=2
            else:
                index_for_fee+=1

        top_colleges_df=pd.DataFrame(parameter)

        #print(top_colleges_df)

        top_colleges_df.to_csv('top_design_clgs.csv', index=None)

        df_new = pd.read_csv('top_design_clgs.csv')


        return JsonResponse(parameter,safe=False)
    except:
        return JsonResponse(list(Design_colleges.objects.values()),safe=False) 

def law_college_list(request):
    clg_india_url='https://collegedunia.com/law-colleges'
    image_list=["https://images.collegedunia.com/public/college_data/images/appImage/25621_NLSIU.jpg?h=300&w=250&mode=stretch","https://images.collegedunia.com/public/college_data/images/appImage/25465_NLAWD.jpg?h=300&w=250&mode=stretch"]
    
    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
        page=requests.get(clg_india_url,headers=header)
        clg_name,fees,course_name,rating,address,image=college_list(clg_india_url,image_list,page)
        parameter=[]
        index_for_fee=0 
        for i in range(0,22):
            parameter_item={}
            if(index_for_fee>len(fees)-3):
                break
            if(clg_name[i].text!="Indian Institute of Management - [IIM], Rohtak"):
                parameter_item["College Name"]=clg_name[i].text
                parameter_item["Fee"]=fees[index_for_fee].text
                parameter_item["Exam"]=fees[index_for_fee+1].text
                parameter_item["Rating"]=fees[index_for_fee+2].text
                if(i<2):
                    parameter_item['Img']=image_list[i]
                else:
                    parameter_item['Img']=image[i+2].previous_sibling['data-src']
                parameter_item["Address"]=address[i].text
                parameter.append(parameter_item)
                modelObject=Law_colleges(College_Name=parameter_item["College_Name"],Fee=parameter_item["Fee"],Exam=parameter_item["Exam"],Rating=parameter_item["Rating"],Address=parameter_item["Address"],Img=parameter_item['Img'])
                modelObject.save()
                #index_for_clg_name+=1
                index_for_fee+=3
            else:
                index_for_fee+=2

        top_colleges_df=pd.DataFrame(parameter)

        #print(top_colleges_df)

        top_colleges_df.to_csv('top_law_clgs.csv', index=None)

        df_new = pd.read_csv('top_law_clgs.csv')

        return JsonResponse(parameter,safe=False)
    except:
        return JsonResponse(list(Law_colleges.objects.values()),safe=False) 

def science_college_list(request):

    clg_india_url='https://collegedunia.com/science-colleges'
    image_list=["https://images.collegedunia.com/public/college_data/images/appImage/25621_NLSIU.jpg?h=300&w=250&mode=stretch","https://images.collegedunia.com/public/college_data/images/appImage/25465_NLAWD.jpg?h=300&w=250&mode=stretch"]
    
    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
        page=requests.get(clg_india_url,headers=header)
        clg_name,fees,course_name,rating,address,image=college_list(clg_india_url,image_list,page)
        parameter=[]
        index_for_fee=0 

        for i in range(0,21):
            parameter_item={}
            if(index_for_fee>len(fees)-3):
                break
            if(clg_name[i].text!="St Stephen's College, New Delhi" and clg_name[i].text!="Lady Shri Ram College for Women - [LSR], New Delhi" and clg_name[i].text!="LJ Institute of Development Studies and Management, Ahmedabad" and clg_name[i].text!="Indian Institute of Clinical Research And Management - [IICRM], Nagpur" and clg_name[i].text!="Madras Christian College - [MCC], Chennai" and clg_name[i].text!="Atma Ram Sanatan Dharma College - [ARSD], New Delhi"):
                parameter_item["College Name"]=clg_name[i].text
                parameter_item["B.Sc First Year Fees"]=fees[index_for_fee].text
                parameter_item["Rating"]=fees[index_for_fee+2].text[0:4]
                parameter_item["Address"]=address[i].text
                parameter.append(parameter_item)
                modelObject=Science_colleges(College_Name=parameter_item["College_Name"],Fee=parameter_item["Fee"],Exam=parameter_item["Exam"],Rating=parameter_item["Rating"],Address=parameter_item["Address"],Img=parameter_item['Img'])
                modelObject.save()
                index_for_fee+=3
            elif(clg_name[i].text!="LJ Institute of Development Studies and Management, Ahmedabad"):
                index_for_fee+=2
            else:
                index_for_fee+=1

        top_colleges_df=pd.DataFrame(parameter)

        #print(top_colleges_df)

        top_colleges_df.to_csv('top_law_clgs.csv', index=None)

        df_new = pd.read_csv('top_law_clgs.csv')

        return JsonResponse(parameter,safe=False)
    except:
        return JsonResponse(list(Science_colleges.objects.values()),safe=False)
