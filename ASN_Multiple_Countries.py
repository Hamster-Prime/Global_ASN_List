'''
Author: ASN Fetcher Script
Date: 2025-10-05
LastEditors: Auto-generated
FilePath: /ASN_Multiple_Countries.py

Copyright © 2025, All Rights Reserved. 
'''
import requests
from lxml import etree
import time
import os
import sys

countries = [
    'CN',  # 中国
    'HK',  # 香港
    'MO',  # 澳门
    'TW',  # 台湾
    'PH',  # 菲律宾
    'VN',  # 越南
    'LA',  # 老挝
    'KH',  # 柬埔寨
    'TH',  # 泰国
    'MM',  # 缅甸
    'JP',  # 日本
    'KR',  # 韩国
    'KP',  # 朝鲜
    'MN',  # 蒙古
    'SG',  # 新加坡
    'MY',  # 马来西亚
    'ID',  # 印度尼西亚
    'BN',  # 文莱
    'TL',  # 东帝汶
    'IN',  # 印度
    'PK',  # 巴基斯坦
    'BD',  # 孟加拉国
    'LK',  # 斯里兰卡
    'NP',  # 尼泊尔
    'BT',  # 不丹
    'MV',  # 马尔代夫
    'DE',  # 德国
    'FR',  # 法国
    'GB',  # 英国
    'IE',  # 爱尔兰
    'IT',  # 意大利
    'ES',  # 西班牙
    'PT',  # 葡萄牙
    'NL',  # 荷兰
    'BE',  # 比利时
    'LU',  # 卢森堡
    'CH',  # 瑞士
    'AT',  # 奥地利
    'DK',  # 丹麦
    'SE',  # 瑞典
    'NO',  # 挪威
    'FI',  # 芬兰
    'IS',  # 冰岛
    'PL',  # 波兰
    'CZ',  # 捷克
    'HU',  # 匈牙利
    'GR',  # 希腊
    'RU',  # 俄罗斯
    'UA',  # 乌克兰
    'BY',  # 白俄罗斯
    'RO',  # 罗马尼亚
    'BG',  # 保加利亚
    'RS',  # 塞尔维亚
    'HR',  # 克罗地亚
    'SI',  # 斯洛文尼亚
    'SK',  # 斯洛伐克
    'BA',  # 波斯尼亚和黑塞哥维那
    'ME',  # 黑山
    'MK',  # 北马其顿
    'AL',  # 阿尔巴尼亚
    'LT',  # 立陶宛
    'LV',  # 拉脱维亚
    'EE',  # 爱沙尼亚
    'MD',  # 摩尔多瓦
    'CY',  # 塞浦路斯
    'MT',  # 马耳他
    'TR',  # 土耳其
    'SA',  # 沙特阿拉伯
    'AE',  # 阿联酋
    'QA',  # 卡塔尔
    'KW',  # 科威特
    'BH',  # 巴林
    'OM',  # 阿曼
    'YE',  # 也门
    'JO',  # 约旦
    'IL',  # 以色列
    'PS',  # 巴勒斯坦
    'LB',  # 黎巴嫩
    'SY',  # 叙利亚
    'IQ',  # 伊拉克
    'IR',  # 伊朗
    'AF',  # 阿富汗
    'KZ',  # 哈萨克斯坦
    'UZ',  # 乌兹别克斯坦
    'TM',  # 土库曼斯坦
    'KG',  # 吉尔吉斯斯坦
    'TJ',  # 塔吉克斯坦
    'GE',  # 格鲁吉亚
    'AM',  # 亚美尼亚
    'AZ',  # 阿塞拜疆
    'AU',  # 澳大利亚
    'NZ',  # 新西兰
    'PG',  # 巴布亚新几内亚
    'FJ',  # 斐济
    'SB',  # 所罗门群岛
    'VU',  # 瓦努阿图
    'WS',  # 萨摩亚
    'TO',  # 汤加
    'US',  # 美国
    'CA',  # 加拿大
    'MX',  # 墨西哥
    'BR',  # 巴西
    'AR',  # 阿根廷
    'CL',  # 智利
    'CO',  # 哥伦比亚
    'PE',  # 秘鲁
    'VE',  # 委内瑞拉
    'EC',  # 厄瓜多尔
    'BO',  # 玻利维亚
    'PY',  # 巴拉圭
    'UY',  # 乌拉圭
    'GT',  # 危地马拉
    'BZ',  # 伯利兹
    'SV',  # 萨尔瓦多
    'HN',  # 洪都拉斯
    'NI',  # 尼加拉瓜
    'CR',  # 哥斯达黎加
    'PA',  # 巴拿马
    'CU',  # 古巴
    'BS',  # 巴哈马
    'JM',  # 牙买加
    'HT',  # 海地
    'DO',  # 多米尼加共和国
    'EG',  # 埃及
    'LY',  # 利比亚
    'DZ',  # 阿尔及利亚
    'MA',  # 摩洛哥
    'SD',  # 苏丹
    'ET',  # 埃塞俄比亚
    'SO',  # 索马里
    'KE',  # 肯尼亚
    'TZ',  # 坦桑尼亚
    'ZA',  # 南非
    'NG',  # 尼日利亚
    'GH',  # 加纳
    'CI',  # 科特迪瓦
    'SN',  # 塞内加尔
    'CM',  # 喀麦隆
    'AO',  # 安哥拉
    'ZM',  # 赞比亚
    'ZW'   # 津巴布韦
]

def initFile(country_code):
    """初始化特定国家的ASN文件"""
    asn_dir = "ASN"
    if not os.path.exists(asn_dir):
        os.makedirs(asn_dir)
        print(f"📁 创建ASN目录: {asn_dir}")
    
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    filename = os.path.join(asn_dir, f"{country_code}_ASN.rsc")
    try:
        with open(filename, "w", encoding="utf-8") as asnFile:
            asnFile.write(f"# ASN Information in {country_code}.\n")
            asnFile.write("# Last Updated: UTC " + localTime + "\n")
            asnFile.write("# Made by ASN Fetcher Script, All rights reserved.\n\n")
            asnFile.write(f'/log info "Loading {country_code} ASN list"\n')
            asnFile.write("/routing filter num-list\n")
        return filename
    except Exception as e:
        print(f"错误: 无法创建文件 {filename}: {e}")
        return None

def saveLatestASN(country_code, max_retries=3):
    """获取并保存指定国家的ASN信息"""
    url = f"https://bgp.he.net/country/{country_code}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    
    for attempt in range(max_retries):
        try:
            print(f"正在获取 {country_code} 的ASN信息... (尝试 {attempt + 1}/{max_retries})")
            r = requests.get(url=url, headers=headers, timeout=30).text
            tree = etree.HTML(r)
            asns = tree.xpath('//*[@id="asns"]/tbody/tr')
            
            if not asns:
                print(f"警告: 在 {country_code} 没有找到ASN信息")
                return 0
            
            filename = initFile(country_code)
            if filename is None:
                print(f"错误: 无法为 {country_code} 创建文件")
                return -1
                
            asn_count = 0
            
            for asn in asns:
                try:
                    asnNumber = asn.xpath('td[1]/a')[0].text.replace('AS','')
                    asnNameElement = asn.xpath('td[2]')[0]
                    asnName = asnNameElement.text if asnNameElement.text else "未知名称"
                    
                    if asnNumber:
                        routerOSCmd = f":do {{ add list={country_code}_ASN range={asnNumber} }} on-error={{}}"
                        try:
                            with open(filename, "a", encoding="utf-8") as asnFile:
                                asnFile.write(routerOSCmd + "\n")
                            asn_count += 1
                        except Exception as e:
                            print(f"写入文件 {filename} 时出错: {e}")
                            return -1
                except Exception as e:
                    print(f"解析 {country_code} 的ASN记录时出错: {e}")
                    continue
            
            print(f"✓ 成功获取 {country_code} 的 {asn_count} 个ASN记录")
            return asn_count
            
        except requests.RequestException as e:
            print(f"网络错误 (尝试 {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"等待 {(attempt + 1) * 2} 秒后重试...")
                time.sleep((attempt + 1) * 2)
            else:
                print(f"✗ 获取 {country_code} 的ASN信息失败: {e}")
                return -1
        except Exception as e:
            print(f"✗ 获取 {country_code} 的ASN信息时发生未知错误: {e}")
            return -1
    
    return -1

def createSummaryFile(results):
    """创建汇总文件并更新README"""
    asn_dir = "ASN"
    if not os.path.exists(asn_dir):
        os.makedirs(asn_dir)
    
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    summary_file = os.path.join(asn_dir, "ASN_Summary.txt")

    total_asns = sum(results.values())
    successful_countries = len([c for c, count in results.items() if count > 0])
    failed_countries = len([c for c, count in results.items() if count == 0])
    error_countries = len([c for c, count in results.items() if count == -1])
    
    try:
        with open(summary_file, "w", encoding="utf-8") as summary:
            summary.write("=== ASN信息获取汇总 ===\n")
            summary.write(f"获取时间: {localTime}\n")
            summary.write("="*50 + "\n\n")
            
            for country, count in results.items():
                summary.write(f"{country}: {count} 个ASN\n")
            
            summary.write(f"\n总计: {total_asns} 个ASN记录\n")
            summary.write(f"成功获取: {successful_countries} 个国家\n")
            summary.write(f"失败或无数据: {failed_countries} 个国家\n")
            if error_countries > 0:
                summary.write(f"出现错误: {error_countries} 个国家\n")
        
        print(f"📊 汇总文件已保存: {summary_file}")

        updateReadme(localTime, results, total_asns, successful_countries, failed_countries, error_countries)
        
    except Exception as e:
        print(f"错误: 无法创建汇总文件 {summary_file}: {e}")

def updateReadme(update_time, results, total_asns, successful_countries, failed_countries, error_countries):
    """更新README文件"""
    try:
        readme_content = """# ASN 自动获取工具

**注意：** 本工具从公开的BGP信息网站获取数据，请遵守相关网站的使用条款和访问频率限制。

---

## 📊 最新统计信息

**最后更新时间:** {update_time}

### 📈 总体统计
- **总ASN记录数:** {total_asns:,} 个
- **支持国家/地区:** {total_countries} 个
- **成功获取:** {successful_countries} 个国家
- **无数据:** {failed_countries} 个国家
{error_info}

### 🌍 各国家ASN数量 (Top 20)

| 国家代码 | ASN数量 | 状态 |
|---------|---------|------|
{country_table}

### 📁 生成的文件

所有文件保存在 `ASN/` 目录下：
- 配置文件：`ASN/{{国家代码}}_ASN.rsc`
- 汇总信息：`ASN/ASN_Summary.txt`

---

*此信息由脚本自动更新于 {update_time}*
""".format(
            update_time=update_time,
            total_asns=total_asns,
            total_countries=len(results),
            successful_countries=successful_countries,
            failed_countries=failed_countries,
            error_info=f"- **出现错误:** {error_countries} 个国家\n" if error_countries > 0 else "",
            country_table=generateCountryTable(results)
        )
        
        with open("README.md", "w", encoding="utf-8") as readme:
            readme.write(readme_content)
        
        print(f"📝 README.md 已更新")
        
    except Exception as e:
        print(f"错误: 无法更新README文件: {e}")

def generateCountryTable(results):
    """生成国家ASN数量表格"""
    valid_results = [(country, count) for country, count in results.items() if count > 0]
    sorted_results = sorted(valid_results, key=lambda x: x[1], reverse=True)
    
    table_rows = []
    for i, (country, count) in enumerate(sorted_results[:20]):
        status = "✅ 成功"
        table_rows.append(f"| {country} | {count:,} | {status} |")
    
    return "\n".join(table_rows) if table_rows else "| 暂无数据 | - | - |"

def main():
    """主函数"""
    print("🚀 开始获取多国ASN信息...")
    print(f"📍 目标国家: {', '.join(countries)}")
    print("="*60)
    
    results = {}
    failed_countries = []
    error_countries = []

    delay_seconds = int(os.getenv('ASN_FETCH_DELAY', '2'))
    max_retries = int(os.getenv('ASN_MAX_RETRIES', '3'))
    
    total_countries = len(countries)
    processed = 0
    
    for country in countries:
        processed += 1
        print(f"\n[{processed}/{total_countries}] 处理国家: {country}")
        
        asn_count = saveLatestASN(country, max_retries)
        results[country] = asn_count
        
        if asn_count == 0:
            failed_countries.append(country)
        elif asn_count == -1:
            error_countries.append(country)

        if os.getenv('CI') != 'true':
            time.sleep(delay_seconds)
        else:
            time.sleep(1)

    createSummaryFile(results)
    
    print("\n" + "="*60)
    print("📊 ASN信息获取完成！")

    successful = len([c for c, count in results.items() if count > 0])
    failed = len(failed_countries)
    errors = len(error_countries)
    
    print(f"✅ 成功: {successful} 个国家")
    print(f"⚠️  无数据: {failed} 个国家")
    print(f"❌ 错误: {errors} 个国家")
    
    if failed_countries:
        print(f"⚠️  无数据的国家: {', '.join(failed_countries)}")
    if error_countries:
        print(f"❌ 出错的国家: {', '.join(error_countries)}")
    
    print("\n📁 生成的文件 (ASN目录下):")
    total_asns = 0
    for country in countries:
        if results[country] > 0:
            print(f"  - ASN/{country}_ASN.rsc ({results[country]} 个ASN)")
            total_asns += results[country]
    print(f"  - ASN/ASN_Summary.txt (汇总信息)")
    print(f"\n📈 总计: {total_asns} 个ASN记录")

    if errors > 0:
        print(f"\n⚠️  由于存在错误，进程将以退出码1结束")
        sys.exit(1)
    elif failed > len(countries) // 2:
        print(f"\n⚠️  由于过多国家获取失败，进程将以退出码1结束")
        sys.exit(1)
    else:
        print(f"\n🎉 处理完成！")
        sys.exit(0)

if __name__ == "__main__":
    main()
