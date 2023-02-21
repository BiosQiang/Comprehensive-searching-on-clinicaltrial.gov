# To download protocol or SAP from XML file located in the direcation(denoted by dire) and write into the current project pathway

def get_file_from_url(dire):
    from pathlib import Path
    import os
    import requests
    import io
    key='<document_url>'
    p = Path(dire)
    file_name = p.glob('**/*.xml')
    urlist = []
    title_lis = []
    for i in file_name:
        f=open(i,'rb')
        title=os.path.basename(f.name)
        title=title[0:11]
        title_lis.append(title)
        for line in f:
            text=str(line)
            if key in text and "Prot_SAP" in text:
                star=text.find('https')

                end=text.find('.pdf')

                end+=4
                pro_url=text[star:end]



            elif key in text and "SAP" in text:
                star=text.find('https')

                end=text.find('.pdf')

                end+=4

                sap_url = text[star:end]


        if pro_url is not None:
            url = pro_url
        else:
            url = sap_url
        urlist.append(url)
    # print("urlis",urlist)
    # print("title_lis", title_lis)
    ssq=0
    for fileseq in urlist:
        a=str(fileseq)
        title=str(title_lis[ssq])+".pdf"
        send_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}
        req = requests.get(a, headers=send_headers)  # 通过访问互联网得到文件内容
        bytes_io = io.BytesIO(req.content)  # 转换为字节流
        with open(title, 'wb') as file:
            ssq+=1
            print("successfully download",ssq,"files")
            file.write(bytes_io.getvalue())  # 保存到本地

if __name__ == '__main__':
    dire = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\source_store the XML file'
    # dire = r'C:\Users\86130\Desktop\TEST'
    a=get_file_from_url(dire)


