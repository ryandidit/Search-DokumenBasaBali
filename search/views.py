from django.shortcuts import render
from .script.delta_topi import main, delta_topi
from .script.text_bolding import main as change_text
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
import glob
import os
import time
# Create your views here.


def index(request):
    startT = time.time()
    if request.GET:
        result = []
        keys = request.GET['keywords']
        print("Keyword : "+(keys))
        jumlah = request.GET['jumlah'].split('-')
        temp = main(keys)
        if(temp != False):
            state, symbol, delta, start_state, final_state = main(keys)
        else:
            context = {
                'error': "Keyword yang anda masukan salah "}
            return render(request, 'search/index.html', context)
        list_text = sorted(glob.glob('docs/*.txt'),
                           key=lambda name: int(name[8:-4]))
        if(len(jumlah) == 1):
            for x in range(int(jumlah[0])):
                f = open(list_text[x], 'r', errors='ignore')
                content = f.read()
                f.close()
                data = delta_topi(content.lower(), state, symbol, delta,
                                  start_state, final_state)
                if data:
                    doc_name = list_text[x][5:-4]
                    text_res = content[int(data)-len(keys)+1:]
                    text_res = change_text(
                        text_res, keys.split(" "))
                    text_res = mark_safe(text_res)
                    result.append({'doc_name': doc_name, 'res': text_res})
            jumlah = jumlah[0]
        else:
            for x in range(int(jumlah[0]), int(jumlah[1])):
                f = open(list_text[x], 'r', errors='ignore')
                content = f.read()
                f.close()
                data = delta_topi(content.lower(), state, symbol, delta,
                                  start_state, final_state)
                if data:
                    doc_name = list_text[x][5:-4]
                    text_res = content[int(data)-len(keys)+1:]
                    text_res = change_text(text_res, keys.split(" "))
                    text_res = mark_safe(text_res)
                    result.append({'doc_name': doc_name, 'res': text_res})
            jumlah = "-".join(jumlah)
        if(len(result) != 0):
            page_num = request.GET.get('page', 1)
            paginator = Paginator(result, 5, allow_empty_first_page=True)
            page = paginator.get_page(page_num)
            context = {'data': page,
                       'keyword': request.GET['keywords'], 'jumlah': jumlah}
        else:
            context = {
                'error': "Tidak ditemukan document dengan keyword : "+keys}
        context['rtime'] = 'About %d results (%.2fms)' % (
            len(result), time.time() - startT)
        print("Runtime :" + str(time.time() - startT))
        return render(request, 'search/index.html', context)
    else:
        return render(request, 'search/index.html')


def detail(request, doc_name):

    f = open("docs/"+doc_name+".txt", 'r', errors='ignore')
    content = f.read()
    f.close()
    context = {'title': doc_name, 'data': content}
    return render(request, 'search/detail.html', context)


def quintuple(request):
    keys = request.GET['keyword']
    state, symbol, delta, start_state, final_state = main(keys)
    context = {'key': keys, 'state': state, 'symbol': symbol, 'delta': delta,
               'start_state': start_state, 'final_state': final_state}
    return render(request, 'search/quintuple.html', context)
