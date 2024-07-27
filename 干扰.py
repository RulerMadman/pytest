import pandas as pd
import os
from datetime import datetime
use_path = r"C:\Users\5453543\Desktop\干扰"

file_path_name_4G = os.path.join(use_path,'4G.xlsx')   #地址名字组合
file_path_name_5G = os.path.join(use_path,'5G.xlsx')
file_name = os.path.join(use_path,'Top干扰小区明细.xlsx')
file_topname = os.path.join(use_path,'Top干扰小区明细.xlsx')
file_yujingpath = use_path + '\\重点指标预警.txt'
file_path_name_gongcan = os.path.join(use_path,"245G重点场景汇总.xlsx")
siG = pd.read_excel(file_path_name_4G,engine='calamine')   #读取文件
siw = pd.read_excel(file_path_name_5G,engine='calamine')
print('正在读取工参')
gongcan_4G = pd.read_excel(file_path_name_gongcan,sheet_name='4G小区明细')
gongcan_5G = pd.read_excel(file_path_name_gongcan,sheet_name='5G小区明细')
shaixuan_4g = "-104 <= 干扰值 and 干扰值 != 0"
shaixuan_5g = "-104 <= 干扰值 and 干扰值 != 0"
print('筛选干扰值小于-104或等于0')
jieguo_4g = siG.query(shaixuan_4g)        # 利用query筛选
jieguo_5g = siw.query(shaixuan_5g)
jieguo_4g['场景归类'] = pd.Series()
jieguo_4g['物点名称'] = pd.Series()
jieguo_4g['站型'] = pd.Series()
jieguo_5g['场景归类'] = pd.Series()
jieguo_5g['物点名称'] = pd.Series()
jieguo_5g['站型'] = pd.Series()   #添加列
shuliang_4g = len(jieguo_4g['地市'])
print(f"4G小区数量为{shuliang_4g}")
shuliang_5g = len(jieguo_5g['地市'])
print(f"5G小区数量为{shuliang_5g}")
jieguo_4g.to_excel('4G.jieguo.xlsx',index=0)
jieguo_5g.to_excel('5G.jieguo.xlsx',index=0)
print('存储结果')
vlookup_4g = pd.read_excel('4G.jieguo.xlsx',engine='calamine')
vlookup_4g1 =pd.merge(vlookup_4g,gongcan_4G.loc[:,['小区名称','场景归类','物点名称','站型']],how='left',on='小区名称')
vlookup_5g = pd.read_excel('5G.jieguo.xlsx',engine='calamine')
vlookup_5g1 =pd.merge(vlookup_5g,gongcan_5G.loc[:,['小区名称','场景归类','物点名称','站型']],how='left',on='小区名称')
vlookup_4g1.drop(columns=['物点名称_x','站型_x','场景归类_x'],inplace=True)
vlookup_5g1.drop(columns=['物点名称_x','站型_x','场景归类_x'],inplace=True)
print('修改标题')
vlookup_4g1.columns = ['地市','区县','小区名称','小区ID','基站名称','制式','干扰值','生产厂商','频段','时间范围','场景归类','物点名称','站型']
vlookup_5g1.columns = ['地市','区县','小区名称','小区ID','基站名称','制式','干扰值','生产厂商','频段','时间范围','场景归类','物点名称','站型']
vlookup_4g1 = vlookup_4g1[vlookup_4g1['场景归类'].notnull()]   #删除场景归类为空的行
vlookup_5g1 = vlookup_5g1[vlookup_5g1['场景归类'].notnull()]
vlookup_4g1.sort_values(by="干扰值",inplace=True,ascending=False)  #按照干扰值从大到小排序
vlookup_5g1.sort_values(by="干扰值",inplace=True,ascending=False)
file_path_name_jieguo = os.path.join(use_path,'Top干扰小区明细.xlsx')
with pd.ExcelWriter(file_path_name_jieguo) as writer:
    vlookup_5g1.to_excel(writer, sheet_name="5G", index=False)
    vlookup_4g1.to_excel(writer,sheet_name="4G",index=False)
wb_4G = pd.read_excel(file_name,sheet_name='4G',engine='calamine')
wb_5G = pd.read_excel(file_name,sheet_name='5G',engine='calamine')
top_4g = wb_4G['地市'].value_counts().head(2)    #提取前2个地市
top_5g = wb_5G['地市'].value_counts().head(2)
top_4gc = pd.DataFrame({
    '地市' : top_4g.index,
    '次数' : top_4g.values
})
top_5gc = pd.DataFrame({
    '地市' : top_5g.index,
    '次数' : top_5g.values
})
ganrao_4G = int(len(wb_4G['地市']))     #计算一共多少小区
ganrao_5G = int(len(wb_5G['地市']))
tiqu_5G = wb_5G.iloc[0:10]             #提取top10
tiqu_4G = wb_4G.iloc[1:11]
tiqu = pd.concat([tiqu_5G,tiqu_4G],ignore_index=True)       #合并top20
tiqu.drop(['小区ID','基站名称','制式','时间范围','场景归类','频段'],axis=1,inplace=True)
tiqu.to_excel(file_topname,index=False)    #提取top数据
today = datetime.now()
month_str = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
shijian = f'{month_str[today.month - 1]}{today.day}日'
yuju = f"""
【{shijian} 干扰监控】
5G：
    15分钟粒度干扰小区（＞-105dBm）{shuliang_5g}个，重点场景Top干扰小区（＞-105dBm）{ganrao_5G}个，其中{top_5gc['地市'][0]}（{top_5gc['次数'][0]}个）、{top_5gc['地市'][1]}（{top_5gc['次数'][1]}个）重点场景Top干扰小区数量较多，主要集中在2.6G频段。
4G：
    15分钟粒度干扰小区（＞-105dBm）{shuliang_4g}个，重点场景Top干扰小区（＞-105dBm）{ganrao_4G}个，其中{top_4gc['地市'][0]}（{top_4gc['次数'][0]}个）、{top_4gc['地市'][1]}（{top_4gc['次数'][1]}个）重点场景Top干扰小区数量较多，主要集中在FDD1800频段。
     重点场景4/5GTop10干扰小区如下："""

with open(file_yujingpath,'w',encoding='utf-8') as file:
    file.write(yuju)




