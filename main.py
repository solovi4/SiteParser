from textFromSite import get_text
from pathFromUrl import get_path
from writeFile import write
import config

conf = config.load_config();
inputUrl = input()
#inputUrl = "https://www.e1.ru/news/spool/news_id-65323341.html"
#inputUrl = "https://lenta.ru/news/2018/08/29/child_policy/"
text = get_text(inputUrl, conf)
file_name = get_path(inputUrl)
write(file_name, text)
