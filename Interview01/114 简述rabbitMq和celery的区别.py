# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/22 0022 下午 9:33'

"""
1 rabbitmq 是管理消息，celery是管理任务
2 celery是分布式任务队列，它的基本工作原理就是管理分配任务到不同的服务器，
并且取得结果。celery不能解决服务器之间的通信。
rabbitmq是作为一个消息队列管理器引入到celery中，负责处理服务器之间的通信。

简述rabbitmq：
生产者通过Exchange（交换器）将消息发送到队列。
生产者将教习发送到Exchange，由Exchange再将消息路由到一个或多个Queue，
这里会过滤掉不符合路由规则的消息。
RabbitMQ通过Binding将Exchange和Queue连接在一起，这样Exchange就知道如何将消息准确
的推送到Queue中。
在绑定（Binding）Exchange和Queue的同时，一般会指定一个Binding Key，
生产者将消息发送给Exchange的时候，一般会产生一个Routing Key，当
Routing key和binding key对应上的时候，消息就会发送到对应的Queue中区。

简述Celery：
celery首先是异步队列。
celery支持使用任务队列的方式在分布的机器、进程、线程上执行任务调度。
celery用消息通信，通常使用中间人（broker）在客户端和worker间斡旋。
这个过程从客户端向队列添加消息开始，之后中间人把消息派发给worker。
celery本身不提供消息服务，但是可以方便的和第三方提供的消息中间件集成.

celery就像一个钩子附在函数上，当函数被调用时，这个钩子会将这个调用的请求
存储在指定的broker中，然后worker进程从broker中取出调用请求去执行，从而实现
异步和分布式。
"""