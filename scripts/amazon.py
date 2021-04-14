import requests
from bs4 import BeautifulSoup as bs
import time


def getReviews(productUrl):
    # productUrl = "https://www.amazon.in/Orient-Electric-Minimagic-CP0801H-8-Litre/dp/B079QLLWXX/ref=pd_sbs_3?pd_rd_w=4bHuo&pf_rd_p=99c630ba-ffa4-4940-9542-3945145447d6&pf_rd_r=KNMARQMXD3P4VWPNEH4Y&pd_rd_r=f3fef081-e943-406b-afee-3224e92fa715&pd_rd_wg=olL7S&pd_rd_i=B079QLLWXX&psc=1"
    # productUrl = "https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJXP4/ref=sr_1_1_sspa?dchild=1&keywords=Boat+earphones&qid=1615064612&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVpDUVpPV0FMWTdXJmVuY3J5cHRlZElkPUEwNzI4ODI4TkpYVjRYS1o3NjNaJmVuY3J5cHRlZEFkSWQ9QTAwNTkxNzkzUUc2SVo2WFJVU0tJJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
    # productUrl = "https://www.amazon.in/dp/B077PWJ8RS/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=2FYENW5DAC6643DF66FW&pf_rd_p=ff783bb0-dce0-41db-a9b3-87362ba499a5"
    reviewUrl = productUrl[:productUrl.find(
        "dp")]+"product-reviews/"+productUrl[productUrl.find("dp")+3:productUrl.find("dp")+13]+"?pageNumber="

    # print(reviewUrl)
    reviewTitle = []
    reviewText = []

    count = 100
    i = 0
    while len(reviewTitle) < count:
        time.sleep(0.1)
        i += 1

        if i == 30:
            # scan 20 pages
            break

        tempUrl = reviewUrl+str(i)+"&sortBy=recent"
        # print(tempUrl)
        res = requests.get(tempUrl)

        soup = bs(res.content, "lxml")
        reviewTitleElements = soup.findAll("a", class_="review-title-content")
        reviewTextElements = soup.findAll("span", class_="review-text")

        for ele in reviewTitleElements:
            reviewTitle.append(ele.text[1:-1])

        for ele in reviewTextElements:
            reviewText.append(ele.text.strip())
    return reviewText

    # print(len(reviewTitle), len(reviewText))
    # print(reviewText)
    # for i in range(len(reviewTitle)):
    #     print("REVIEW NUMBER. "+str(i))
    #     print(reviewTitle[i])
    #     print(reviewText[i])
    #     print()
