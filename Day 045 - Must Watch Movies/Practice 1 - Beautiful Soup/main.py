from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf-8") as file:
    website = file.read()

soup = BeautifulSoup(website, "html.parser")

#print(soup.title.string)

# Intended text
#print(soup.prettify())

#print(soup.p)

#all_anchors = soup.findAll(name="a")
#print(all_anchors)

#print(soup.li.string)

#all_anchors = soup.findAll(name="a")
#for tag in all_anchors:
#    print(tag.getText())
#    print(tag.get("href"))


#heading = soup.find(name="h1", id="name")
#print(heading.getText())

#s_heading = soup.find(name="h3")
#print(s_heading.get("class"))


comp_url = soup.select_one(selector="strong a")
print(comp_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select_one(".heading")
print(headings)



#with open("http://www.bloggingintensifies.com/index.php", encoding="utf-8") as file:
#    website2 = file.read()
#
#soup2 = BeautifulSoup(website2, "html.parser")
#
#all_img = soup2.findAll(name="img")
#for tag in all_img:
#    print(tag.get("src"))