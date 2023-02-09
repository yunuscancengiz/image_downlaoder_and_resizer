from PIL import Image
import wget
import os

product1 = ["https://cdn.dsmcdn.com/ty594/product/media/images/20221110/21/211846297/559073319/1/1_org_zoom.jpg",
            "https://cdn.dsmcdn.com/ty594/product/media/images/20221110/21/211846297/559073319/1/1_org_zoom.jpg"]
product2 = ["https://cdn.dsmcdn.com/ty553/product/media/images/20221005/13/186463120/589712930/1/1_org_zoom.jpg"]
product3 = ["https://cdn.dsmcdn.com/ty639/product/media/images/20221212/17/234855793/646678658/1/1_org_zoom.jpg",
            "https://cdn.dsmcdn.com/ty522/product/media/images/20220904/16/169082492/558890166/1/1_org_zoom.jpg",
            "https://cdn.dsmcdn.com/ty184/product/media/images/20210930/22/137833466/226324491/1/1_org_zoom.jpg"]

products = [product1, product2, product3]
img1 = Image.new("RGB", (1800, 1800), "white")
product_counter = 1
for product in products:
    img_counter = 1
    os.mkdir(str(product_counter))
    for img2 in product:
        print("--------")
        wget.download(img2, out = f"{product_counter}/{img_counter}.jpg")

        img2 = Image.open(f"{product_counter}/{img_counter}.jpg")
        img2 = img2.resize((1200, 1800))
        img1.paste(img2, (300, 0))
        img1.save(f"{product_counter}/{img_counter}.jpg")
        
        img_counter += 1
    product_counter += 1