# coding:utf-8
import sys
import os
import pandas as pd
import shutil
import stat

def find(path,ip):
    # open the excel file
    df = pd.read_excel(path)
    if ip in df["ip1"].values:
        s1 = df[df["ip1"]==ip]["man"].values.tolist()[0]
        return {s1:ip}
    elif ip in df["ip2"].values:
        s2 = df[df["ip2"]==ip]["man"].values.tolist()[0]
        return {s2:ip}
    elif ip in df["ip3"].values:
        s3 = df[df["ip3"]==ip]["man"].values.tolist()[0]
        return {s3:ip}
    else:
        return 0
def mkdir(path,filename,desname):
    path = path.strip()
    path = path.rstrip("\\")
    path_e = str(path) + '\\' + str(filename) + '_' +  desname
    isExists = os.path.exists(path_e)
    if not isExists:
        os.makedirs(path_e)
        print path_e + ' 创建成功'.decode('utf-8')
        return path_e
    else:
        print path_e + ' 目录已存在'.decode('utf-8')
        return path_e

def save(rootdir,newpath,ip):
    list = os.listdir(rootdir)
    ip_name = ip+'.html'
    all_path_name = []
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        all_path_name.append(os.path.basename(path))
    s_media = os.path.join(rootdir,'media')
    d_media = os.path.join(newpath,'media')
    isExists_media = os.path.exists(d_media)
    if not isExists_media:
        shutil.copytree(s_media,d_media)
    else:
        print d_media + ' 目录已存在'.decode('utf-8')
    if ip_name in all_path_name:
        dst_path = os.path.join(rootdir,ip_name)
        newfp = os.path.join(newpath,ip_name)
        isExists_newfp = os.path.exists(newfp)
        if not isExists_newfp:
            shutil.copy(dst_path, newfp)
            print "copy %s -> %s"%(dst_path,newfp)
        else:
            print newfp + ' 文件已存在'.decode('utf-8')
    else:
        return 0

if __name__ == "__main__":
    # input the excel file
    path_xlsx = raw_input('请输入excel文件地址:')
    path_report = raw_input('请输入保存报告地址:')
    file_name = raw_input('请输入报告名前缀:')
    host_path = raw_input('请输入报表漏洞站点地址:')
    f = open("test.txt", 'r')
    all_ip = f.readlines()
    f.close()
    for each_ip in all_ip:
        dict_name = find(path_xlsx,each_ip.strip('\n'))
        for des_name in dict_name.keys():
            new_path = mkdir(path_report,file_name,des_name)
            #print new_path
            save(host_path,new_path,dict_name.get(des_name))



