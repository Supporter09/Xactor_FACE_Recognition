from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import requests

def crawNewsData(baseUrl, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    titles_actor = soup.findAll('h3', class_='lister-item-header')
    links = [link.find('a').attrs["href"] for link in titles_actor]
    data = []
    for link in links:
        news = requests.get(baseUrl + link)
        soup = BeautifulSoup(news.content, "html.parser")
        name = soup.find("span", class_="itemprop").text
        information = soup.find("div", class_="name-trivia-bio-text").text
        born_date = soup.find("div", id="name-born-info").text

        
        image = soup.find("img").attrs["src"]
        data.append({
            "name": name,
            "information": information,
            "born_date" : born_date,
            "image": image,
        })
        print("craw " + name)
    return data


def writeToImage(image, text, position, font, color, maxLine):
    charPerLine = 650 // font.getsize('x')[0]
    pen = ImageDraw.Draw(image)
    yStart = position[1]
    xStart = position[0]
    point = 0
    prePoint = 0
    while point < len(text):
        prePoint = point
        point += charPerLine
        while point < len(text) and text[point] != " ":
            point -= 1
        pen.text((xStart, yStart), text[prePoint:point], font=font, fill=color)
        yStart += font.getsize('hg')[1]
        maxLine -= 1
        if (maxLine == 0):
            if (point < len(text)):
                pen.text((xStart, yStart), "...", font=font, fill="black")
            break


def makeFastNews(data):
    for index, item in enumerate(data):
        # make new image and tool to draw
        image = Image.new('RGB', (650, 750), color="white")
        pen = ImageDraw.Draw(image)
        # load image from internet => resize => paste to main image
        pen.rectangle(((0, 0), (650, 300)), fill="grey")
        newsImage = Image.open(requests.get(item["image"], stream=True).raw)
        newsImage.thumbnail((650, 300), Image.ANTIALIAS)
        image.paste(newsImage, (650 // 2 - newsImage.width // 2, 300 // 2 - newsImage.height//2))
        ## write title
        titleFont = ImageFont.truetype("font/arial.ttf", 22)
        writeToImage(image, item["name"], (10, 310), titleFont, "black", 3)
        abstractFont = ImageFont.truetype("font/arial.ttf", 15)
        writeToImage(image, item["information"], (10, 390), abstractFont, "gray", 4)
        contentFont = ImageFont.truetype("font/arial.ttf", 20)
        writeToImage(image, item["born_date"], (10, 460), contentFont, "black", 11)
        name = "news-" + str(index) + ".png"
        image.save("news/" + name)
        print("saved to " + "news/" + name)


if __name__ == "__main__":
    makeFastNews(crawNewsData("https://www.imdb.com/", "https://www.imdb.com/list/ls058011111/"))