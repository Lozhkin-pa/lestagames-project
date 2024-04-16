import re, math

def read_file(file_name):
    with open(f'data/{file_name}', 'r', encoding='utf-8') as f:
        content = f.read()
        array = re.sub('[^A-zА-я]', ' ', content).split()
    return array

def term_frequency(files_name_list):
    content = read_file(files_name_list[0])
    word_count = len(content)
    files_count = len(files_name_list)
    result_tf = {}
    result_idf = {}
    for i in content:
        if i not in result_tf:
            n = content.count(i)
            result_tf[i] = round(n / word_count, 3)
            result_idf[i] = 1
    for i in result_tf:
        for f in files_name_list[1:]:
            content_idf = read_file(f)
            if i in content_idf:
                result_idf[i] += 1
    for k, v in result_idf.items():
        result_idf[k] = [result_tf[k], round(math.log10(files_count / v), 3)]
    sorted_result_idf = sorted(
        result_idf.items(),
        key=lambda item: item[1][1],
        reverse=True
    )[:50]
    return sorted_result_idf
