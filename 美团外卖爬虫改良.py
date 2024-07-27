import datetime
import json
import pandas as pd
from tqdm import tqdm
from lxml import etree
from auth_db import UserAuthenticator

def read_config(config_path):
    """读取并返回配置文件内容"""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"配置文件 {config_path} 不存在，使用默认配置。")
        return {
            'all_info': '//div[@class="textPart_CDl999"]',
            'store_name': './/div[@class="nameLine_h53bsq"]',
            'base_info': './/div[@class="infoCount_SzLoSC"]',
            'suggestion_info': './/div[@class="recommendItem_RZbLVG"]',
            'discount_content': './/div[@class="d_sublabel"]',
            'sheet_name': '美团h5数据',
            'path': 'C:\\Users\\Administrator\\Desktop\\美团爬虫\\',
            'html_name': '美团外卖.mht',
            'excel_name': '美团数据',
            'format_time': '%Y-%m-%d-%H-%M-%S'
        }


def parse_html(html_path, xpath_dict):
    """解析HTML文件并返回ElementTree对象"""
    parser = etree.HTMLParser()
    try:
        return etree.parse(html_path, parser)
    except etree.XMLSyntaxError as e:
        print(f"解析 HTML 文件时发生错误：{e}")
        return None


def extract_data(tree, xpath_dict):
    """从ElementTree对象中提取数据并返回列表"""
    data = []
    elements = tree.xpath(xpath_dict['all_info'])
    for element in tqdm(elements, desc="Processing elements"):
        item = {
            "店名": element.xpath(xpath_dict['store_name'] + "//text()")[0].strip(),
            "月售": float(element.xpath(xpath_dict['base_info'] + "//text()")[0].replace('+', '').strip()),
            "起送": float(element.xpath(xpath_dict['base_info'] + "//text()")[1].strip()),
            "配送费": float(element.xpath(xpath_dict['base_info'] + "//text()")[2].strip())
        }
        for i, suggestion in enumerate(element.xpath(xpath_dict['suggestion_info'] + "//text()"), start=1):
            item[f"建议信息{i}"] = suggestion.strip()
        for i, discount in enumerate(element.xpath(xpath_dict['discount_content'] + "//text()"), start=1):
            item[f"优惠内容{i}"] = discount.strip()
        data.append(item)
    return data


def save_to_excel(data, output_path, sheet_name, timestamp_format):
    """将数据保存到Excel文件中"""
    now = datetime.datetime.now().strftime(timestamp_format)
    excel_name = f"{output_path}{sheet_name}_{now}.xlsx"
    df = pd.DataFrame(data)
    df.to_excel(excel_name, sheet_name=sheet_name, index=False)
    print(f"数据已成功保存到 {excel_name}")


def main():
    config_path = 'config.json'
    xpath_dict = read_config(config_path)

    if not xpath_dict:
        print("配置文件读取失败，程序退出。")
        return

    html_path = xpath_dict['path'] + xpath_dict['html_name']
    tree = parse_html(html_path, xpath_dict)
    
    if tree is not None:
        data = extract_data(tree, xpath_dict)
        save_to_excel(data, xpath_dict['path'], xpath_dict['sheet_name'], xpath_dict['format_time'])
    else:
        print("解析HTML文件失败，无法提取数据。")


if __name__ == "__main__":

    

    authenticator = UserAuthenticator(DB_CONFIG)
    authenticator.connect()
    res = authenticator.login_loop()
    authenticator.disconnect()
    if res:
        main()