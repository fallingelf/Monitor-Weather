一·用途：
用于监控丽江天气，频率为每分钟访问一次，
监控数据为湿度与云量，
假如湿度超90%或云量大于5则播放音乐，
程序运行的历史数据存放于WeaInf.txt，
整个文件夹LiJiang_weather放入C盘之下，否则需要修改路径。


二·操作步骤
1.安装python
双击exe文件
2.打开终端安装模块pygame:
>python -m pip install pygame
3.进入脚本文件：
cd C:\LiJiang_weather
4.运行脚本：
python LiJiangWeather.py 

Note：
WeaInf文件存储获得的数据用于日后程序的完善