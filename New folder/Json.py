import requests
import csv
try:
    url="https://jsonplaceholder.typicode.com/comments"
    with open('QuotesToScrapeData.csv', 'w', newline='', encoding='UTF8') as csvfile:
        fieldnames = ['postId', 'id', 'name',"email","body"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        r=requests.get(url)
        f=open("Data.json","w")
        Data=r.json()
        # f=open("Data.csv","a")
        for i in Data:
            writer.writerow([i['postId'],i['id'],i['name'],i['email'],i['body']])
except Exception as E:
    print('Error',E)
    #  print(f"Title:{Title}\nAuthor:{Author} URL={AuthorURL}\n Tags={' ,'.join(TagText)}\n TagsURL:{';'.join(TagURLS)}")
#      'userId': 1,
#     'id': 1,
#     'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
#     'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
#   },
    
