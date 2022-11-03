from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import webbrowser


my_url = 'https://www.bunnings.com.au/products/tools/power-tools?L0=products&L1=tools&L2=power-tools&pageSize=36&page=1'

#opening up connection, grabbing the page
uClient = Request(my_url)
#page_html = webbrowser.open(my_url)
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
#uClient.close()
page_html = urlopen(req).read()



#html parser
page_soup = soup(page_html, "html.parser")

#grap each products
containers = page_soup.findAll("div", {"class":"product-wrapper"})


filename = "product.csv"
f= open(filename, "w")

headers = "brand,product_name \n"

f.write("headers")


for container in containers:
	#product name
	prod_name = container.div.div["title"]

	#brand name
	brand = container.div.findAll("div", {"class":"brand-logo-container"})
	brand_name = brand[0].img["alt"]



	#brand = container.div.div.a.img["title"]

	#title_container = container.findALL("a", {"class":"item-container"})
	#product_name = title_container[0].text

	#shipping_container = container.findALL("li", {"class":"price-shipping"})
	#shipping = shipping_container[0].text.strip()

	print("brand:" + brand_name)
	print("product_name:" + prod_name)
	#print("shipping" + shipping)

	#f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
	f.write(brand_name + "," + prod_name.replace(",", "|")  + "\n")

f.close()