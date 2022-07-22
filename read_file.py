# 导入相关模块
import pymongo
import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.signal import argrelextrema
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Bench Data Visualization", page_icon=":bar_chart:", layout="wide")

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['IRCdatabase']
tablefile = db['IRB1210axis2_03_endurance']
db2 = client['opcdatabase']
tabledata = db2['RV27C_01_collection']

#'''读取txt'''
# dt=pd.read_csv('1#-1118h_20211221.txt',skiprows=13,index_col=None,sep='\t')
# data=pd.DataFrame(dt)
# t=data['%Time_s']
# speed=data['GB_IRB1210_ax2__6464__1']
# position=data['GB_IRB1210_ax2__1717__1']
# torque=data['GB_IRB1210_ax2__4947__1']

# 读取mongodb file数据库数据
dataf = pd.DataFrame(list(tablefile.find()))
dataf=dataf.iloc[181760:,:]

t=dataf['Time'].astype(float)
speed=dataf['GB_IRB1210_ax2__speed__1'].astype(float)
position=dataf['GB_IRB1210_ax2__position__1'].astype(float)
torque=dataf['GB_IRB1210_ax2__torque__1'].astype(float)

# 读取mongodb data数据库数据
datad = pd.DataFrame(list(tabledata.find().sort('_id', -1).limit(1)))
# print(datad)
benchname=datad['bench name'][0]
timetotal=round(datad['hour'][0].astype(float),1)
cycle=datad['cycle'][0]
date=datad['time'][0]
running=datad['state'][0]
# print(cycle)


# 侧边栏
st.sidebar.header("Select data here:")
option = st.sidebar.selectbox(
    "Select Bench:",
    ('IRB1210-Axis2-1', 'IRB1210-Axis2-2', 'IRB1210-Axis2-3')
)

genre = st.sidebar.radio(
                "Select Number",
                ('1#', '2#', '3#','4#'))

st.title(":bar_chart: Bench Data Visualization")
st.markdown("##")

# 3列布局
left_column, middlel_column, middlem_column, middler_column, right_column = st.columns(5)

# 添加相关信息
with left_column:
    st.subheader("BenchName:")
    st.subheader(benchname)
with middlel_column:
    st.subheader("Time:")
    st.subheader(timetotal)
with middlem_column:
    st.subheader("Cycle:")
    st.subheader(cycle)
with middler_column:
    st.subheader("Running State:")
    st.subheader(running)
with right_column:
    st.subheader("Date:")
    st.subheader(date)

st.markdown("""---""")


# fig_product_sales = px.scatter(
#     speed,
#     x="GB_IRB1210_ax2__speed__1",
#     y="GB_IRB1210_ax2__speed__1",
#     orientation="h",
#     title="<b>每种商品销售总额</b>",
#     # color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#     template="plotly_white",
# )
# fig_product_sales.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )
#
# fig_hourly_sales = px.scatter(
#     torque,
#     x="GB_IRB1210_ax2__torque__1",
#     y="GB_IRB1210_ax2__torque__1",
#     title="<b>每小时销售总额</b>",
#     # color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )

fig1 = px.line(data_frame=None, x=t, y=speed)
fig2 = px.line(data_frame=None, x=t, y=torque)
# st.plotly_chart(fig2)


left_column, right_column = st.columns(2)

left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)


# 隐藏streamlit默认格式信息
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <![]()yle>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)



#'''matplotlib 绘图'''
# plt.figure(figsize=(12,8))
# plt.subplot(3,1,1)
# plt.plot(speed)
#
# plt.subplot(3,1,2)
# plt.plot(position)
# plt.subplot(3,1,3)
#
# plt.plot(torque)
# plt.show()


#'''读取mongodb数据库方法二'''
# cursor = table.find()
# columns = []
# data_list = []
# for data in cursor:
#     if len(columns) == 0:
#         columns = list(data)
#         # print(columns)
#         columns.remove('_id')
#     row_data = []
#     for column in columns:
#         row_data.append(float(data[column]))
#     # print(list(row_data))
#     data_list.append(row_data)
# datafr = pd.DataFrame(list(data_list))
# client.close()
#
# plt.figure(figsize=(12,8))
# plt.subplot(3,1,1)
# plt.plot(datafr[0],datafr[1])
# plt.subplot(3,1,2)
# plt.plot(datafr[0],datafr[2])
# plt.subplot(3,1,3)
#
# plt.plot(datafr[0],datafr[3])
# plt.show()