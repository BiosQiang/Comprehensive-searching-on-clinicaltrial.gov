import PyPDF2
from pathlib import Path


import logging
import shutil

logging.propagate = False
logging.getLogger().setLevel(logging.ERROR)

lis1=['group sequential','conditional power','predictive power','conditional error','alpha spending','interim analysis']
lis2=['multi-arm multi-stage','multiarm multistage','multi stage']
lis3=['adaptive platform','adaptive platform']
lis4=['pick the winner','drop the loser','adaptive dose selection','seamless','adaptive design']
lis5=['adaptive enrichment','population enrichment','patient enrichment','enrichment design','biomarker adaptive']
lis6=['response adaptive','adaptive randomisation','adaptive randomization','outcome adaptive']
lis7=['adaptive hypothesis','adaptive hypotheses']
lis8=['sample size adjustment','sample size re estimation','sample size reestimation','sample size modification','sample size revision','sample size reassessment'
    ,'sample size re assessment','sample size re-calculation','sample size recalculation']

dir =r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\search_store the PDF files which are going to scanned'

dr1 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\GSD'
dr2 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\MAMS'
dr3 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Platform'
dr4 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Dose selection'
dr5 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Enrichment'
dr6 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\ARD'
dr7 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Adaptive hypo'
dr8 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\sample size reestimation'
dr9 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Not adaptive'


p = Path(dir)
file_name = p.glob('**/*.pdf')


for i in file_name:
    # open a pdf file with the function 'open', the file was read and stored in Binary format/使用open的‘rb’方法打开pdf文件，使用二进制模式
    mypdf = open(i, mode='rb')

    # call the PdfFileReader function
    pdf_document = PyPDF2.PdfReader(mypdf)



    max=len(pdf_document.pages)
    pageseq=range(1,max,1)
    print(pageseq)


    content=''
    for num in pageseq:
        page_document = pdf_document.pages[num]
        page_temp = page_document.extract_text()
        content=content+page_temp
    try:
        for key in lis1:
            if key in content:
                mypdf.close()
                print(i)
                shutil.move(i, dr1)
                print('GSD was found')
                break
            else:
                for key in lis2:
                    if key in content:
                        mypdf.close()
                        print(i)
                        shutil.move(i, dr2)
                        print('MAMS was found')
                        break
                    else:
                        for key in lis3:
                            if key in content:
                                mypdf.close()
                                print(i)
                                shutil.move(i, dr3)
                                print('platform was found')
                                break
                            else:
                                for key in lis4:
                                    if key in content:
                                        mypdf.close()
                                        print(i)
                                        shutil.move(i, dr4)
                                        print('dose selection was found')
                                        break
                                    else:
                                        for key in lis5:
                                            if key in content:
                                                mypdf.close()
                                                print(i)
                                                shutil.move(i, dr5)
                                                print('enrichment was found')
                                                break
                                            else:
                                                for key in lis6:
                                                    if key in content:
                                                        mypdf.close()
                                                        print(i)
                                                        shutil.move(i, dr6)
                                                        print('ARD was found')
                                                        break
                                                    else:
                                                        for key in lis7:
                                                            if key in content:
                                                                mypdf.close()
                                                                print(i)
                                                                shutil.move(i, dr7)
                                                                print('ADAPTIVE HYPO was found')
                                                                break
                                                            else:
                                                                for key in lis8:
                                                                    if key in content:
                                                                        mypdf.close()
                                                                        print(i)
                                                                        shutil.move(i, dr8)
                                                                        print('sample size reestiment was found')
                                                                        break
                                                                    else:
                                                                        mypdf.close()
                                                                        shutil.move(i, dr9)
                                                                        print('key word was not found')

    except Exception as e:
        pass
    continue
