def main(text_res, keys):
    for key in keys:
        text_res = text_res.replace(
            key+" ", '<strong>'+key+'</strong> ')
        text_res = text_res.replace(
            key.title()+" ", '<strong>'+key.title()+'</strong> ')
        text_res = text_res.replace(
            key.title()+"-", '<strong>'+key.title()+'</strong>-')
        text_res = text_res.replace(
            key+"-", '<strong>'+key+'</strong>-')
        text_res = text_res.replace(
            key.title()+".", '<strong>'+key.title()+'</strong>.')
        text_res = text_res.replace(
            key+".", '<strong>'+key+'</strong>.')
        text_res = text_res.replace(
            key.title()+",", '<strong>'+key.title()+'</strong>,')
        text_res = text_res.replace(
            key+",", '<strong>'+key+'</strong>,')
    return text_res

