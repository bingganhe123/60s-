## 60s读世界
# 定时向指定群或列表好友发送每日60s读世界
# 配置方法
# 注意 使用本插件前，需要在商店下载nonebot_plugin_apscheduler（APScheduler 定时任务插件）
60s读世界下载方式
```
pip install nonebot_plugin_read_60s 
```
不要忘记在bot.py里加入
```
nonebot.load_plugin("nonebot_plugin_read_60s")
```
在nonebot的env配置文件中输入以下内容
```
#定时发送配置
read_qq_friends=[12345678910] #设定要发送的QQ好友
read_qq_groups=[123456789,123456789,123456789] #设定要发送的群
read_inform_time=[{"HOUR":9,"MINUTE":1}] #在输入时间的时候 不要 以0开头如{"HOUR":06,"MINUTE":08}是错误的
```
