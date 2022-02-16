## 60s读世界
# 定时向指定群或列表好友发送每日60s读世界
# 配置方法
下载方式
```
pip install nonebot-plugin-read-60s 
```
在nonebot的env配置文件中输入以下内容
```
LEETCODE_QQ_FRIENDS=[12345678,123456]#设定要发送的QQ好友
LEETCODE_QQ_GROUPS=[1234567]#设定要发送的群
LEETCODE_INFORM_TIME=[{"HOUR":6,"MINUTE":8},{"HOUR":18,"MINUTE":20}]#在输入时间的时候 不要 以0开头如{"HOUR":06,"MINUTE":08}是错误的
```
