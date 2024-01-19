from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from .serializers import MedicineSerializer
from .models import Medicine
import requests

# Create your views here.
def get_med(request):
    max_page = 1
    page = 1
    while page <= max_page:
        url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
        params ={'serviceKey' : 'cDUUm72WcKWjVqG2QmPMafkkDZiqyFWJj0WAz2%2BjNT8zd86c2tb1Py3NdcJB2NEJcMu17vLfZwUzFzCpApX8cg%3D%3D', 
                'pageNo' : str(page), 
                'numOfRows' : '100', 
                #  'entpName' : '', 
                #  'itemName' : '', 
                #  'itemSeq' : '', 
                #  'efcyQesitm' : '', 
                #  'useMethodQesitm' : '', 
                #  'atpnWarnQesitm' : '', 
                #  'atpnQesitm' : '', 
                #  'intrcQesitm' : '', 
                #  'seQesitm' : '', 
                #  'depositMethodQesitm' : '', 
                #  'openDe' : '', 
                #  'updateDe' : '', 
                'type' : 'json' }
        response = requests.get(url, params=params).json()
        if page == 1:
            max_page = response['body']['totalCount'] // 100 + 1
        for medicine in response['body']['items']:
            save_data = {
                'entpName': medicine.get('entpName'),
                'itemName': medicine.get('itemName'),
                'itemSeq': medicine.get('itemSeq'),
                'efcyQesitm': medicine.get('efcyQesitm'),
                'useMethodQesitm': medicine.get('useMethodQesitm'),
                'atpnWarnQesitm': medicine.get('atpnWarnQesitm'),
                'atpnQesitm': medicine.get('atpnQesitm'),
                'intrcQesitm': medicine.get('intrcQesitm'),
                'seQesitm': medicine.get('seQesitm'),
                'depositMethodQesitm': medicine.get('depositMethodQesitm'),
                'openDe': medicine.get('openDe'),
                'updateDe': medicine.get('updateDe'),
                'itemImage': medicine.get('itemImage'),
                'bizrno': medicine.get('bizrno')
            }
            serializer = MedicineSerializer(data = save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        page += 1
    return JsonResponse(response)

def check(request, num):
    url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
    params ={'serviceKey' : 'cDUUm72WcKWjVqG2QmPMafkkDZiqyFWJj0WAz2%2BjNT8zd86c2tb1Py3NdcJB2NEJcMu17vLfZwUzFzCpApX8cg%3D%3D', 
            'pageNo' : str(num), 
            'numOfRows' : '100', 
            #  'entpName' : '', 
            #  'itemName' : '', 
            #  'itemSeq' : '', 
            #  'efcyQesitm' : '', 
            #  'useMethodQesitm' : '', 
            #  'atpnWarnQesitm' : '', 
            #  'atpnQesitm' : '', 
            #  'intrcQesitm' : '', 
            #  'seQesitm' : '', 
            #  'depositMethodQesitm' : '', 
            #  'openDe' : '', 
            #  'updateDe' : '', 
            'type' : 'json' }
    response = requests.get(url, params=params).json()
    return JsonResponse(response)

def max(request):
    medicines = get_list_or_404(Medicine)
    max_len = 0
    for med in medicines:
        if med.useMethodQesitm and max_len < len(med.useMethodQesitm):
            max_len = len(med.useMethodQesitm)
    print(max_len)
    return JsonResponse({'max': max_len})