def urls(url_list):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for i, url in enumerate(url_list):
        url_len = len(url)
        for j in range(url_len):
            if url[j] == '@':
                list1.append(url[0:j])
                list2.append(url[j+1:url_len-1])

    for i, key in enumerate(list1):
        for j in range(len(key)):
            print(j)
            if key[j] == '+':
                key = key[0:j]
                break
        list3.append(key)

    for k, key2 in enumerate(list2):
        for l in range(len(key2)):
            if key2[l] == '.':
                key2 = key2[0:l]
                break
        list4.append(key2)

    return list3, list4


if __name__ == "__main__":
    input_given = ['swarnims@bu.edu', 'this+this@that.com', 'normal@example.gov.in']
    print(urls(input_given))
     # print(output1)
     # print(output2)



