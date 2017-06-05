from bs4 import BeautifulSoup
import  requests
import time


#url = 'https://cn.tripadvisor.com/Attractions-g60673-Activities-New_York_City_New_York.html'
url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
#print(urls)


def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    tltles = soup.select('div.property_title > a[target=""_blank]')
    imgs = soup.select('img[width="160"]')
    cates = soup.select('div.p13n_reasoning_v2 ')

    for tltle,img,cate in zip(tltles,imgs,cates):
        data = {
            'title':tltle.get_text(),
            'img':img.get('src'),
            'cate':list(cate.stripped_strings)
        }
        print(data)

for single_url in urls:
    get_attractions(single_url)











'''
headers = {
    'Users-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS perscoestorem%2C%2C-1%7CPremiumRRSeX 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Cookie':'TAUnique=%1%enc%3AWu04FVEqkwDuhEhXr81fc3AL%2BWGvs8d1IHyOZ74QHjpcZDjTQsqGzA%3D%3D; TASSK=enc%3AAJXQoHdh6GOE7J4xMeFP03mvFS5gpEqrvAWDxKsU%2FbaA9HzUToNMT1hroesCDtR%2F%2Fo52HeyEtGzq0jn2hbkmYPU68PUgtxjOxYxPzj%2B7tCLrfPwmQ6TG2Jgqx7R6%2F3gNjg%3D%3D; TAPD=tripadvisor.cn; __gads=ID=b811cc25c47081cd:T=1479972424:S=ALNI_MZmHwvZeW8oxbhknaU2RcM7yMGfaQ; CommercePopunder=SuppressAll*1479973599580; TAAuth2=%1%3%3Aff249c3e5156a5746be982af4c9e5d07%3AAI0RLfndC%2FQ7lBlOgVzZLXvP1Twc%2FLzpgUn5QrFXomzPALsClpsf4%2F9i5bIfCDO0dmULywJMVclpHmDhewku4hFH8Mu1F0VGusZeTIRb34gebjlFfW5Kp132IjnQYQPVYzZFy7JeWhMtmfAiq2pLFMI7rklVHxP5Yx6yi1tmICqgkxpjtwYmUKxxTRvwdj1sz2ypAGsJm%2Fq44mlg9ZxKEJKQkv1TlFR8qYlr48Bb5zFj; _smt_uid=5836a395.21b81ed4; bdshare_firstime=1479975973688; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60673_329l105127_329l60763_329l1739552_329l267031_329*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C9%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d267031-Reviews-Manhattan_Skyline-New_York_City_New_York.html; roybatty=TNI1625!ACS1z0tckj%2BzWk%2Bjy40d99Qu9c1OR%2BMsRRbFmCto3atmtivPt1%2BmJ6UxFqoWoDciB%2FiGuGTi1WiIANKxHuAuAygVysXPbOYbGFbwUu1Dh%2Fy78UHfQqrHzbchDfYudjsSG9cCWWx%2FOwKIuBfx80vSn%2FxsDVJ62DU8h4ttDtKDySxj%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1479972421; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1479978991; ki_t=1479972421262%3B1479972421262%3B1479978990924%3B1%3B28; ki_r=; NPID=; TASession=%1%V2ID.85A9E0CC8341A4E1B61D320FDD248919*SQ.101*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DA%26returnTo%3D%252FAttractions-g60763-Activities-New_York_City_New_York%5C.html*PR.427%7C*LS.ActionRecord*GR.76*TCPAR.89*TBR.98*EXEX.73*ABTR.40*PPRP.5*PHTB.60*FS.29*CPU.88*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.248FADC83508BC309141A0EA3C7A4733*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.267031; TAUD=LA-1479972408089-1*LG-6945086-2.1.F.*LD-6945087-.....'
    }

url_saves = 'http://www.tripadvisor.cn/Saves#545039'
wb_data = requests.get(url_saves,headers=headers)

soup = BeautifulSoup(wb_data.text,'lxml')
print(wb_data)
titles = soup.select('span.format_address')
#print(titles)
'''