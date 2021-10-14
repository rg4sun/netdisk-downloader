import re
import os
import time 
import datetime 
from notedrive.baidu.drive import BaiDuDrive

def bar(n=100):
    print('\n', '-'*n, '\n')

cookie ="BIDUPSID=0CFD0E33BA72B599173C3C51ECA9FB03; PSTM=1634010172; BAIDUID=0CFD0E33BA72B599AB571D036D79B5FD:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=31253_26350; __yjs_duid=1_e1f5a9e1079f345f487d014b430ff1c81634019044941; BDUSS=RKM294ZjNSbWFDWTkybTc4aE9hd0l4QlI5OVJGM2Z5WVNLcGZ3bHJTWDF-b3hoSVFBQUFBJCQAAAAAAAAAAAEAAACXuzI5yOe5-87Sy7Wyu7DV0N0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPVxZWH1cWVhS0; BDUSS_BFESS=RKM294ZjNSbWFDWTkybTc4aE9hd0l4QlI5OVJGM2Z5WVNLcGZ3bHJTWDF-b3hoSVFBQUFBJCQAAAAAAAAAAAEAAACXuzI5yOe5-87Sy7Wyu7DV0N0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPVxZWH1cWVhS0; ab_sr=1.0.1_MjA4MDlhOTE3MzZlOTc2OTcxYTNhOGI5ZTc4MTgzZmRlY2NlM2VjNTliZDgwMjM1MDM3ODY4NTk2ZDJjZmE0ZDQ4ZmZjMjFhODM1ZmJiZWI5NWQwYjk1MWEwOTEyNWVjNWM2YzEyNmJiOWNmYTU0ODQ4ODFiY2NhOTZiOTllMTY2NWQ0YzFlNTZjZWU2ZjcwNDk0Y2NhZmEwZmJlMTVlOA==; delPer=0; BAIDUID_BFESS=0CFD0E33BA72B599AB571D036D79B5FD:FG=1; csrfToken=BLhI750rISFy3xoi-RHj2zU1; STOKEN=cf665c926dbaf722b85a00d0d511f881c057449e1dc7dbb92640daa83a89a1f5; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1634040665; BDRCVFR[VXHUG3ZuJnT]=mk3SLVN4HKm; PANPSC=12209539300392536932:DJI9ZdfpjgJ6GTCuUVWNwEy7txDAjOFZiqjjq7qWi8pa+zVsu1hu371iJS3G2jGbk2nt9sDNbJvy8D+Wwy+1YCO+EbNjkMM0OA6+HHtciFfHSTuafFA3EtUlWIY0tSpoUOuF9bNVtOXvuopL0N3EtxTpKkbQG71OovmNV+7na/RtoLnfYC42LUaIG3quAP1SJlOfPZFHq37Yo1rfcTTVA3z1V6DkjvELO6gB4KX1MEY=; PSINO=5; BA_HECTOR=2hala18021ag2l0l0v1gmb0qv0q; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1634042746"
BDUSS = re.findall('BDUSS=(.*?);', cookie)[0]

try:
    client = BaiDuDrive(bduss=BDUSS, save=False)
    print(client)
except:
    print('Can not init client')
else:
    print('Client init successfully！')
    bar()

# print(client.list("/"))
# print(type(client.list("/")))
# print(client.list('/')[0])

def list_files(file_path):
    return [file_info['server_filename'] for file_info in client.list(file_path)]

FILE_ROOT_PATH = '/数据集/TSN'
DOWNLOAD_ROOT_PATH = '../YunDownload'
dir_name_list = list_files(FILE_ROOT_PATH)
print(dir_name_list)
bar()

# file_name = dir_name_list[1]
# file_path = os.path.join(FILE_ROOT_PATH, file_name)
# print((file_path))
# bar()
# print('Downloading file: {} ...'.format(file_path))
# download_path = os.path.join(DOWNLOAD_ROOT_PATH, file_name)
# client.download(file_path, download_path, overwrite=False) # False的话，如果已经下过了，不会再下一遍
# print('File < {} > has been stored at {}'.format(file_name, download_path))
# print('Done!')

def file_download(file_name, FILE_ROOT_PATH=FILE_ROOT_PATH, DOWNLOAD_ROOT_PATH=DOWNLOAD_ROOT_PATH):

    file_path = os.path.join(FILE_ROOT_PATH, file_name)
    print('Downloading file: {} ...'.format(file_path))
    download_path = os.path.join(DOWNLOAD_ROOT_PATH, file_name)
    client.download(file_path, download_path, overwrite=False) # False的话，如果已经下过了，不会再下一遍
    bar()
    print('Done!')
    print('File < {} > has been stored at {}'.format(file_name, download_path))

# file_download(dir_name_list[2])


zips_root_path = os.path.join(FILE_ROOT_PATH, 'tvl1')
zips_name_list = list_files(zips_root_path)
print(zips_name_list)
print('Amount: ', len(zips_name_list))
bar()
# print('Sorted')
# bar()
# zips_name_list = sorted(list_files(zips_root_path), reverse=True)
# print(zips_name_list)
# bar()

start_time = time.time()
start_datetime = datetime.datetime.now()

# file_download(zips_name_list[1], FILE_ROOT_PATH=zips_root_path)

file_download(dir_name_list[3])

end_time = time.time()
end_datetime = start_datetime = datetime.datetime.now()

print('time cost: {} [calculated by time]'.format(end_time - start_time))
print('time cost: {} [calculated by datetime]'.format(end_datetime - start_datetime))