import os

from pdfminer.pdfparser import  PDFParser
from pdfminer.pdfdocument import PDFDocument

from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

from pathlib import Path

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from pdfminer.layout import  LAParams
import shutil


import logging


lis1=['group sequential','conditional power','predictive power','conditional error','alpha spending']
lis2=['multi-arm multi-stage','multiarm multistage','multi stage']
lis3=['adaptive platform','adaptive platform']
lis4=['pick the winner','drop the loser','adaptive dose selection','seamless','adaptive design']
lis5=['adaptive enrichment','population enrichment','patient enrichment','enrichment design','biomarker adaptive']
lis6=['response adaptive','adaptive randomisation','adaptive randomization','outcome adaptive']
lis7=['adaptive hypothesis','adaptive hypotheses']
lis8=['sample size adjustment','sample size re estimation','sample size reestimation','sample size modification','sample size revision','sample size reassessment'
    ,'sample size re assessment','sample size re-calculation','sample size recalculation']

dr1 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\GSD'
dr2 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\MAMS'
dr3 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Platform'
dr4 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Dose selection'
dr5 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Enrichment'
dr6 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\ARD'
dr7 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Adaptive hypo'
dr8 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\sample size reestimation'
dr9 = r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\Demo structure\Not adaptive'

logging.propagate = False
logging.getLogger().setLevel(logging.ERROR)



dir =r'D:\Python toolkit for comprehensive searching on clinicaltrials.gov\search_store the PDF files which are going to scanned'
p = Path(dir)
file_name = p.glob('**/*.pdf')

def readpdf(file):
    with open(file,'rb') as Path:
        parser = PDFParser(Path)
        document = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            t2=b''
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
                layout = device.get_result()
                t=b''
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        results = x.get_text().encode('utf-8')
                        t += results
                t2+=t
        return(t2)

        Path.close()




for i in file_name:
    print(i)
    content_bef = readpdf(i)
    content = str(content_bef, encoding="utf-8").casefold()
    try:
        print('searching in lis1')
        for key in lis1:
            if key in content:
                shutil.copy(i, dr1)
                os.remove(i)
                print('GSD was found')
                break
            else:
                print('searching in lis2')
                for key in lis2:
                    if key in content:
                        shutil.copy(i, dr2)
                        os.remove(i)
                        print('MAMS was found')
                        break
                    else:
                        print('searching in lis3')
                        for key in lis3:
                            if key in content:
                                shutil.move(i, dr3)
                                os.remove(i)
                                print('platform was found')
                                break
                            else:
                                print('searching in lis4')
                                for key in lis4:
                                    if key in content:
                                        shutil.move(i, dr4)
                                        os.remove(i)
                                        print('dose selection was found')
                                        break
                                    else:
                                        print('searching in lis5')
                                        for key in lis5:
                                            if key in content:
                                                shutil.move(i, dr5)
                                                os.remove(i)
                                                print('enrichment was found')
                                                break
                                            else:
                                                print('searching in lis6')
                                                for key in lis6:
                                                    if key in content:
                                                        shutil.move(i, dr6)
                                                        os.remove(i)
                                                        print('ARD was found')
                                                        break
                                                    else:
                                                        print('searching in lis7')
                                                        for key in lis7:
                                                            if key in content:
                                                                shutil.move(i, dr7)
                                                                os.remove(i)
                                                                print('ADAPTIVE HYPO was found')
                                                                break
                                                            else:
                                                                print('searching in lis8')
                                                                for key in lis8:
                                                                    if key in content:
                                                                        shutil.move(i, dr8)
                                                                        os.remove(i)
                                                                        print('sample size reestiment  was found')
                                                                        break
                                                                    else:
                                                                        shutil.copy(i, dr9)
                                                                        os.remove(i)
                                                                        print('key word was not found')
                                                                        break
    except Exception as e:
        pass
    continue
