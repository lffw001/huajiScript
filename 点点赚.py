


#   --------------------------------注释&变量区--------------------------------
#   入口 微信打开： https://168740033-1257141735.cos-website.ap-nanjing.myqcloud.com/index.html?pid=16345
#               或:https://168719171-1257141735.cos-website.ap-nanjing.myqcloud.com/index.html?pid=16345
#   找含sx.shuxiangby.cn域名下的cookie中的user_openid,uid,PHPSESSID的值
#   user_openid=**** 只要**** 其余两项也是如此
#   变量格式user_openid的值#uid的值#PHPSESSID的值
#   变量名：yuanshen_ddz 多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   在抓取上面的参数时同时抓取请求头中的user-agent填入yuanshen_useragent 之前有抓过可乐或鱼儿等阅读的无需更改 同用的
#
#   检测配置：
#   在yuanshen_apptoken，yuanshen_topicid分别填入你的wxpusher的apptoken和topicid
#   注意是填的topicid而不是你的uid 不要傻乎乎把uid填上去 填了不推送文章包黑号的
#   不懂看 https://wxpusher.zjiecode.com/docs/#/ 或 百度 或 打钱
#
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#   --------------------------------代码区--------------------------------

'''
Powered By Huaji
Create at [2024-08-03 14:37]

 __    __   __    __       ___             __   __  
|  |  |  | |  |  |  |     /   \           |  | |  | 
|  |__|  | |  |  |  |    /  ^  \          |  | |  | 
|   __   | |  |  |  |   /  /_\  \   .--.  |  | |  | 
|  |  |  | |  `--'  |  /  _____  \  |  `--'  | |  | 
|__|  |__|  \______/  /__/     \__\  \______/  |__|                                                

'''

import base64, zlib, lzma, bz2, gzip
exec((lambda c: compile(c, '<string>', 'exec'))(zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode('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')))))。decode()))
#!Look Your Mother! At the end there was nothing!
